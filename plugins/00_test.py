from module_utils.utils import VirtualHost

exported_headers = [{"header": "x-wing", "value": "john"}]
access_rules = [{"location": "/bob", "rule": "denied"}]
vhost = VirtualHost(
    name="alice.com", exported_headers=exported_headers, access_rules=access_rules
)


def test_exported_headers():
    assert vhost.generate_exported_headers_cmd_part() == [
        "exportedHeaders/alice.com",
        "x-wing",
        "john",
    ]


def test_access_rules():
    assert vhost.generate_access_rules_cmd_part() == [
        "locationRules/alice.com",
        "/bob",
        "denied",
    ]
