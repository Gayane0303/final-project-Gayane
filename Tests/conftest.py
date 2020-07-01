import json
import pytest
import selenium.webdriver
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture
def config(scope='session'):
    # Read the file
    cwd = os.getcwd() # Get the current working directory (cwd)
    files = os.listdir(cwd) # Get all the files in that directory
    print ("Files in %r: %s" % (cwd, files))
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome', 'Chrome_Remote']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    #Return config so it can be used
    return config

@pytest.fixture
def browser(config):
    # Initialize the WebDriver instance
    if config ['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config ['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()

    elif config ['browser'] == 'Chrome_Remote':
        b = selenium.webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception (f'Browser "{config["browser"]}" is not supported')

    #Make its calls wait for elements to appear
    b.implicitly_wait(config["implicit_wait"])

    #Maximize browser
    b.maximize_window()

    #Navigate to the URL from Config,
    b.get(config["baseUrl"])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()