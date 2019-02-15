#!/bin/sh
 
# CHANGE THESE
resourceGroup="temp.resourcegroup"
region="westeurope"
subscriptionId="<subscription-id>"
 
echo "*** STEP 1: Building docker images... ***"
docker-compose build
 
echo "*** STEP 2: Checking Azure CLI version... ***"
az --version
 
az login

echo "*** STEP 3: Creating resource group $resourceGroup... "
az group create --name $resourceGroup \
                --location $region \
                --subscription $subscriptionId \
                --verbose
 
echo "*** STEP 4: Creating cluster nodes..."
az aks create --resource-group $resourceGroup \
              --name aks-cluster \
              --location $region \
              --node-count 3 \
              --node-vm-size Standard_DS2_v2 \
              --subscription $subscriptionId \
              --generate-ssh-keys \
              --verbose

# TODO: tag image
# TODO: deploy image to ACR
# TODO: create instances of docker containers