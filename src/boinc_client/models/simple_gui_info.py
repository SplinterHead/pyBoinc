from marshmallow import Schema, fields, pre_load

from boinc_client.models.project_status import ProjectState
from boinc_client.models.result import Result


# Update the ProjectState schema to include the missing fields
class UpdatedProjectState(ProjectState):
    verify_files_on_app_start = fields.Bool(required=False, missing=None)
    attached_via_acct_mgr = fields.Bool(required=False, missing=None)
    venue = fields.Str(required=False, missing=None)
    no_rsc_pref = fields.Str(required=False, missing=None)
    trickle_up_pending = fields.Bool(required=False, missing=None)


class GuiInfo(Schema):
    # Use the updated schema for projects
    projects = fields.Nested(UpdatedProjectState(many=True), data_key="project")
    results = fields.Nested(Result(many=True), data_key="result")


class SimpleGuiInfo(Schema):
    gui_info = fields.Nested(GuiInfo(), data_key="simple_gui_info")

    @pre_load
    def _a_normalise_none(self, data, **kwargs):
        if not data["simple_gui_info"]:
            data["simple_gui_info"] = {"project": [], "result": []}
        return data
