"""Configuration variables for the ISC301 week 1 project.

Used for centralizing paths definitions, among other things.
"""

import os
import yaml


# Root of the repository.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))


def load_config(project_root):
    """Load project configuration file."""
    with open(os.path.join(project_root, "config.yaml")) as p:
        config = yaml.safe_load(p)
    return config


config = load_config(project_root)

campaign_name = config["campaign_name"]

raw_data_folder = os.path.join(project_root, config["raw_data_folder"])
clean_data_folder = os.path.join(project_root, config["clean_data_folder"])

# Campaign-specific folders.
fuel_consumption_raw_path = os.path.join(raw_data_folder,"fuel_consumption.csv")
