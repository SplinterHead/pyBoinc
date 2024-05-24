from marshmallow import Schema, fields, post_load, pre_load

from boinc_client.models.helpers import (
    create_lists,
    flatten_data,
    normalise_none_to_list,
    replace_none_string,
    set_bools,
)

""" from boinc_client.models.additional_fields import (
    scheduler_rpc_pending,
    suspended_via_gui,
    dont_request_more_work,
    ended,
    project_files_downloaded_time,
    ready_to_report,
    got_server_ack,
    final_cpu_time,
    final_elapsed_time,
    state,
    exit_status,
    signal,
    project_suspended_via_gui,
    edf_scheduled,
    scheduler_rpc_pending,
    coproc_missing,
    runtime_outlier,
    project_backend
) """



class RscBackoffTime(Schema):
    name = fields.Str()
    value = fields.Float()


class RscBackoffInterval(Schema):
    name = fields.Str()
    value = fields.Float()


class GuiUrl(Schema):
    description = fields.Str()
    name = fields.Str()
    url = fields.Url()


class ProjectState(Schema):
    cpid_time = fields.Float()
    cross_project_id = fields.Str(allow_none=True)
    desired_disk_usage = fields.Float()
    disk_share = fields.Float()
    disk_usage = fields.Float()
    dont_request_more_work = fields.Bool()
    dont_use_dcf = fields.Bool()
    duration_correction_factor = fields.Float()
    elapsed_time = fields.Float()
    email_hash = fields.Str(allow_none=True)
    external_cpid = fields.Str(allow_none=True)
    gui_urls = fields.Nested(GuiUrl(many=True))
    host_create_time = fields.Float()
    host_expavg_credit = fields.Float()
    host_total_credit = fields.Float()
    host_venue = fields.Str(allow_none=True)
    hostid = fields.Int()
    last_rpc_time = fields.Float()
    master_fetch_failures = fields.Int()
    master_url = fields.Str()
    master_url_fetch_pending = fields.Bool()
    min_rpc_time = fields.Float()
    next_rpc_time = fields.Float()
    njobs_error = fields.Int()
    njobs_success = fields.Int()
    nrpc_failures = fields.Int()
    project_dir = fields.Str()
    project_files_downloaded_time = fields.Float()
    project_name = fields.Str()
    rec = fields.Float()
    rec_time = fields.Float()
    resource_share = fields.Float()
    rpc_seqno = fields.Int()
    rsc_backoff_interval = fields.Nested(RscBackoffInterval())
    rsc_backoff_time = fields.Nested(RscBackoffTime())
    sched_priority = fields.Float()
    sched_rpc_pending = fields.Int()
    scheduler_rpc_in_progress = fields.Bool()
    send_job_log = fields.Int()
    send_time_stats_log = fields.Int()
    suspended_via_gui = fields.Bool()
    symstore = fields.Str(allow_none=True)
    team_name = fields.Str(allow_none=True)
    teamid = fields.Int()
    upload_backoff = fields.Float()
    user_create_time = fields.Float()
    user_expavg_credit = fields.Float()
    user_name = fields.Str(allow_none=True)
    user_total_credit = fields.Float()
    userid = fields.Int()
    no_rsc_pref = fields.Bool(allow_none=True)
    venue = fields.Str(allow_none=True)
    verify_files_on_app_start = fields.Bool(allow_none=True)
    attached_via_acct_mgr = fields.Bool(allow_none=True)

    @pre_load
    def _a_create_keys(self, data, **kwargs):
        return create_lists(data, ["gui_urls"])

    @pre_load
    def _b_flatten_data(self, data, **kwargs):
        return flatten_data(data, "gui_urls", "gui_url")

    @pre_load
    def _c_set_bools(self, data, **kwargs):
        return set_bools(
            data,
            [
                "dont_request_more_work",
                "dont_use_dcf",
                "master_url_fetch_pending",
                "scheduler_rpc_in_progress",
                "suspended_via_gui",
            ],
        )

    @post_load
    def _a_replace_none_string(self, data, **kwargs):
        return replace_none_string(data)


class ProjectStatus(Schema):
    project_status = fields.Nested(ProjectState(many=True), data_key="projects")

    @pre_load
    def _a_normalise_none(self, data, **kwargs):
        return normalise_none_to_list(data, "projects")

    @pre_load
    def _b_flatten_data(self, data, **kwargs):
        return flatten_data(data, "projects", "project")
