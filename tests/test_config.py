import pytest
from pathlib import Path
from hydromt import config


def test_config(tmpdir):
    cfdict = {
        "section1": {
            "list": [1, 2, 3],
            "tuple": (1, "b"),
            "bool": True,
            "str": "test",
            "int": 1,
            "float": 2.3,
            "None": None,
        },
        "section2": {
            "path": "config.ini",  # path exists -> Path
            "path1": "config1.ini",  # path does not exist -> str
        },
        # evaluation skipped by default for setup_config
        "setup_config": {
            "path": "config.ini",
            "float": 2.3,
        },
    }
    config_fn = tmpdir.join("config.ini")
    config.configwrite(config_fn, cfdict)
    cfdict1 = config.configread(config_fn, abs_path=True)
    assert cfdict["section1"] == cfdict1["section1"]
    assert isinstance(cfdict1["section2"]["path"], Path)
    assert isinstance(cfdict1["section2"]["path1"], str)
    assert isinstance(cfdict1["setup_config"]["path"], str)
    assert isinstance(cfdict1["setup_config"]["float"], str)
