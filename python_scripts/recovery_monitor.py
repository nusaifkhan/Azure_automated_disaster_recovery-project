from azure.mgmt.monitor import MonitorManagementClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
subscription_id = "your_subscription_id"

monitor_client = MonitorManagementClient(credential, subscription_id)

def list_alerts(resource_group):
    alerts = monitor_client.activity_logs.list(
        filter=f"resourceGroupName eq '{resource_group}'"
    )
    for alert in alerts:
        print(f"Time: {alert.event_timestamp}, Severity: {alert.severity}, Description: {alert.operation_name}")

list_alerts("myResourceGroup")
