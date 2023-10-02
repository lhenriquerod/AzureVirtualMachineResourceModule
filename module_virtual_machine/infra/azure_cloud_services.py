"""Interact with Azure Virtual Machines services."""
from azure.mgmt.compute import ComputeManagementClient
from module_virtual_machine.infra.authenticate import AzureAuthenticate
from module_virtual_machine.entities.virtual_machine_model import VirtualMachine

class AzureVirtualMachineServices:
    """Class to interact with Azure Virtual Machines services."""

    def __init__(self):
        """Initializes the AzureVirtualMachineServices class."""
        self.__az_authenticate = AzureAuthenticate()
        self.__credential = self.__az_authenticate.client_credentials()

    def list_vm_by_subscription_id(self, sub_id: str):
        """Lists all virtual machines of a specific subscription.

         Args:
             sub_id (str): The subscription ID.

         returns:
             list: A list of VirtualMachine objects representing the virtual machines found.

         """
        compute_client = ComputeManagementClient(self.__credential, sub_id)
        virtual_machines = compute_client.virtual_machines.list_all()

        vm_list = []
        for virtual_machine in virtual_machines:
            rg_name = virtual_machine.id.split('/')[4]
            vm_name = virtual_machine.id.split('/')[-1]
            vm_get = self.__get_vm(sub_id, rg_name, vm_name)
            if len(vm_get.instance_view.statuses) == 2:
                os_status = vm_get.instance_view.statuses[1].display_status

            osname = vm_get.instance_view.os_name
            osversion = vm_get.instance_view.os_version

            if virtual_machine.tags is None:
                virtual_machine.tags = {}

            vm_list.append(VirtualMachine(rg_name=rg_name, vm_name=vm_name, resource_id=virtual_machine.id, vm_id=virtual_machine.vm_id,location=virtual_machine.location, vm_tags=virtual_machine.tags, vm_status=os_status, os_name=osname, os_version=osversion))
        return vm_list


    def list_vm_by_resource_group(self, sub_id, rg_name):
        """Lists all virtual machines of a specific resource group.

         Args:
             sub_id (str): The subscription ID.
             rg_name (str): The name of the resource group.

         returns:
             list: A list of VirtualMachine objects representing the virtual machines found.

         """
        compute_client = ComputeManagementClient(self.__credential, sub_id)
        vm_list = []

        virtual_machines = compute_client.virtual_machines.list(rg_name)

        for virtual_machine in virtual_machines:

            vm_name = virtual_machine.id.split('/')[-1]
            vm_get = self.__get_vm(sub_id, rg_name, vm_name)
            if len(vm_get.instance_view.statuses) == 2:
                os_status = vm_get.instance_view.statuses[1].display_status

            osname = vm_get.instance_view.os_name
            osversion = vm_get.instance_view.os_version

            if virtual_machine.tags is None:
                virtual_machine.tags = {}

            vm_list.append(VirtualMachine(rg_name=rg_name, vm_name=vm_name, resource_id=virtual_machine.id, vm_id=virtual_machine.vm_id,location=virtual_machine.location, vm_tags=virtual_machine.tags, vm_status=os_status, os_name=osname, os_version=osversion))
        return vm_list

    def get_virtual_machine(self, sub_id: str, rg_name, vm_name):
        """Get information about a specific virtual machine.

         Args:
             sub_id (str): The subscription ID.
             rg_name (str): The name of the resource group.
             vm_name(str): The name of the virtual machine.

         returns:
             VirtualMachine: A VirtualMachine object representing the virtual machine found.

         """

        virtual_machine = self.__get_vm(sub_id, rg_name, vm_name)

        if len(virtual_machine.instance_view.statuses) == 2:
            os_status = virtual_machine.instance_view.statuses[1].display_status

            osname = virtual_machine.instance_view.os_name
            osversion = virtual_machine.instance_view.os_version

        if virtual_machine.tags is None:
            virtual_machine.tags = {}

        return VirtualMachine(rg_name=rg_name, vm_name=vm_name, resource_id=virtual_machine.id, vm_id=virtual_machine.vm_id,location=virtual_machine.location, vm_tags=virtual_machine.tags, vm_status=os_status, os_name=osname, os_version=osversion)

    def __get_vm(self, sub_id: str, rg_name:str, vm_name:str):
        """"""
        compute_client = ComputeManagementClient(self.__credential, sub_id)

        return compute_client.virtual_machines.get(resource_group_name=rg_name, vm_name=vm_name, expand = 'instanceview')
