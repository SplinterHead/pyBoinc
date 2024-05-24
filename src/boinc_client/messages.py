import logging

import xmltodict

from boinc_client.clients.rpc_client import RpcClient
from boinc_client.models.message_count import MessageCount
from boinc_client.models.messages import Messages
from boinc_client.models.public_notice import Notices

logger = logging.getLogger(__name__)
logging.basicConfig(filename="boinc_client.log", encoding="utf-8", level=logging.DEBUG)


def messages(client: RpcClient, start: int = 0) -> dict:
    """Show messages with sequence numbers beyond the given seqno."""
    logging.info("Getting recent messages")
    rpc_resp = client.make_request(
        f"<get_messages><seqno>{start}</seqno></get_messages>"
    )
    rpc_json = xmltodict.parse(rpc_resp, force_list="msg")
    logger.debug(rpc_json)
    logger.debug("Converting to Messages model")
    return Messages().load(rpc_json)


def message_count(client: RpcClient) -> dict:
    """Show the largest message seqno."""
    logging.info("Getting the count of messages")
    rpc_resp = client.make_request("<get_message_count/>")
    rpc_json = xmltodict.parse(rpc_resp)
    logger.debug(rpc_json)
    logger.debug("Converting to MessageCount model")
    return MessageCount().load(rpc_json)


def public_notices(client: RpcClient, start: int = 1) -> dict:
    """Returns only non-private notices, doesn't require authentication."""
    logging.info("Getting all public messages")
    rpc_resp = client.make_request(
        f"<get_notices_public><seqno>{start}</seqno></get_notices_public>"
    )
    rpc_json = xmltodict.parse(rpc_resp, force_list="notice")
    logger.debug(rpc_json)
    logger.debug("Converting to Notices model")
    return Notices().load(rpc_json)


def get_all_notices(client: RpcClient, start: int = 1) -> dict:
    """Returns both private and non-private notices."""
    logging.info("Getting recent notices")
    rpc_resp = client.make_request(f"<get_notices><seqno>{start}</seqno></get_notices>")
    rpc_json = xmltodict.parse(rpc_resp, force_list="notice")
    logger.debug(rpc_json)
    logger.debug("Converting to Notices model")
    return Notices().load(rpc_json)
