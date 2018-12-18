from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def extract_data(browser, link):
    result = []
    browser.get(link)
    while(True):
        try:
            show_more = browser.find_element_by_xpath("//span[text()='Show More']")
            show_more.click()
        except NoSuchElementException:
            break
        except Exception as ex:
            pass

    items = browser.find_elements_by_class_name("newsblock-story-card")
    for item in items:
        try:
            title = item.find_element_by_css_selector('.newsblock-story-card__title-link').text
            result.append(title)
        except:
            pass

    result = [x.text for x in items]

    return tuple(result)


def main():
    chrome_driver_path = "C:\chromedriver.exe"
    base_link = "https://www.buzzfeednews.com/"
    try:
        browser = webdriver.Chrome(chrome_driver_path)

        result = extract_data(browser, base_link)

    except Exception as e:
        print(e)

main()