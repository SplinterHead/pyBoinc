from marshmallow import Schema, fields


class ProxySettings(Schema):
    autodetect_port = fields.Str()
    autodetect_protocol = fields.Str()
    autodetect_server_name = fields.Str()
    http_server_name = fields.Str(allow_none=True)
    http_server_port = fields.Int(allow_none=True)
    http_user_name = fields.Str(allow_none=True)
    http_user_passwd = fields.Str(allow_none=True)
    no_autodetect = fields.Str(allow_none=True)
    no_proxy = fields.Str(allow_none=True)
    socks5_remote_dns = fields.Str(allow_none=True)
    socks5_user_name = fields.Str(allow_none=True)
    socks5_user_passwd = fields.Str(allow_none=True)
    socks_server_name = fields.Str(allow_none=True)
    socks_server_port = fields.Int(allow_none=True)
    use_http_auth = fields.Str()
    use_http_proxy = fields.Str()
    use_socks_proxy = fields.Str()


class ProxyInfo(Schema):
    proxy_info = fields.Nested(ProxySettings())
