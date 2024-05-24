from marshmallow import Schema, fields, post_load, pre_load, EXCLUDE

from boinc_client.models.helpers import (
    create_lists,
    normalise_none_to_list,
    replace_none_string,
)
from boinc_client.models.host_info import Host
from boinc_client.models.project_status import ProjectState
from boinc_client.models.result import Result


class NetStats(Schema):
    avg_down = fields.Float()
    avg_time_down = fields.Float()
    avg_time_up = fields.Float()
    avg_up = fields.Float()
    bwdown = fields.Float()
    bwup = fields.Float()


class TimeStats(Schema):
    active_frac = fields.Float()
    client_start_time = fields.Float()
    connected_frac = fields.Float()
    cpu_and_network_available_frac = fields.Float()
    gpu_active_frac = fields.Float()
    now = fields.Float()
    on_frac = fields.Float()
    previous_uptime = fields.Float()
    session_active_duration = fields.Float()
    session_gpu_active_duration = fields.Float()
    total_active_duration = fields.Float()
    total_duration = fields.Float()
    total_gpu_active_duration = fields.Float()
    total_start_time = fields.Float()


class AppDetails(Schema):
    name = fields.Str()
    non_cpu_intensive = fields.Bool()
    user_friendly_name = fields.Str()


class AppFileRef(Schema):
    class Meta:
        unknown = EXCLUDE
    copy_file = fields.Bool()
    file_name = fields.Str()
    main_program = fields.Bool()
    open_name = fields.Str(allow_none=True)

    @pre_load
    def _set_main_program(self, data, **kwargs):
        data["main_program"] = "main_program" in data
        return data

    @pre_load
    def _set_copy_file(self, data, **kwargs):
        data["copy_file"] = "copy_file" in data
        return data

class AppVersion(Schema):
    class Meta:
        unknown = EXCLUDE
    api_version = fields.Str()
    app_name = fields.Str()
    avg_ncpus = fields.Float()
    file_ref = fields.Nested(AppFileRef(many=True), required=False, missing=None)
    flops = fields.Float()
    platform = fields.Str()
    version_num = fields.Int()
    plan_class = fields.Str(allow_none=True)
    is_wrapper = fields.Bool(allow_none=True)
    cmdline = fields.Str(allow_none=True)


class WorkUnit(Schema):
    app_name = fields.Str()
    command_line = fields.Str()
    file_ref = fields.Nested(AppFileRef(many=True))
    name = fields.Str()
    rsc_disk_bound = fields.Float()
    rsc_fpops_bound = fields.Float()
    rsc_fpops_est = fields.Float()
    rsc_memory_bound = fields.Float()
    version_num = fields.Int()
    plan_class = fields.Str(allow_none=True)
    cmdline = fields.Str(allow_none=True)


class GlobalPreferences(Schema):
    battery_charge_min_pct = fields.Float()
    battery_max_temperature = fields.Float()
    confirm_before_connecting = fields.Int()
    cpu_scheduling_period_minutes = fields.Float()
    cpu_usage_limit = fields.Float()
    daily_xfer_limit_mb = fields.Float()
    daily_xfer_period_days = fields.Int()
    disk_interval = fields.Float()
    disk_max_used_gb = fields.Float()
    disk_max_used_pct = fields.Float()
    disk_min_free_gb = fields.Float()
    dont_verify_images = fields.Int()
    end_hour = fields.Float()
    hangup_if_dialed = fields.Int()
    idle_time_to_run = fields.Float()
    leave_apps_in_memory = fields.Int()
    max_bytes_sec_down = fields.Float()
    max_bytes_sec_up = fields.Float()
    max_cpus = fields.Int()
    max_ncpus_pct = fields.Float()
    mod_time = fields.Float()
    net_end_hour = fields.Float()
    net_start_hour = fields.Float()
    network_wifi_only = fields.Int()
    override_file_present = fields.Int()
    ram_max_used_busy_pct = fields.Float()
    ram_max_used_idle_pct = fields.Float()
    run_gpu_if_user_active = fields.Int()
    run_if_user_active = fields.Int()
    run_on_batteries = fields.Int()
    source_project = fields.Str(allow_none=True)
    start_hour = fields.Float()
    suspend_cpu_usage = fields.Float()
    suspend_if_no_recent_input = fields.Float()
    vm_max_used_pct = fields.Float()
    work_buf_additional_days = fields.Float()
    work_buf_min_days = fields.Float()

    @post_load
    def _a_replace_none_string(self, data, **kwargs):
        return replace_none_string(data)


class State(Schema):
    class Meta:
        unknown = EXCLUDE
    app_versions = fields.Nested(
        AppVersion(many=True), data_key="app_version", allow_none=True
    )
    apps = fields.Nested(AppDetails(many=True), data_key="app", allow_none=True)
    core_client_major_version = fields.Int()
    core_client_minor_version = fields.Int()
    core_client_release = fields.Int()
    executing_as_daemon = fields.Bool()
    global_preferences = fields.Nested(GlobalPreferences())
    host_info = fields.Nested(Host())
    net_stats = fields.Nested(NetStats())
    platform = fields.Str()
    platform_name = fields.Str()
    projects = fields.Nested(
        ProjectState(many=True), data_key="project", load_default=[]
    )
    results = fields.Nested(Result(many=True), data_key="result", load_default=[])
    time_stats = fields.Nested(TimeStats())
    work_units = fields.Nested(
        WorkUnit(many=True), data_key="workunit", allow_none=True
    )

    @pre_load
    def _a_create_keys(self, data, **kwargs):
        return create_lists(data, ["app", "app_version", "project", "workunit"])

    @pre_load
    def _b_wrap_dict(self, data, **kwargs):
        data["project"] = (
            [data["project"]] if type(data["project"]) is not list else data["project"]
        )
        return data


class ClientState(Schema):
    client_state = fields.Nested(State())
