# optimize_resources.py
import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.monitor import MonitorManagementClient

# Authentication
credential = DefaultAzureCredential()
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

compute_client = ComputeManagementClient(credential, subscription_id)
monitor_client = MonitorManagementClient(credential, subscription_id)

# Function to optimize VM resources
def optimize_vm_resources(resource_group, vm_name):
    # Get VM details
    vm = compute_client.virtual_machines.get(resource_group, vm_name)
    
    # Monitor CPU and Memory usage
    metrics_data = monitor_client.metrics.list(
        resource_id=vm.id,
        timespan="PT1H",
        interval="PT1M",
        metricnames="Percentage CPU,Available Memory Bytes",
        aggregation="Average"
    )
    
    cpu_usage = None
    memory_available = None
    for item in metrics_data.value:
        if item.name.value == "Percentage CPU":
            cpu_usage = item.timeseries[0].data[-1].average
        elif item.name.value == "Available Memory Bytes":
            memory_available = item.timeseries[0].data[-1].average

    # Optimize resources based on metrics
    if cpu_usage and cpu_usage > 80:
        new_vm_size = "Standard_D4_v3"
        vm.hardware_profile.vm_size = new_vm_size
        compute_client.virtual_machines.create_or_update(resource_group, vm_name, vm)
        print(f"Scaled up VM {vm_name} to {new_vm_size}")
        
    if memory_available and memory_available < 1e9:
        new_vm_size = "Standard_D4_v3"
        vm.hardware_profile.vm_size = new_vm_size
        compute_client.virtual_machines.create_or_update(resource_group, vm_name, vm)
        print(f"Scaled up VM {vm_name} to {new_vm_size}")

# Example usage
if __name__ == "__main__":
    resource_group = "MyResourceGroup"
    vm_name = "MyVM"
    optimize_vm_resources(resource_group, vm_name)
