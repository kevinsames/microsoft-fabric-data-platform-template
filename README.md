# 🚀 Microsoft Fabric Template Repository

This repository is a comprehensive template for building modern **Data Engineering**, **Machine Learning**, and **AI** projects using **Microsoft Fabric**. It applies best practices in software engineering, CI/CD, and architectural documentation (arc42), and is structured around the **medallion architecture** (Bronze → Silver → Gold).

---

## 📌 Features

- 🪙 **Medallion Architecture**  
  Bronze (raw data) → Silver (refined) → Gold (curated) using Fabric Lakehouses & Warehouses

- 📘 **Spark Notebooks & dbt**  
  Use Spark Notebooks for ingestion & transformation, dbt for analytics engineering in the gold layer

- 🤖 **Machine Learning Ready**  
  ML training pipelines, experiment tracking with MLflow, and batch inference

- 🧠 **AI Service Integration**  
  Prompt orchestration, SynapseML, Azure OpenAI integration

- 📦 **CI/CD with GitHub Actions**  
  Automate dbt runs, notebook orchestration, model training, and AI service deployment

- 🧱 **Software Engineering Principles**  
  Modular folder structure, environment configs (dev/test/prod), and code reuse

- 📄 **arc42 Documentation**  
  Documented architecture for Data Platform, ML systems, AI services, and decision logs

---

## 📁 Folder Structure (Summary)

```
/.github/                 # CI/CD workflows and templates  
/config/                 # Environment-specific configs  
/docs/                   # arc42-based documentation  
/infrastructure/         # IaC (Bicep, Terraform), deployment scripts  
/src/                    # Source code for ingestion, transformation, ML, and AI  
/tests/                  # Unit and integration tests  
/tools/                  # CLI utilities, fabric-cicd helpers  
```

---

## 🛠️ Requirements

- [Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/)
- Python 3.10+
- `dbt-core`, `dbt-fabric`
- `mlflow`, `synapseml`
- `fabric-cicd` (for deployment automation)
- Azure CLI or GitHub Actions for CI/CD

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🧪 Example Workflows

- `GitHub Actions`:  
  - Run Spark notebooks  
  - Deploy dbt models to Fabric Warehouse  
  - Train & evaluate ML models  
  - Deploy AI APIs or prompt flows

- `Notebooks`:  
  - Ingest to Bronze  
  - Transform Bronze → Silver  
  - Prepare Gold layer with dbt

- `ML`:  
  - Train models using Fabric notebooks  
  - Log experiments in MLflow  
  - Register models for batch inference

---

## 🧭 Documentation

This repository includes templates and examples aligned to the [arc42](https://arc42.org/) architecture standard. See:
- `docs/architecture-overview.md`
- `docs/ml-system.md`
- `docs/ai-services.md`
- `docs/arc42-template.md`
- `docs/decisions/` (ADR records)

---

## 🤝 Contributing

Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) and our [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).  
We welcome contributions that improve usability, structure, or add useful examples.

---

## 📢 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 💡 Inspiration & Credits

- [Microsoft Fabric Docs](https://learn.microsoft.com/en-us/fabric/)
- [dbt-fabric Adapter](https://github.com/dbt-msft/dbt-fabric)
- [fabric-cicd](https://github.com/microsoft/fabric-cicd)
- [Fabric Accelerator](https://github.com/bennyaustin/fabric-accelerator)
