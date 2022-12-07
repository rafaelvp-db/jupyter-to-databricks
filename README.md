# Python Github Action

Convert Jupyter Notebooks to Databricks Notebooks

## Sample Usage

```yaml
name: lint

on: push

env:
  DATABRICKS_HOST: ${{ secrets.DATABRICKS_HOST }}
  DATABRICKS_TOKEN: ${{ secrets.DATABRICKS_TOKEN }}

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
    - name: Convert Jupyter Notebooks to Databricks Notebooks
      uses: rafaelvp-db/jupyter-to-databricks@v1.3
      with:
        inputPath: jupyter
        outputPath: databricks
    - name: Run Databricks Notebook
      uses: databricks/run-notebook@v0.0.2
      with:
        local-notebook-path: databricks/example.py
        existing-cluster-id: 0807-225846-motto493


```
