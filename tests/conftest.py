import json

import pytest
from selenium import webdriver

"""
This module contains shared fixtures.
"""


@pytest.fixture(scope='session')
def config():

    with open('config.json') as conf_file:
        config = json.load(conf_file)

    assert config["browser"] in ["chrome", "headless chrome", "edge"]
    assert isinstance(config["implicit wait"], int)
    assert config["implicit wait"] > 0
    return config


@pytest.fixture
def browser(config):

    if config["browser"].lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--log-level=3")
        driver = webdriver.Chrome(options)
    elif config["browser"].lower() == "headless chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("--log-level=3")
        driver = webdriver.Chrome(options=options)
    elif config["browser"].lower() == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--log-level=3")
        driver = webdriver.Edge(options)
    else:
        raise Exception(f"Browser {config['browser']} not supported.")

    driver.implicitly_wait(config["implicit wait"])
    driver.maximize_window()

    yield driver

    driver.quit()
