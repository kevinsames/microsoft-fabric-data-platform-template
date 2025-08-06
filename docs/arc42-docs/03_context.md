# 03. System Scope and Context

In the context of a enterprise data platform, this repository sits at the intersection of development workflows and cloud infrastructure.

Data scientists/engineers develop a project “bundle” in a local or Databricks Repo environment, commit to version control (GitHub), and CI/CD pipelines promote and deploy the bundle to Azure Databricks workspaces for dev and production environments.

In this architecture, users interact with Databricks notebooks and code in a development workspace (or locally with Databricks Connect/CLI), then push changes to the GitHub repository. External systems and actors include:

- **GitHub (Source Control):** Hosts the code, notebooks, and config. It triggers CI/CD workflows on code changes.
- **GitHub Actions (CI/CD runners):** An external service that runs linting, tests, and deployment jobs on our behalf. It has access (via secrets) to Azure to provision infra and to Databricks to deploy artifacts.
- **Azure Databricks Workspaces:** The target environment(s) where the ML workflows run. In an enterprise, there could be separate workspaces for Development, Staging, and Production (each a managed Databricks environment in Azure).
- **Azure Data Lake Storage (ADLS Gen2):** An external data repository for large datasets. The ML notebooks read/write data from ADLS (e.g., reading raw training data, writing prepared data or model outputs). ADLS may also hold shared assets like feature store data or results.
- **Azure Active Directory (Identities):** Provides service principals and identities used by Databricks and CI/CD to authenticate. For example, a service principal is used by Terraform to create resources, and another might be used by Databricks clusters to access ADLS.
- **MLflow Tracking Server:** In Azure Databricks this is a hosted service (part of the workspace) that tracks experiments. It is not a separate external system we deploy, but it’s an important part of the context as it stores model artifacts and metrics. Downstream, model consumers or deployment targets (like a serving endpoint or Azure ML for deployment) could be considered, but in scope we focus on the Databricks/MLflow integration.

## Scope of the repo

This repo covers the end-to-end lifecycle from development to deployment of data and ML pipelines within Azure Databricks:

- It covers development artifacts: reusable Python modules, Spark jobs, notebooks for ETL or model training, and unit/integration tests.
- It implements CI/CD pipelines to validate code and automatically deploy notebooks and job configurations to Databricks.
- Model tracking (via MLflow) and job orchestration on Databricks are part of the scope, demonstrated with example notebooks and job definitions (e.g., a training job that triggers an evaluation job).
- The repo also provides comprehensive documentation (arc42 architecture docs, README, etc.) to help new projects understand and adapt the structure.

## Out of Scope

The repo does not directly cover data ingestion from external sources into ADLS (it assumes data is available in the data lake or provided sample data). It also doesn’t include real-time streaming pipelines or deep integration with other Azure services like Azure ML or Data Factory – though those could be added if needed. Deployment of models to production serving (e.g., via Azure ML or Databricks Model Serving) is considered optional and exemplified but not fully automated by default. The focus remains on batch or scheduled ML workflows (e.g., training and batch scoring jobs) rather than live API serving (though the structure could be extended for that).

Everything in this repo is meant to run within the Azure Databricks environment and its surrounding Azure resources – it is not intended for on-prem or other cloud providers.

TODO