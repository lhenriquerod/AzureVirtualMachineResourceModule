"""Model for the attributes of a virtual machine."""
from dataclasses import dataclass

@dataclass
class VirtualMachine:
    """Template for creating an object to return"""
    rg_name: str
    vm_name: str
    resource_id: str
    vm_id: str
    location: str
    vm_tags: dict
    vm_status: str
    os_name: str
    os_version: str
