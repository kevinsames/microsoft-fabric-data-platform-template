# Contributing Guidelines

Welcome! 👋 Thanks for your interest in contributing to this project.

This repository provides a production-grade, enterprise-ready template for analytics projects using several databases as the core compute engine. It is designed for CPM -and BI-Consultants, and adheres to software engineering best practices (modularity, CI/CD, versioning, testing) with full documentation using the arc42 architecture framework.

---

## 🧰 Prerequisites

- Python 3.8+ and `pip`
- Access to SQL Server
- `pre-commit` installed
- Fork this repository and create your own working branch

---

## 🛠️ Development Workflow

1. **Clone & Setup**

   ```bash
   #Clone the repository
   git fork kevinsames/microsoft-fabric-data-platform-template
   cd microsoft-fabric-data-platform-template
   python -m venv .env
   source .env/bin/activate
   pip install -r requirements.txt
   ```

2. **Pre-commit Hooks**

   Install and run `pre-commit`:

   ```bash
   pip install pre-commit
   pre-commit install
   pre-commit run --all-files
   ```

3. **Write Your Code**

   - Place reusable logic in `src/`
   - Write unit tests in `tests/`
   - Document any architectural decisions or changes in `docs`

4. **Test**

   ```bash
   pytest
   ```

5. **Create a Pull Request**

   - Write a clear title and description
   - Link related issues or enhancements
   - Ensure no secretes are stored in the code
   - Ensure CI checks pass

---

## 🔍 Code Standards

- Use [Black](https://github.com/psf/black) and [Flake8](https://flake8.pycqa.org/)
- Organize notebooks with markdown headers and explanatory comments
- Modularize code for reuse in production

---

## 🧪 Adding New Tests

Tests live under the `tests/` directory. Each module in `src/` should be covered.

We use:
- `pytest` for unit testing

---

## 🧾 License

By contributing, you agree that your contributions will be licensed #TODO.

---

Thanks again for helping improve our drjve+! 🙏
