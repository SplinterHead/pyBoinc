from boinc_client.network import get_proxy_settings


def test_can_get_proxy_settings(
    mocker, mock_rpc_client, proxy_settings_xml, proxy_settings_dict
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=proxy_settings_xml,
    )
    assert get_proxy_settings(client=mock_rpc_client) == proxy_settings_dict
    assert True
