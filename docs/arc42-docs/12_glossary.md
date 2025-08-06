# 12. Glossary

**ADLS Gen2 (Azure Data Lake Storage Gen2):**  
An Azure cloud storage service optimized for big data workloads. Provides hierarchical file system capabilities on top of Azure Blob Storage. Used in this project to store large datasets, intermediate results, and outputs. Gen2 allows Hadoop-compatible access (`abfss://` paths) and is typically the backing store for Databricks data (e.g., Delta Lake tables).

**arc42:**  
A template and methodology for software architecture documentation, divided into sections covering different aspects of the design (as used in this document for consistency and completeness).

**Asset Bundle (Databricks Asset Bundle):**  
A declarative packaging of Databricks project assets (notebooks, files, configurations) and resource definitions (jobs, pipelines, etc.) into a single deployable unit. Asset Bundles use YAML config and the Databricks CLI to enable CI/CD for Databricks projects, treating them as Infrastructure-as-Code. In practice, it’s a way to represent what’s in a Databricks workspace in source-controlled files, which can be validated and deployed as a bundle.

**CI/CD (Continuous Integration / Continuous Deployment):**  
Practices to frequently integrate code changes (CI) and deploy them to environments (CD) through automation. In our context, CI refers to automated testing/validation on each commit, and CD refers to automated deployment to Databricks and Azure when changes are merged, using GitHub Actions workflows.

**Databricks:**  
An analytics platform based on Apache Spark, optimized on Azure as a first-party service. It provides interactive notebooks, job scheduling, and a managed Spark compute engine. Often used to implement data pipelines, ETL, and machine learning at scale. Azure Databricks integrates with Azure services like ADLS and Azure Machine Learning. In this project, Azure Databricks is the core compute where all processing and model training occurs.

**DBFS (Databricks File System):**  
A distributed file system mounted to Databricks workspaces. Backed by Azure Blob storage, it provides a default storage location (`dbfs:/`) accessible in Databricks. Often used for storing small files, libraries, or results. For large data, direct ADLS access (`abfss`) is preferred. In the template, DBFS might be used to store uploaded libraries or temporary data, but primary datasets reside in ADLS.

**Delta Lake:**  
An open-source storage layer on top of data lakes that supports ACID transactions, time-travel (versioned data), and schema enforcement. On Databricks, Delta is a default format for many operations (especially in Spark 3+). We use Delta for reliable data pipelines (e.g., writing feature tables or intermediate results) to ensure data quality and easy rollbacks if needed.

**GitHub Actions:**  
GitHub’s CI/CD service for automating software workflows directly from a GitHub repository. Workflows are defined as YAML files and run on virtual runners. In this project, Actions run tests and deploy code/infrastructure to Azure.

**Great Expectations (GX):**  
An open-source data validation framework. It allows you to define “expectations” about your data (schemas, distributions, etc.) and test if data meets them. While not built-in, the template mentions it as an option for enforcing data contracts and quality checks in pipelines.

**MLOps:**  
A set of practices to streamline the process of taking machine learning models from development to production reliably and efficiently. It extends DevOps to include ML-specific concerns (data management, experiment tracking, etc.). This template aims to implement MLOps level 4 maturity practices, meaning full automation and continuous delivery of ML pipelines, with governance.

**MLflow:**  
An open-source framework for tracking machine learning experiments, packaging ML models, and managing model lifecycle (registry). Databricks provides a managed MLflow service built into its workspace.  
- **MLflow Tracking:** Logging of metrics, parameters, artifacts for each experiment run.  
- **MLflow Model Registry:** A centralized store for model versions, allowing staging/prod transitions and annotations.  
In this template, MLflow is used to track model training runs and register models for later deployment or analysis.

**NYC Taxi Dataset:**  
A popular public dataset containing taxi ride records in New York City (fares, pickup/dropoff locations, timestamps, etc.). Often used in data science demos. The template references this as an example dataset for demonstrating pipeline functionality (e.g., predicting taxi fare or trip duration). Databricks provides it in `dbfs:/databricks-datasets/` for convenience.

**PySpark:**  
The Python API for Apache Spark. Allows writing Spark code using Python syntax, which runs on the Spark cluster parallelizing operations on large datasets. PySpark is used for data transformations in this project to leverage distributed computation for big data.

**Terraform:**  
An Infrastructure-as-Code (IaC) tool by HashiCorp, used to provision and manage cloud resources declaratively. Terraform uses providers (like the AzureRM provider for Azure resources, and the Databricks provider for Databricks workspace objects) to apply desired states. We use Terraform to set up Azure Databricks workspace, storage, and related infrastructure, enabling reproducible and version-controlled environment setup.

**Unity Catalog:**  
A unified governance solution for data and AI assets in Databricks. It provides centralized metadata and fine-grained access control across Databricks workspaces.  
- **Metastore:** Top-level container for all catalogs and assets.  
- **Catalog:** A collection of schemas (often mapping to organizational domains).  
- **Schema:** A collection of tables and views (and now also ML models) under a catalog.  
Unity Catalog also tracks data lineage and usage. In this template, integration with Unity Catalog is optional, but recommended for enterprises to manage data access and catalog datasets/models for discovery and reuse.

**Workspace APIs:**  
Refers to Databricks REST APIs that allow programmatic control of the workspace, such as the Workspace API for notebook import/export, Jobs API for job management, Clusters API, etc. The template uses these under the hood via tools (e.g., the Databricks CLI and Asset Bundles use Workspace and Jobs APIs). “Integration with workspace APIs” means you can also directly use these APIs for advanced control – for instance, a Python script in `/src` could call the Jobs API to create a job dynamically, or use the Files API to put data in DBFS. While Asset Bundles cover most needs declaratively, we acknowledge that understanding and possibly using the raw Workspace APIs can be part of advanced use.

**Data Contract:**  
A formal specification of the schema, types, and expectations of data exchanged between systems (producers and consumers). In the context of this template, data contracts ensure that upstream data sources provide data in a format the downstream pipeline expects. If a contract is broken (e.g., a column is missing or a value is of wrong type), the pipeline should detect it (through validations) and raise an error rather than producing potentially incorrect results. Data contracts promote reliability in data pipelines and are a cornerstone of data quality in collaborative environments.