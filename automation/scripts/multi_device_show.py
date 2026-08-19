"""Collect operational data from Cisco IOS devices with Netmiko."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Any

import yaml
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException


DEFAULT_COMMANDS = [
    "show ip interface brief",
    "show ip route",
    "show version",
]


def load_inventory(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    """Load devices and commands from a YAML inventory."""
    with path.open(encoding="utf-8") as inventory_file:
        data = yaml.safe_load(inventory_file) or {}

    devices = data.get("devices", [])
    commands = data.get("commands", DEFAULT_COMMANDS)

    if not devices:
        raise ValueError("Inventory must contain at least one device.")

    return devices, commands


def credentials() -> tuple[str, str]:
    """Read credentials from environment variables."""
    username = os.getenv("NETWORK_USERNAME")
    password = os.getenv("NETWORK_PASSWORD")

    if not username or not password:
        raise RuntimeError(
            "Set NETWORK_USERNAME and NETWORK_PASSWORD before running the script."
        )

    return username, password


def collect_commands(
    devices: list[dict[str, Any]], commands: list[str], username: str, password: str
) -> None:
    """Connect to each device and print the requested command output."""
    for device in devices:
        name = device.get("name", device["host"])
        connection_details = {
            "device_type": device["device_type"],
            "host": device["host"],
            "username": username,
            "password": password,
        }

        print(f"\n{'=' * 60}")
        print(f"Connecting to {name} ({device['host']})")
        print(f"{'=' * 60}")

        try:
            with ConnectHandler(**connection_details) as connection:
                for command in commands:
                    print(f"\n### {command} ###")
                    print(connection.send_command(command))
        except (NetmikoAuthenticationException, NetmikoTimeoutException) as error:
            print(f"Connection failed for {name}: {error}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run operational commands across Cisco IOS devices."
    )
    parser.add_argument(
        "--inventory",
        type=Path,
        default=Path("inventory/devices.yaml"),
        help="Path to the YAML inventory (default: inventory/devices.yaml)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    devices, commands = load_inventory(args.inventory)
    username, password = credentials()
    collect_commands(devices, commands, username, password)


if __name__ == "__main__":
    main()
