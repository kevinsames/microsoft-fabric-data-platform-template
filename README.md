# Microsoft Fabric Data Platform Template

A production-ready template for analytics projects on [Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/). This repository provides modular organization, CI/CD automation, and arc42-based documentation to accelerate data engineering, BI, and ML workflows.

---

## 📁 Project Structure

```
.github/                 # CI/CD workflows, issue & PR templates
docs/                    # Architecture docs (arc42), dbt docs
fabric/                  # Lakehouse and notebook assets
macros/                  # dbt macros
models/                  # dbt models (staging, intermediate, marts)
seeds/                   # dbt seed data
snapshots/               # dbt snapshots
tests/                   # Unit and integration tests
requirements.txt         # Python dependencies
dbt_project.yml          # dbt project config
.pre-commit-config.yaml  # Pre-commit hooks config
profiles.yml.example     # dbt profile example
```

---

## 🚀 Quickstart

### Prerequisites

- Microsoft Fabric workspace
- Python 3.8+
- dbt-core, dbt-fabric
- pre-commit, pytest

### Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/your-org/microsoft-fabric-data-platform-template.git
    cd microsoft-fabric-data-platform-template
    ```

2. **Install dependencies**
    ```bash
    python -m venv .env
    source .env/bin/activate
    pip install -r requirements.txt
    ```

3. **Configure dbt profile**
    - Copy `profiles.yml.example` to your dbt profile location and update credentials.

4. **Run pre-commit checks**
    ```bash
    pre-commit install
    pre-commit run --all-files
    ```

5. **Run tests**
    ```bash
    pytest
    ```

---

## 🧰 Usage

- **Notebooks**: Use notebooks in [`fabric/nb-dp-bronze-aw.Notebook/notebook-content.py`](fabric/nb-dp-bronze-aw.Notebook/notebook-content.py) for data ingestion and transformation.
- **Lakehouse**: Lakehouse metadata and shortcuts in [`fabric/lh_dp.Lakehouse/`](fabric/lh_dp.Lakehouse/).
- **dbt Models**: Organize models in `models/staging`, `models/intermediate`, and `models/marts`.
- **CI/CD**: Automated checks via GitHub Actions ([`.github/workflows/ci.yml`](.github/workflows/ci.yml)).

---

## 📖 Documentation

- Architecture docs: [`docs/arc42-docs/`](docs/arc42-docs/)
- dbt docs: [`docs/dbt-docs/`](docs/dbt-docs/)
- Contribution guidelines: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Code of conduct: [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)
- Security policy: [`SECURITY.md`](SECURITY.md)

---

## 🤝 Contributing

We welcome contributions!  
See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines.

---

## 📄 License

MIT License – see [LICENSE](LICENSE).

---

## 🌟 References

- [Microsoft Fabric Documentation](https://learn.microsoft.com/en-us/fabric/)
- [dbt-fabric Adapter](https://github.com/dbt-msft/dbt-fabric)