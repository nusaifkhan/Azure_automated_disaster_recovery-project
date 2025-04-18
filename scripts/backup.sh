#!/bin/bash

# Variables
RESOURCE_GROUP="myResourceGroup"
VM_NAME="myVM"
SNAPSHOT_NAME="mySnapshot"
LOCATION="eastus"

# Create a snapshot
az snapshot create \
    --resource-group $RESOURCE_GROUP \
    --name $SNAPSHOT_NAME \
    --source "/subscriptions/<subscription_id>/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Compute/virtualMachines/$VM_NAME" \
    --location $LOCATION

echo "Snapshot $SNAPSHOT_NAME created successfully."
