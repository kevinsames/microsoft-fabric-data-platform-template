# 02. Architecture Constraints

The design is constrained by several technology and policy choices:

- **Azure Cloud & Services:**  
  The solution is built specifically for Azure. It assumes use of Azure Databricks as the compute engine and Azure Data Lake Storage Gen2 for storage. Alternative clouds or services are out of scope. For example, model training and data processing must occur on Azure Databricks clusters (not on local machines or other platforms).

- **Infrastructure as Code (Terraform):**  
  All cloud infrastructure must be provisioned via Terraform scripts (no manual creation through Azure Portal). This includes the Azure Databricks workspace, storage accounts, identity roles, etc. Terraform ensures environment consistency and enables automation via CI/CD. The Terraform code uses the Azure RM provider and Databricks provider as needed, and must adhere to enterprise standards for environment configuration (e.g., remote state storage, approved modules).

- **CI/CD with GitHub Actions:**  
  Continuous integration and deployment pipelines are implemented with GitHub Actions (not other CI tools like Azure DevOps, Jenkins, etc.). The repository includes YAML workflow files under `.github/workflows` (surfaced in `/pipelines` directory for clarity) to enforce code quality and automate deployment steps. Organisational policy mandates code review via pull requests and automated checks, which is implemented via these GitHub Actions.

- **Technology Stack Constraints:**  
  Python is the primary programming language (for notebooks, `.py` modules, tests). PySpark (Spark with Python) is used for distributed data processing, along with common ML libraries (pandas for data manipulation, scikit-learn for sample modeling, etc.). The project must support MLflow integration for tracking. Only open-source or enterprise-approved libraries should be used (managed via `requirements.txt`). Enterprise Python coding standards (PEP8, etc.) should be followed, enforced by linting tools.

- **Databricks Asset Bundles:**  
  Deployment of notebooks and job configurations must use Databricks Asset Bundles, following Databricks’ best practice to treat environment and job config as code. This is a constraint to avoid ad-hoc manual notebook imports or UI-based job setups; instead, all such assets are specified in bundle YAML files and deployed through CLI, ensuring consistency.

- **Environment Separation:**  
  Typically, enterprises require separate Dev, Staging, and Prod environments. This template assumes multiple Databricks workspaces (or at least logical environment separation) and provides configuration to deploy to each. For instance, Terraform and bundle config can be parameterized by environment (with separate state or config files). Promotion from dev to prod is done by merging code and possibly creating a release branch, rather than manual rework.

- **Security and Compliance:**  
  All secrets (cloud credentials, service principal keys, etc.) must be stored securely (e.g., in GitHub Actions secrets, or Azure Key Vault if integrated) and never committed to the repo. The Terraform code is expected to set up service principals/managed identities for Databricks to access ADLS securely (so no hard-coded storage keys in notebooks). The design should comply with data security standards – for example, enabling encryption on storage, principle of least privilege on identities, and optionally using Unity Catalog for fine-grained data access control.

- **Reusability as Template:**  
  Since this is a template repository, it should remain generic (no hard-coded environment names or personal info) and use placeholders or minimal dummy data so that new projects can adapt it easily. License (e.g., Apache-2.0) and contribution guidelines are included to clarify usage rights and how teams can contribute improvements.