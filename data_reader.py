import datetime
import os
import pandas as pd
import json
import slate3k as slate
import PyPDF2
import re

data_path = "./data"
total_stock_path = './data/total/%s.pkl' % ("total")
countries_path = './data/countries.xls'
path_stock_list = "./data/stock.xlsx"
pdf_analysis_path = './data/total'


def get_countries(path):
    df = pd.read_excel(path)
    return df


def read_stock_list(path):
    df = pd.read_excel(path)
    return df


def get_total_stock(path):
    df = pd.read_pickle(path)
    return df


def get_total_stock_analysis(stock_list, path):
    total = pd.DataFrame()
    for index, row in stock_list.iterrows():
        try:
            stock_code = row['Stock Code']
            pkl_path = os.path.join(path, "%s_analysis.pkl" % (stock_code))
            df = pd.read_pickle(pkl_path)
            total = pd.concat([total, df])

        except Exception as e:
            print(e)

    return total


stock_list = read_stock_list(path_stock_list)
total_stock_price = get_total_stock(total_stock_path)
total_stock_analysis = get_total_stock_analysis(stock_list, pdf_analysis_path)