import xmltodict

from boinc_client.clients.rpc_client import RpcClient
from boinc_client.models.proxy_settings import ProxyInfo


def get_proxy_settings(client: RpcClient) -> dict:
    rpc_resp = client.make_request("<get_proxy_settings/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return ProxyInfo().load(rpc_json)
