import datetime
import os
import pandas as pd
import numpy as np
import json
import re
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.colors as co

data_path = "./data"
total_stock_path = './data/total/%s.pkl' % ("total")
countries_path = './data/countries.xlsx'
path_stock_list = "./data/stock.xlsx"
pdf_analysis_path = './data/total'
hsi_etf_path = './data/2800.pkl'

def get_countries(path):
    df = pd.read_excel(path)
    df = pd.unique(df['country'])
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


def get_hsi_etf(path):
    df = pd.read_pickle(path)
    return df

countries = get_countries(countries_path)
stock_list = read_stock_list(path_stock_list)
total_stock_price = get_total_stock(total_stock_path)
total_stock_analysis = get_total_stock_analysis(stock_list, pdf_analysis_path)
stock_price_2800 = get_hsi_etf(hsi_etf_path)

country_stock_mean = total_stock_analysis.groupby(['Country', "lat", "lng", "Stock Code"])['Percent'].mean().reset_index()

#
# def plot_maps(frame, stock_list):
#     for index, row in stock_list.iterrows():
#         try:
#             stock_code = row['Stock Code']
#             m = Basemap(projection='cyl')
#             scale = 0.2
#             m.shadedrelief(scale=scale)
#
#             cmap = plt.cm.jet
#             vmin = 0
#             vmax = 100
#
#             data = frame.loc[frame['Stock Code'] == stock_code]
#
#             lon = [row['lng'] for index, row in data.iterrows()]
#             lat = [row['lat'] for index, row in data.iterrows()]
#             wind = [row['Percent'] for index, row in data.iterrows()]
#             plt.scatter(lon, lat, marker='o',
#                         c=wind, alpha=0.5, zorder=10, vmin=vmin, vmax=vmax, cmap=cmap)
#
#             try:
#                 norm = co.Normalize(vmin=vmin, vmax=vmax)
#                 pointcolors = plt.cm.ScalarMappable(norm, cmap)
#                 pointcolors.set_array([])
#                 cbar = m.colorbar(pointcolors, location='bottom')
#                 cbar.set_label('%')
#             except Exception as e:
#                 pass
#
#             plt.title('Stock %s Country distribution' % stock_code)
#             plt.show()
#
#
#         except Exception as e:
#             print(e)
#
#
# plot_maps(country_stock_mean, stock_list)