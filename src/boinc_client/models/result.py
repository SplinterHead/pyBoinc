from marshmallow import Schema, fields, pre_load

from boinc_client.models.helpers import flatten_data, normalise_none_to_list


class ActiveTask(Schema):
    active_task_state = fields.Int()
    app_version_num = fields.Int()
    bytes_received = fields.Float()
    bytes_sent = fields.Float()
    checkpoint_cpu_time = fields.Float()
    current_cpu_time = fields.Float()
    elapsed_time = fields.Float()
    fraction_done = fields.Float()
    graphics_exec_path = fields.Str()
    page_fault_rate = fields.Float()
    pid = fields.Int()
    progress_rate = fields.Float()
    scheduler_state = fields.Int()
    slot = fields.Int()
    slot_path = fields.Str()
    swap_size = fields.Float()
    working_set_size = fields.Float()
    working_set_size_smoothed = fields.Float()
    too_large = fields.Bool(required=False, missing=None)


class Result(Schema):
    active_task = fields.Nested(ActiveTask())
    completed_time = fields.Float()
    edf_scheduled = fields.Bool()
    estimated_cpu_time_remaining = fields.Float()
    exit_status = fields.Int()
    final_cpu_time = fields.Float()
    final_elapsed_time = fields.Float()
    name = fields.Str()
    plan_class = fields.Str(allow_none=True)
    platform = fields.Str()
    project_suspended_via_gui = fields.Bool()
    project_url = fields.Url()
    ready_to_report = fields.Bool()
    received_time = fields.Float()
    report_deadline = fields.Float()
    state = fields.Int()
    version_num = fields.Int()
    wu_name = fields.Str()
    report_immediately = fields.Bool(required=False, missing=None)
    resources = fields.Str(required=False, missing=None)
    suspended_via_gui = fields.Bool(required=False, missing=None)

    @pre_load
    def _set_ready(self, data, **kwargs):
        data["ready_to_report"] = "ready_to_report" in data
        return data

    @pre_load
    def _set_scheduled(self, data, **kwargs):
        data["edf_scheduled"] = "edf_scheduled" in data
        return data

    @pre_load
    def _set_suspended(self, data, **kwargs):
        data["project_suspended_via_gui"] = "project_suspended_via_gui" in data
        return data


class Results(Schema):
    results = fields.Nested(Result(many=True))

    @pre_load
    def _a_normalise_none(self, data, **kwargs):
        return normalise_none_to_list(data, "results")

    @pre_load
    def _b_flatten_data(self, data, **kwargs):
        return flatten_data(data, "results", "result")
