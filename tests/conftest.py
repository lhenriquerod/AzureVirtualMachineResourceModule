"""Create mocks and fixtures for tests"""
from unittest.mock import MagicMock
from pytest import fixture
import module_virtual_machine.infra.azure_cloud_services as mock_azure_services
from module_virtual_machine.entities.virtual_machine_model import VirtualMachine


@fixture(autouse=True)
def mock_env_var(monkeypatch):
    """
    Fixture that sets environment variables for Azure authentication to be used in tests.

    Args:
        monkeypatch: pytest fixture that provides a way to temporarily replace or modify
                     attributes, functions or classes.
    """
    monkeypatch.setenv("AZURE_TENANT_ID", "tenant")
    monkeypatch.setenv("AZURE_CLIENT_ID", "client")
    monkeypatch.setenv("AZURE_CLIENT_SECRET", "secret")


@fixture
def mock_virtual_machines(monkeypatch):
    """Fixture to simulate virtual machine objects.

     This fixture creates a fake compute management client object
     and simulates listing and getting virtual machines.
    """

    def mock_vm(*args):
        mock_compute_management_client = MagicMock()
        mock_compute_client_virtual_machines = MagicMock()
        mock_compute_management_client.virtual_machines = mock_compute_client_virtual_machines

        virtual_machines = MagicMock()
        virtual_machines.id = '/subscriptions/615e7ca6-1c2c-49d4-b202-c61c03e7eb47/resourceGroups/RG-GDMS-QA/providers/Microsoft.Compute/virtualMachines/BRAZU1TESTA'
        virtual_machines.vm_id = 'e380aa76-097f-4767-8134-b9fe64651cd3'
        virtual_machines.location = 'brazilsouth'
        virtual_machines.tags = {'Backup': 'VMStdProd',
                         'Billing DXC': 'TRUE',
                         'Billing Entity': 'VALE S.A.',
                         'Budget Clearance': '700',
                         'Cost Center': '1011391',
                         'Created By': 'm.schwendler@dxc.com',
                         'DBA Support Team': 'N/A',
                         'Description': 'GDMS Geotechnical Research',
                         'KPE': 'FALSE',
                         'Responsible - App': 'priscilla.otoni@vale.com',
                         'Responsible - Infra': 'alessandro.frizzera@vale.com',
                         'Support': 'cloudopslatam@dxc.com',
                         'Workload Type': 'QA'}

        vm = MagicMock()
        vm.instance_view = MagicMock()
        vm.instance_view.statuses = [MagicMock(), MagicMock()]
        vm.instance_view.statuses[1].display_status = 'VM running'
        vm.instance_view.os_name = 'Windows Server 2022 Datacenter'
        vm.instance_view.os_version = '10.0.20348.1668'
        vm.id = '/subscriptions/615e7ca6-1c2c-49d4-b202-c61c03e7eb47/resourceGroups/RG-GDMS-QA/providers/Microsoft.Compute/virtualMachines/BRAZU1TESTA'
        vm.vm_id = 'e380aa76-097f-4767-8134-b9fe64651cd3'
        vm.location = 'brazilsouth'
        vm.tags = virtual_machines.tags

        def mock_list_all(*args, **Kwargs):
            return [virtual_machines]

        def mock_get(*args, **Kwargs):
            return vm

        mock_compute_client_virtual_machines.list_all = mock_list_all
        mock_compute_client_virtual_machines.list = mock_list_all
        mock_compute_client_virtual_machines.get = mock_get

        return mock_compute_management_client

    monkeypatch.setattr(mock_azure_services, "ComputeManagementClient", mock_vm)

@fixture
def mock_vm_list_return():
    """Mock of return of list of virtual machines"""
    return [VirtualMachine(rg_name='RG-GDMS-QA', vm_name='BRAZU1TESTA', resource_id='/subscriptions/615e7ca6-1c2c-49d4-b202-c61c03e7eb47/resourceGroups/RG-GDMS-QA/providers/Microsoft.Compute/virtualMachines/BRAZU1TESTA', vm_id='e380aa76-097f-4767-8134-b9fe64651cd3', location='brazilsouth', vm_tags={'Backup': 'VMStdProd', 'Billing DXC': 'TRUE', 'Billing Entity': 'VALE S.A.', 'Budget Clearance': '700', 'Cost Center': '1011391', 'Created By': 'm.schwendler@dxc.com', 'DBA Support Team': 'N/A', 'Description': 'GDMS Geotechnical Research', 'KPE': 'FALSE', 'Responsible - App': 'priscilla.otoni@vale.com', 'Responsible - Infra': 'alessandro.frizzera@vale.com', 'Support': 'cloudopslatam@dxc.com', 'Workload Type': 'QA'}, vm_status='VM running', os_name='Windows Server 2022 Datacenter', os_version='10.0.20348.1668')]

@fixture
def mock_vm_return():
    """Mock of return of virtual machines"""
    return VirtualMachine(rg_name='RG-GDMS-QA', vm_name='BRAZU1TESTA', resource_id='/subscriptions/615e7ca6-1c2c-49d4-b202-c61c03e7eb47/resourceGroups/RG-GDMS-QA/providers/Microsoft.Compute/virtualMachines/BRAZU1TESTA', vm_id='e380aa76-097f-4767-8134-b9fe64651cd3', location='brazilsouth', vm_tags={'Backup': 'VMStdProd', 'Billing DXC': 'TRUE', 'Billing Entity': 'VALE S.A.', 'Budget Clearance': '700', 'Cost Center': '1011391', 'Created By': 'm.schwendler@dxc.com', 'DBA Support Team': 'N/A', 'Description': 'GDMS Geotechnical Research', 'KPE': 'FALSE', 'Responsible - App': 'priscilla.otoni@vale.com', 'Responsible - Infra': 'alessandro.frizzera@vale.com', 'Support': 'cloudopslatam@dxc.com', 'Workload Type': 'QA'}, vm_status='VM running', os_name='Windows Server 2022 Datacenter', os_version='10.0.20348.1668')
