import os
import toml
import json
import logging
import pandas as pd
import joblib
from datetime import datetime

PROJECT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir)
)


def load_config():
    """

    @return:  toml file configurations
    @rtype: object
    """
    config_file = "config.toml"
    filepath = os.path.join(PROJECT_DIR, "config", config_file)
    with open(filepath, "r") as f:
        return toml.load(f)