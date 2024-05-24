import logging

import xmltodict
from marshmallow import ValidationError

from boinc_client.clients.rpc_client import RpcClient
from boinc_client.models.generic_response import GenericResponse
from boinc_client.models.global_preference_override import GlobalPreferenceOverrides
from boinc_client.models.global_preferences import GlobalPreferences

logger = logging.getLogger(__name__)
logging.basicConfig(filename="boinc_client.log", encoding="utf-8", level=logging.DEBUG)


def get_global_prefs_file(client: RpcClient) -> dict:
    """Get the contents of the global_prefs.xml file if present."""
    logger.info("Retrieving Global Prefs file")
    rpc_resp = client.make_request("<get_global_prefs_file/>")
    rpc_json = xmltodict.parse(rpc_resp)
    logger.debug(rpc_json)
    try:
        logger.debug("Converting to GlobalPreferences model")
        return GlobalPreferences().load(rpc_json)
    except ValidationError:
        logger.debug("Converting to GenericResponse model")
        return GenericResponse().load(rpc_json)


def get_global_prefs_override(client: RpcClient):
    """Get the contents of the global_prefs_override.xml file if present."""
    logger.info("Retrieving Global Prefs Override file")
    rpc_resp = client.make_request("<get_global_prefs_override/>")
    rpc_json = xmltodict.parse(rpc_resp)
    logger.debug(rpc_json)
    try:
        logger.debug("Converting to GlobalPreferenceOverrides model")
        return GlobalPreferenceOverrides().load(rpc_json)
    except ValidationError:
        logger.debug("Converting to GenericResponse model")
        return GenericResponse().load(rpc_json)


def get_global_prefs_working(client: RpcClient):
    """Get the currently used global_prefs."""
    logger.info("Retrieving active Global Prefs")
    rpc_resp = client.make_request("<get_global_prefs_working/>")
    rpc_json = xmltodict.parse(rpc_resp)
    logger.debug(rpc_json)
    logger.debug("Converting to GlobalPreferences model")
    return GlobalPreferences().load(rpc_json)


def set_global_prefs_override(client: RpcClient, override: dict):
    """Write the global_prefs_override.xml file."""
    logger.info("Setting the contents of Global Prefs file")
    logger.debug(override)
    override_xml = "".join([f"<{k}>{v}</{k}>" for k, v in override.items()])
    logger.debug(override_xml)
    rpc_resp = client.make_request(
        f"""<set_global_prefs_override>
        <global_preferences>
        {override_xml}
        </global_preferences>
        </set_global_prefs_override>"""
    )
    rpc_json = xmltodict.parse(rpc_resp)
    logger.debug(rpc_json)
    logger.debug("Converting to GenericResponse model")
    return GenericResponse().load(rpc_json)


def read_global_prefs_override(client: RpcClient):
    """Read the global_prefs_override.xml file and set the preferences accordingly."""
    logger.info("Instructing BOINC Client to refresh the Global Prefs")
    rpc_resp = client.make_request("<read_global_prefs_override/>")
    rpc_json = xmltodict.parse(rpc_resp)
    logger.debug(rpc_json)
    logger.debug("Converting to GenericResponse model")
    return GenericResponse().load(rpc_json)


############
# Helpers
############
def update_global_prefs_override(client: RpcClient, override: dict):
    """Helper for updating global prefs without resetting others."""
    logger.info("Updating Global Prefs file")
    current_overrides = get_global_prefs_override(client)
    if "error" in current_overrides:
        merged_overrides = override
    else:
        merged_overrides = {**current_overrides["global_preferences"], **override}
    logger.debug(merged_overrides)
    set_global_prefs_override(client, merged_overrides)
