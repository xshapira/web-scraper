from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def scrape(url):
    options = webdriver.FirefoxOptions()
    options.add_argument(" - incognito")

    cap = DesiredCapabilities().FIREFOX
    cap["marionette"] = True
    binary = FirefoxBinary("/Applications/Firefox.app/Contents/MacOS/firefox-bin")
    browser = webdriver.Firefox(
        executable_path="./geckodriver",
        firefox_options=options,
        firefox_binary=binary,
        capabilities=cap,
    )

    browser.get(url)

    timeout = 10

    try:
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located(
                By.XPATH, "//div[@class='crayons-story__body']"
            )
        )
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()


#
