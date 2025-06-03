# Microsoft Fabric Data Platform Template (Hybrid Model)

This repository provides a starter template for building a **modern Data Platform on Microsoft Fabric**, combining **Spark notebooks** and **dbt** for data transformations across the medallion architecture:

- **Bronze Layer**: Raw data ingested via **Spark notebooks** into a Fabric Lakehouse
- **Silver Layer**: Cleaned and enriched using **Spark notebooks**
- **Gold Layer**: Curated business logic modeled via **dbt** and stored in a Fabric Warehouse

## 🚀 Features

- ✅ Hybrid medallion architecture: Spark (Bronze/Silver) + dbt (Gold)
- ✅ CI/CD with GitHub Actions (Spark + dbt)
- ✅ Environment separation (dev/test/prod)
- ✅ arc42-based architecture documentation
- ✅ Modular repo for ingestion, transformation, deployment, and documentation

## 📂 Folder Structure

```
.github/workflows/         # CI/CD automation
environments/              # Dev/Test/Prod configs
infrastructure/            # IaC templates
ingestion/notebooks/       # Spark notebooks (Bronze → Silver)
dbt/                       # dbt project (Silver → Gold)
docs/                      # arc42 docs
notebooks/                 # Optional orchestration
```

## 🛠️ Tools Used

| Layer    | Engine  | Tool            | Storage             |
|----------|---------|------------------|----------------------|
| Bronze   | Spark   | Fabric Notebook   | Fabric Lakehouse     |
| Silver   | Spark   | Fabric Notebook   | Fabric Lakehouse     |
| Gold     | SQL     | dbt Core          | Fabric Warehouse     |

## ⚙️ CI/CD

- GitHub Actions run dbt builds and tests on PR
- Optional: validate Spark notebooks using pipeline triggers or notebook tests
- Promote changes to higher envs (prod) on merge to `main`

## 🧪 Getting Started

1. Clone this repo
2. Deploy Fabric resources using `/infrastructure`
3. Load sample data via `ingestion/notebooks/01_load_raw_data.ipynb`
4. Run the `02_transform_bronze_to_silver.ipynb` to generate Silver data
5. Build and test dbt models from Silver to Gold
6. Use GitHub Actions to automate deployment and tests

---

MIT License. Contributions welcome!
