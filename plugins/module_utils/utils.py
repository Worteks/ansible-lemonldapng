from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


@dataclass
class ExportedHeader:
    header: str
    field: str


@dataclass
class locationRule:
    location: str
    rule: str


@dataclass
class VirtualHost:
    """Represent a lemonldap virtualhost with header and rules"""

    name: str
    exported_headers: List[ExportedHeader]
    access_rules: List[locationRule]
    https: bool
    maintenance: bool

    def __init__(
        self,
        name: str,
        exported_headers: dict[str, str],
        access_rules: dict[str, str],
        https: bool = True,
        maintenance: bool = True,
    ):
        super().__init__()
        self.name = name
        self.https = https
        self.maintenance = maintenance
        self.exported_headers = []
        self.access_rules = []
        for eh in exported_headers:
            self.exported_headers.append(
                ExportedHeader(header=eh["header"], field=eh["value"])
            )
        for r in access_rules:
            self.access_rules.append(
                locationRule(location=r["location"], rule=r["rule"])
            )

    def generate_exported_headers_cmd_part(self) -> list[str]:
        cmd = []
        for eh in self.exported_headers:
            cmd += [
                f"exportedHeaders/{self.name}",
                f"{eh.header}",
                f"{eh.field}",
            ]
        return cmd

    def generate_access_rules_cmd_part(self) -> list[str]:
        cmd = []
        for r in self.access_rules:
            cmd += [
                f"locationRules/{self.name}",
                f"{r.location}",
                f"{r.rule}",
            ]
        return cmd

    def generate_https_cmd_part(self) -> list[str]:
        return [f"vhostOptions/{self.name}", "vhostHttps", "1" if self.https else "0"]

    def generate_maintenance_cmd_part(self) -> list[str]:
        return [
            f"vhostOptions/{self.name}",
            "vhostMaintenance",
            "1" if self.maintenance else "0",
        ]


def get_llng_binary_path() -> Optional[Path]:
    possible_llng_cli = [
        "/usr/share/lemonldap-ng/bin/lemonldap-ng-cli",
        "/usr/libexec/lemonldap-ng/bin/lemonldap-ng-cli",
    ]
    for llng_cli in possible_llng_cli:
        # User morse operator ?
        llng_cli_location = Path(llng_cli)
        if llng_cli_location.exists():
            return llng_cli_location
