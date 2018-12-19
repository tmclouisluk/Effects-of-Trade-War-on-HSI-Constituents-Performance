import datetime
import os

from dateutil.relativedelta import relativedelta
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import fix_yahoo_finance as yf
import pandas as pd
from pandas_datareader import data as pdr

chrome_driver_path = "C:\chromedriver.exe"
data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def read_stock_list(path):
    pass


def download_finanical_statement(link, no, year):
    options = webdriver.ChromeOptions()
    download_folder = os.path.join(data_folder, no)

    prefs = {"plugins.always_open_pdf_externally": True,
             "download.default_directory": download_folder,
             "download.prompt_for_download": False,
             }
    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(chrome_driver_path, chrome_options=options)

    browser.get(link)
    try:
        #set params
        input_stock_code = browser.find_element_by_css_selector('#ctl00_txt_stock_code')
        input_stock_code.send_keys(no)

        input_category = browser.find_element_by_css_selector('#ctl00_rbAfter2006')
        input_category.click()
        select_category = Select(browser.find_element_by_css_selector('#ctl00_sel_tier_1'))
        select_category.select_by_value("4")

        now = datetime.datetime.now()
        start_year = now.year - year

        year_category = Select(browser.find_element_by_css_selector('#ctl00_sel_DateOfReleaseFrom_y'))
        year_category.select_by_value(str(start_year))

        btn_search = browser.find_element_by_css_selector('label a')
        btn_search.click()

        a_report_links = browser.find_elements_by_css_selector('a.news')
        for a in a_report_links:
            a.click()
            #browser.get(a.get_attribute("href"))

    except Exception as ex:
        print(ex)

    def every_downloads_chrome(driver):
        if not driver.current_url.startswith("chrome://downloads"):
            driver.get("chrome://downloads/")
        return driver.execute_script("""
            var items = downloads.Manager.get().items_;
            if (items.every(e => e.state === "COMPLETE"))
                return items.map(e => e.file_url);
            """)

    WebDriverWait(browser, 120, 1).until(every_downloads_chrome)
    print("%s downloaded" % (no))
    browser.quit()


def get_stock_price(no, year):
    yf.pdr_override()
    data_frame = pdr.get_data_yahoo("%04d.HK" % int(no), start=datetime.datetime.now() - relativedelta(years=year), end=datetime.datetime.now())
    return data_frame


def main():
    base_link = "http://www3.hkexnews.hk/listedco/listconews/advancedsearch/search_active_main.aspx"
    path_stock_list = "./data/stock"
    year = 3
    try:
        stock_list=read_stock_list(path_stock_list)
        for stock in stock_list:
            get_stock_price("1", year)
            download_finanical_statement(base_link, "1", year)


    except Exception as e:
        print(e)

main()