# STAT7008-Project

## Objectives:
To show the techniques including but not limited to those taught in class e.g. web scraping, charting, reading PDF, data manipulation, maps, etc
 
## Ideas:
-  To find undervalued stocks of a specific industry by comparing financial ratios and to check the impact of Trade Wars to its business.
-  The proposed Industry will have business across the globe so that we can calculate the possible effect of Trade Wars on its business.
 
## Python Skills:
### 1. Web Scraping and Reading PDF:
- From Hang Seng Composite Index (https://www.hsi.com.hk/eng/indexes/all-indexes), we can download the industry factsheet and use its way of classification to help us look for the companies (stock codes) of the industry that we think will be affected by Trade War
- With the obtained stock codes, we can go to HKExNews (http://www3.hkexnews.hk/listedco/listconews/advancedsearch/search_active_main.aspx) to download the latest annual financial statements (in PDF formats) 
- Maybe we should obtain up to the last 3 years so that the comparison of the calculated financial ratios will be more valid
- Also we can find the companies that use the same auditor so that when reading the PDFs, the financial data can be obtained with the same method (because the data will be shown in the same format for the same auditor)

### 2. Data Manipulation and Visualisation:
- After obtaining the financial data, we can calculate the financial ratios e.g. P/E, Sales Growth, Trade Cycles
- Visualise the calculated data for comparison (bar chart, boxplot, line chart, pie chart, etc)
- Visualisation (Basemap) for revenue locations to indicate how much its business is affected by Trade War (determined by proportion of business related to the US)
 

