# Microsoft Fabric Data Platform Template

This repository provides a production-ready template for building a modern Data Platform on **Microsoft Fabric**, following the **medallion architecture**:

- **Bronze Layer**: Raw data stored in a Fabric **Lakehouse**
- **Silver Layer**: Cleaned/transformed data via **dbt**, stored in Lakehouse
- **Gold Layer**: Curated business-ready data in a **Fabric Warehouse**

## 🚀 Features

- ✅ Medallion architecture using Lakehouses and Warehouses
- ✅ **dbt Core** for SQL-based transformations (Silver & Gold)
- ✅ **GitHub Actions** for CI/CD (build, test, deploy)
- ✅ Environment separation (**dev / test / prod**)
- ✅ IaC setup templates for Fabric (Lakehouses, Warehouses, Workspaces)
- ✅ Example ingestion notebooks for the Bronze layer
- ✅ arc42-based documentation structure for architectural clarity

## 📂 Repository Structure

```
.github/workflows/         # CI/CD workflows
environments/              # Dev, Test, Prod configurations
infrastructure/            # Terraform/Bicep scripts for Fabric setup
ingestion/                 # Sample notebooks or pipelines for Bronze ingestion
dbt/                       # dbt project: models, profiles, tests, macros
docs/                      # arc42 architecture documentation
notebooks/                 # Optional orchestration notebooks
```

## 🛠️ Technology Stack

- **Microsoft Fabric**: Lakehouse, Warehouse, Pipelines, Notebooks
- **dbt Core**: SQL-based transformations (via [dbt-fabric adapter](https://github.com/microsoft/dbt-fabric))
- **GitHub Actions**: CI/CD automation
- **arc42**: Architecture documentation standard

## 🚦 Getting Started

1. Clone this repository.
2. Set up Fabric workspaces using `/infrastructure`.
3. Configure environment files in `/environments`.
4. Use `/ingestion` to load sample data into the Bronze layer.
5. Run dbt models using GitHub Actions or `/notebooks/run_dbt_model.ipynb`.
6. Document your solution in `/docs` using the arc42 template.

---

MIT License. Contributions welcome!
