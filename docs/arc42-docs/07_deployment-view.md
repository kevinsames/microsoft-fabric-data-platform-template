# 07. Deployment View

This solution is deployed in Azure (West Europe) for both test and production environments, using the following resources:

## Test Environment (`-dev`, `datalounge-test`)

- **Resource Groups:**
  - `rg-dp-common-euw-dev`: Shared resources (Key Vault, Access Connector)
  - `rg-dp-lakehouse-euw-dev`: Lakehouse-specific resources (Databricks, Data Factory, Storage)
- **Compute & Data:**
  - `adb-dp-lakehouse-euw-dev`: Azure Databricks workspace
  - `adls0dp0euw0dev`: Azure Storage Account for data lake
- **Integration & Security:**
  - `acadb-dp-common-euw-dev`: Access Connector for Databricks
  - `kv-dp-common-euw-dev`: Azure Key Vault for secrets
- **Orchestration:**
  - `adf-dp-lakehouse-euw-dev`: Azure Data Factory

## Production Environment (`-prod`, `datalounge-prod`)

- **Resource Groups:**
  - `rg-dp-common-euw-prod`: Shared resources (Key Vault, Access Connector)
  - `rg-dp-lakehouse-euw-prod`: Lakehouse-specific resources (Databricks, Data Factory, Storage)
- **Compute & Data:**
  - `adb-dp-lakehouse-euw-prod`: Azure Databricks workspace
  - `adls0dp0euw0prod`: Azure Storage Account for data lake
- **Integration & Security:**
  - `acadb-dp-common-euw-prod`: Access Connector for Databricks
  - `kv-dp-common-euw-prod`: Azure Key Vault for secrets
- **Orchestration:**
  - `adf-dp-lakehouse-euw-prod`: Azure Data Factory

**Region:** All resources are deployed in West Europe.

**Summary:**  
Databricks provides compute, Storage Account holds data, Data Factory orchestrates pipelines, Key Vault manages secrets, and Access Connector secures Databricks access. Resources are grouped for separation of concerns and managed via Azure Resource Groups for both environments.