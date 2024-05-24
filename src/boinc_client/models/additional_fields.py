from marshmallow import fields

# Additional fields for ProjectState
scheduler_rpc_pending = fields.Bool()
suspended_via_gui = fields.Bool()
dont_request_more_work = fields.Bool()
ended = fields.Bool()
project_files_downloaded_time = fields.Float()

# Additional fields for Result
ready_to_report = fields.Bool()
got_server_ack = fields.Bool()
final_cpu_time = fields.Float()
final_elapsed_time = fields.Float()
state = fields.Int()
exit_status = fields.Int()
signal = fields.Int()
suspended_via_gui = fields.Bool()
project_suspended_via_gui = fields.Bool()
edf_scheduled = fields.Bool()
scheduler_rpc_pending = fields.Bool()
coproc_missing = fields.Bool()
runtime_outlier = fields.Bool()

# Other additional fields
project_backend = fields.Str()
