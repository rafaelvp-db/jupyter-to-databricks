import fire
import json
import logging
import glob
import os

class Converter(object):
    """A simple converter class."""

    def _convert(self, jupyter_dict):

        target_output = "# Databricks notebook source\n"

        for cell in jupyter_dict["cells"]:
            if cell["cell_type"] in ["heading", "markdown"]:
                line = f"# MAGIC %md\n# MAGIC {'# MAGIC '.join(cell['source'])}\n"
            elif cell["cell_type"] == "code":
                line = f"{''.join(cell['source'])}\n"
            line += "\n# COMMAND ----------\n"
            target_output += line

        return target_output

    def run(self, input_path, output_path):
        for ipynb in glob.glob(os.path.join(input_path, "*.ipynb")):
            with open(ipynb, "r") as ipynb_file:
                jupyter_str = ipynb_file.read()
                logging.info(f"Input Jupyter Notebook: {jupyter_str[:20]}")
                jupyter_dict = json.loads(jupyter_str)

            target_output = self._convert(jupyter_dict)
            file_name = ipynb.split("/")[-1].replace(".ipynb", "")

            with open(os.path.join(output_path, f"{file_name}.py"), "w") as output:
                output.write(target_output)
            logging.info(f"Wrote Databricks notebook to {output_path}/{file_name}.py")


if __name__ == '__main__':
  fire.Fire(Converter)