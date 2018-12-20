import os
from threading import Thread

import pandas as pd
import slate3k as slate
import numpy as np


data_path = "./data"
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
    print("%s start" % (code))
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
                        if row['Country'].lower() in all_pdf_text.lower():
                            countries_df.loc[countries_df['Country'] == row['Country'], "Count"] += 1

                    except Exception as e:
                        print(code, e)

                total_countries_df = pd.concat([total_countries_df, countries_df])
        except Exception as e:
            print(code, e)

    total_countries_df.to_pickle('./data/total/%s%s.pkl' % (code, "_analysis"))
    print("%s done" % (code))
    return total_countries_df


def batch_analysis_finanical_statement(codes, countries):
    for index, row in codes.iterrows():
        stock_code = row['Stock Code']
        analysis_stock = analysis_finanical_statement(stock_code, countries)


def main():
    threads = []
    cluster = 10
    countries = get_countries(countries_path)
    stock_list = read_stock_list(path_stock_list)

    stock_list_parts = np.split(stock_list, cluster)

    try:
        for c in stock_list_parts:
            t = Thread(target=batch_analysis_finanical_statement, args=(c, countries))
            t.daemon = True
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    except Exception as e:
        print("Error: unable to start thread")

main()