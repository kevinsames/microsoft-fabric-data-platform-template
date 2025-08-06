# 06. Runtime View

This section describes how the system operates at runtime, covering both the execution of BI/ML pipelines on Databricks and the CI/CD automation workflow. One primary runtime scenarios are illustrated: (a) the CI/CD workflow that delivers code to the environment.

## a. CI/CD Pipeline Execution (Automation Workflow)

The CI/CD pipelines automate validation and deployment:

1. **Developer Commit & CI Trigger:**  
   A developer pushes changes. GitHub triggers the CI workflow.

2. **CI (Build & Test) Steps:**  
   - **Linting:** Runs black and flake8 for code style.
   - **Testing:** Runs pytest (including PySpark tests). Optionally, executes notebooks via Papermill or similar.

3. **CI Outcomes:**  
   If all checks pass, the commit/PR is marked green. Failures notify the developer for fixes.

4. **Merge and CD Deploy Trigger:**  
TODO

---