#!/bin/bash

# Variables
RESOURCE_GROUP="myResourceGroup"
TEST_VM_NAME="testVM"

# Deallocate the test VM to simulate a failure
echo "Simulating failure: Deallocating VM $TEST_VM_NAME..."
az vm deallocate --resource-group $RESOURCE_GROUP --name $TEST_VM_NAME

# Trigger the recovery process
echo "Initiating recovery process..."
bash scripts/recover_vm.sh  # Call the restoration script

echo "Disaster recovery test completed successfully!"
