import datetime
import os
import pandas as pd
import json
import slate3k as slate
import PyPDF2
import re

data_path = "./data"
total_stock_path = './data/total/%s.pkl' % ("total")
countries_path = './data/countries.xlsx'
path_stock_list = "./data/stock.xlsx"
pdf_analysis_path = './data/total'


def get_countries(path):
    df = pd.read_excel(path)
    countries = df.groupby(['country'])['lat', 'lng'].mean().reset_index()
    return countries


def read_stock_list(path):
    df = pd.read_excel(path)
    return df


def normalize_total_stock(stock_list):
    total_stock = pd.DataFrame()
    for index, row in stock_list.iterrows():
        stock_code = row['Stock Code']
        stock_price = pd.read_pickle('./data/%s.pkl' % (stock_code))
        stock_price = stock_price.reset_index()
        stock_start = stock_price.loc[0]
        stock_price['Norm Close'] = stock_price.apply(lambda x: x['Close']/stock_start['Close'], axis=1)
        stock_price.to_pickle('./data/%s.pkl' % (stock_code))
        total_stock = pd.concat([total_stock, stock_price])

    total_stock.to_pickle(total_stock_path)


def normalize_total_stock_analysis(stock_list, countries, path):
    for index, row in stock_list.iterrows():
        try:
            stock_code = row['Stock Code']
            pkl_path = os.path.join(path, "%s_analysis.pkl" % (stock_code))
            df = pd.read_pickle(pkl_path)
            df = pd.merge(df, countries, how='left', left_on='Country', right_on='country',)
            df = df.drop(columns=['country'])

            total_sum_count_year_month = df.groupby(['Year', 'Month'])['Count'].sum().reset_index()

            def get_percent(x, sum_list):
                base = sum_list.loc[(sum_list['Year']==x['Year']) & (sum_list['Month']==x['Month'])].iloc[0]
                if base['Count'] == 0:
                    base['Count'] = 1
                return x['Count']/base['Count'] * 100

            df['Percent'] = df.apply(lambda x: get_percent(x, total_sum_count_year_month), axis=1)
            df.to_pickle(pkl_path)

        except Exception as e:
            print(e)



countries = get_countries(countries_path)
stock_list = read_stock_list(path_stock_list)
#normalize_total_stock(stock_list)
normalize_total_stock_analysis(stock_list, countries, pdf_analysis_path)