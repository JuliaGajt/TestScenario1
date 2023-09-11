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
        driver = webdriver.Chrome()
    elif config["browser"].lower() == "headless chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(options=options)
    elif config["browser"].lower() == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception(f"Browser {config['browser']} not supported.")

    driver.implicitly_wait(config["implicit wait"])
    driver.maximize_window()

    yield driver

    driver.quit()
