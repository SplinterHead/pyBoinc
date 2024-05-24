from pytest import fixture


@fixture
def proxy_settings_xml() -> str:
    return """<proxy_info>
        <socks_server_name>foo</socks_server_name>
        <socks_server_port>10</socks_server_port>
        <http_server_name>foo</http_server_name>
        <http_server_port>10</http_server_port>
        <socks5_user_name>foo</socks5_user_name>
        <socks5_user_passwd>foo</socks5_user_passwd>
        <socks5_remote_dns>foo</socks5_remote_dns>
        <http_user_name>foo</http_user_name>
        <http_user_passwd>foo</http_user_passwd>
        <no_autodetect>foo</no_autodetect>
        <no_proxy>foo</no_proxy>
    </proxy_info>"""


@fixture
def proxy_settings_dict() -> dict:
    return {
        "proxy_info": {
            "socks_server_name": "foo",
            "socks_server_port": 10,
            "http_server_name": "foo",
            "http_server_port": 10,
            "socks5_user_name": "foo",
            "socks5_user_passwd": "foo",
            "socks5_remote_dns": "foo",
            "http_user_name": "foo",
            "http_user_passwd": "foo",
            "no_autodetect": "foo",
            "no_proxy": "foo",
        }
    }
