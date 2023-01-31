#!/bin/bash

# Login to Azure
az login

# Create a new resource group
az group create --name myResourceGroup --location eastus

# Create a new App Service Plan
az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku B1 --is-linux

# Create a new Web App
az webapp create --name myWebApp --resource-group myResourceGroup --plan myAppServicePlan

# Deploy the Python application code to the Web App
az webapp deployment source config-local-git --name myWebApp --resource-group myResourceGroup

# Clone the Git repository for the Web App
git clone https://<your-git-username>@myWebApp.scm.azurewebsites.net/myWebApp.git

# Navigate to the cloned repository
cd myWebApp

# Copy the Python application code to the repository
cp ../my_python_app/* .

# Commit the changes to the Git repository
git add .
git commit -m "Initial Deployment"

# Push the changes to the Web App
git push origin master

# Open the Web App in a web browser
az webapp browse --name myWebApp --resource-group myResourceGroup
