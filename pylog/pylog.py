import csv
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


"""
Capture a screenshot of the given URL with the given driver and
store the screenshot into a file.
"""
def capture_page(driver, url, filename):
    print(f'Capturing {url}')
    driver.get(url)

    # Remove unwanted elements
    driver.execute_script("""
function removeElement(className) {
    var element = document.querySelector(className);
    if (element)
        element.parentNode.removeChild(element);
}
removeElement(".page-header");
removeElement(".field-recaptcha");
""")
    time.sleep(2)

    element = driver.find_element_by_id('maincontent')
    # png = element.screenshot_as_png
    if not element.screenshot(f'./screenshots/{filename}.png'):
        print(f'Failed capturing: {url}')



options = Options()
options.headless = False

fox = webdriver.Firefox(options=options)
fox.set_window_size(1000, 1700)

urlsReader = csv.reader(open('urls.csv', newline=''))

for row in urlsReader:
    capture_page(fox, row[0], row[1])

fox.quit()
