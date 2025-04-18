from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

credential = DefaultAzureCredential()
subscription_id = "your_subscription_id"

compute_client = ComputeManagementClient(credential, subscription_id)

def create_snapshot(resource_group, vm_name, snapshot_name):
    snapshot_config = {
        "location": "eastus",
        "creation_data": {
            "create_option": "Copy",
            "source_resource_id": f"/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Compute/virtualMachines/{vm_name}"
        }
    }
    snapshot = compute_client.snapshots.begin_create_or_update(
        resource_group_name=resource_group,
        snapshot_name=snapshot_name,
        parameters=snapshot_config
    ).result()
    print(f"Snapshot {snapshot_name} created successfully.")

create_snapshot("myResourceGroup", "myVM", "mySnapshot")
