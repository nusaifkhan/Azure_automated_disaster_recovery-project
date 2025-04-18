#!/bin/bash

# Variables
RESOURCE_GROUP="myResourceGroup"
VM_NAME="myRecoveredVM"
SNAPSHOT_NAME="mySnapshot"
DISK_NAME="myRecoveredDisk"
LOCATION="eastus"

# Create a new managed disk
az disk create \
    --resource-group $RESOURCE_GROUP \
    --name $DISK_NAME \
    --source $SNAPSHOT_NAME \
    --location $LOCATION

# Create a VM from the managed disk
az vm create \
    --resource-group $RESOURCE_GROUP \
    --name $VM_NAME \
    --attach-os-disk $DISK_NAME \
    --os-type Linux

echo "VM $VM_NAME restored from snapshot $SNAPSHOT_NAME."
