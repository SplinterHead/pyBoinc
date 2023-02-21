from marshmallow import Schema, fields, pre_load


class ActiveTask(Schema):
    active_task_state = fields.Int()
    app_version_num = fields.Int()
    slot = fields.Int()
    pid = fields.Int()
    scheduler_state = fields.Int()
    checkpoint_cpu_time = fields.Float()
    fraction_done = fields.Float()
    current_cpu_time = fields.Float()
    elapsed_time = fields.Float()
    swap_size = fields.Float()
    working_set_size = fields.Float()
    working_set_size_smoothed = fields.Float()
    page_fault_rate = fields.Float()
    bytes_sent = fields.Float()
    bytes_received = fields.Float()
    progress_rate = fields.Float()
    graphics_exec_path = fields.Str()
    slot_path = fields.Str()


class Result(Schema):
    name = fields.Str()
    wu_name = fields.Str()
    platform = fields.Str()
    version_num = fields.Int()
    plan_class = fields.Str(allow_none=True)
    project_url = fields.Url()
    final_cpu_time = fields.Float()
    final_elapsed_time = fields.Float()
    exit_status = fields.Int()
    state = fields.Int()
    report_deadline = fields.Float()
    received_time = fields.Float()
    estimated_cpu_time_remaining = fields.Float()
    edf_scheduled = fields.Str(allow_none=True)
    active_task = fields.Nested(ActiveTask())


class Results(Schema):
    results = fields.Nested(Result(many=True))

    @pre_load
    def _convert_none_to_empty_list(self, data, **kwargs):
        data["results"] = data["results"]["result"] if data["results"] else []
        return data