"""Module responsible for testing the Virtual Machines Module."""
from module_virtual_machine.infra.azure_cloud_services import AzureVirtualMachineServices

def test_list_vm_by_subscription_id(mock_virtual_machines, mock_vm_list_return):
    """Tests the list_vm_by_subscription_id method of the AzureVirtualMachineServices class.

     Verifies that the list of virtual machines returned by the list_vm_by_subscription_id method
     matches the expected result.

     Args:
         mock_virtual_machines: Fixture that simulates virtual machine objects.

     """
    az_services = AzureVirtualMachineServices()

    expected = az_services.list_vm_by_subscription_id('615e7ca6-1c2c-49d4-b202-c61c03e7eb47')

    assert expected == mock_vm_list_return

def test_list_vm_by_resource_group(mock_virtual_machines, mock_vm_list_return):
    """Tests the list_vm_by_resource_group method of the AzureVirtualMachineServices class.

     Verifies that the list of virtual machines returned by the list_vm_by_resource_group method
     matches the expected result.

     Args:
         mock_virtual_machines: Fixture that simulates virtual machine objects.

     """
    az_services = AzureVirtualMachineServices()

    expected = az_services.list_vm_by_resource_group('13546548445', 'RG-GDMS-QA')

    assert expected == mock_vm_list_return

def test_get_virtual_machine(mock_virtual_machines, mock_vm_return):
    """Test the get_virtual_machine method of the AzureVirtualMachineServices class.

     Checks whether the virtual machine returned by the get_virtual_machine method
     matches the expected result.

     Args:
         mock_virtual_machines: Fixture that simulates virtual machine objects.

     """
    az_services = AzureVirtualMachineServices()

    expected = az_services.get_virtual_machine('12146546456', 'RG-GDMS-QA', 'BRAZU1TESTA')

    assert expected == mock_vm_return
