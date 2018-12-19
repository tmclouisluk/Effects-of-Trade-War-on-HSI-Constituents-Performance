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

def get_total_stock():
    total_stock = pd.DataFrame()
    listdir = os.listdir(data_path)
    for file in listdir:
        try:
            if file.endswith(".pkl"):
                pkl_path = os.path.join(data_path, file)
                stock = pd.read_pickle(pkl_path)
                stock['Name'] = file.replace(".pkl", "")
                total_stock = pd.concat([total_stock, stock])
        except Exception as e:
            pass

    total_stock.to_pickle('./data/total/%s.pkl' % ("total"))


def get_countries(path):
    df = pd.read_excel(path)
    return df


def read_pdf(path):
    with open(path, 'rb') as f:
        extracted_text = slate.PDF(f)

    return extracted_text


def read_stock_list(path):
    df = pd.read_excel(path)
    return df


def analysis_finanical_statement(code, countries):
    dir_path = os.path.join(data_path, str(code))
    listdir = os.listdir(dir_path)
    total_countries_df = pd.DataFrame()

    for file in listdir:
        try:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(dir_path, file)
                pdf_text = read_pdf(pdf_path)
                all_pdf_text = " ".join(pdf_text)

                countries_df = countries[['Country']]
                countries_df["Count"] = 0
                countries_df["Stock Code"] = code
                countries_df["Year"] = file[3:7]
                countries_df["Month"] = file[7:9]
                for index, row in countries.iterrows():
                    try:
                        if row['Country'].lower() in all_pdf_text:
                            countries_df.loc[countries_df['Country'] == row['Country'], "Count"] += 1

                    except Exception as e:
                        pass

                total_countries_df = pd.concat([total_countries_df, countries_df])
        except Exception as e:
            pass

    return total_countries_df


countries = get_countries(countries_path)
stock_list = read_stock_list(path_stock_list)
total_analysis_stock = pd.DataFrame()
for index, row in stock_list.iterrows():
    stock_code = row['Stock Code']
    analysis_stock = analysis_finanical_statement(stock_code, countries)
    total_analysis_stock = pd.concat([total_analysis_stock, analysis_stock])

total_analysis_stock.to_pickle('./data/total/%s.pkl' % ("total_analysis_stock"))
