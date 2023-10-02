"""Interact with Azure Virtual Machine services."""
from module_virtual_machine.infra.azure_cloud_services import AzureVirtualMachineServices
from module_virtual_machine.utils.type_validation import TypeValidation
from module_virtual_machine.utils.exception import Error

class VirtualMachineServices:
    """Class to interact with Azure Virtual Machine services."""

    def __init__(self):
        self.__az_resource_services = AzureVirtualMachineServices()
        self.__error = Error()
        self.__type_validation = TypeValidation()

    def list_vm_by_subscription_id(self, sub_id:str):
        """Lists all virtual machines of a specific subscription.

         Args:
             sub_id (str): The subscription ID.

         returns:
             list: A list of VirtualMachine objects representing the virtual machines found.

         """
        self.__type_validation.validate_string_param(sub_id, "sub_id")

        try:
            return self.__az_resource_services.list_vm_by_subscription_id(sub_id)

        except Exception as exception:
            self.__error.exception_error('list_vm_by_subscription_id', exception)

    def list_vm_by_resource_group(self, sub_id:str, rg_name:str):
        """Lists all virtual machines of a specific resource group.

         Args:
             sub_id (str): The subscription ID.
             rg_name (str): The name of the resource group.

         returns:
             list: A list of VirtualMachine objects representing the virtual machines found.

         """

        self.__type_validation.validate_string_param(sub_id, "sub_id")
        self.__type_validation.validate_string_param(rg_name, "rg_name")

        try:
            return self.__az_resource_services.list_vm_by_resource_group(sub_id, rg_name)
        except Exception as exception:
            self.__error.exception_error('list_vm_by_resource_group', exception)

    def get_virtual_machine(self, sub_id:str, rg_name:str, vm_name:str):
        """Get information about a specific virtual machine.

         Args:
             sub_id (str): The subscription ID.
             rg_name (str): The name of the resource group.
             vm_name(str): The name of the virtual machine.

         returns:
             VirtualMachine: A VirtualMachine object representing the virtual machine found.

         """

        self.__type_validation.validate_string_param(sub_id, "sub_id")
        self.__type_validation.validate_string_param(rg_name, "rg_name")
        self.__type_validation.validate_string_param(vm_name, "vm_name")

        try:
            return self.__az_resource_services.get_virtual_machine(sub_id, rg_name, vm_name)
        except Exception as exception:
            self.__error.exception_error('get_virtual_machine', exception)
