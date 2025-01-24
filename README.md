# MyAzureAIProject

This project contains an AI agent that integrates within Azure cloud to optimize resources and orchestrate workloads.

## Setup

1. Create a resource group and VM:
    ```sh
    az group create --name MyResourceGroup --location eastus
    az vm create --resource-group MyResourceGroup --name MyVM --image UbuntuLTS --admin-username azureuser --generate-ssh-keys
    ```

2. Install Azure SDK on the VM:
    ```sh
    ssh azureuser@<VM_PUBLIC_IP>
    sudo apt update
    sudo apt install python3-pip
    pip3 install azure-mgmt-compute azure-mgmt-monitor azure-identity
    ```

3. Clone this repository and navigate to the project directory:
    ```sh
    git clone <repository_url>
    cd MyAzureAIProject
    ```

4. Update environment variables and run the optimization script:
    ```sh
    export AZURE_SUBSCRIPTION_ID=<Your_Azure_Subscription_ID>
    python3 optimize_resources.py
    ```

5. Create and deploy the Azure Function:
    ```sh
    cd MyFunctionApp
    func init MyFunctionApp --python
    func new --name OptimizeResourcesFunction --template "Timer trigger"
    func azure functionapp publish <Your_Function_App_Name>
    ```
