from pyboinc.results import old_results, results


def test_can_get_single_result(
    mocker,
    mock_rpc_client,
    single_result_xml,
    single_result_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=single_result_xml,
    )
    assert results(client=mock_rpc_client) == single_result_dict


def test_can_get_multiple_result(
    mocker,
    mock_rpc_client,
    multi_result_xml,
    multi_result_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=multi_result_xml,
    )
    assert results(client=mock_rpc_client) == multi_result_dict


def test_can_get_only_active_results(
    mocker, mock_rpc_client, multi_result_xml, multi_result_dict
):
    m_call = mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=multi_result_xml,
    )
    _ = results(client=mock_rpc_client, active_only=True) == multi_result_dict
    m_call.assert_called_once_with(
        "<get_results><active_only></active_only></get_results>"
    )


def test_can_get_single_old_result(
    mocker,
    mock_rpc_client,
    single_old_result_xml,
    single_old_result_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=single_old_result_xml,
    )
    assert old_results(client=mock_rpc_client) == single_old_result_dict


def test_can_get_multi_old_result(
    mocker,
    mock_rpc_client,
    multi_old_result_xml,
    multi_old_result_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=multi_old_result_xml,
    )
    assert old_results(client=mock_rpc_client) == multi_old_result_dict