# Effects of Trade War on HSI Constituents Performance

## Introduction:
Being one of the most developed financial markets in the world, Hong Kong has attracted
companies from around the globe to list in Hong Kong Stock Exchange. As of 29 Dec 2017, the
market capitalization of the whole Hong Kong market was HKD33,998 billion and number of
listed companies rose to 2,118. The Hong Kong stock market is so important that other important
financial markets will be affected by Hong Kong Stocks and vice-verse.

2018 has been an appalling year for global investors, especially the Hong Kong market. Followed
by a booming year of 2017 where the HSI rose 36% and closed at nearly 30,000 points, 2018 had
a great start that HSI rose to all time high at 33,484 points by the end of Jan 2018. Every investor
was fascinated and invest in the stock market with larger budgets but HSI has dropped to a year
low of 24,540 points by the end of Oct 2018 which was a 27% drop. The situation was a result of
a memorandum signed by the US president to impose tariffs on Chinese products in Mar 2018 and
declared the Trade War.

Trade War was first initiated by the US regarding access of US firms to China’s agriculture, energy,
and financial markets to balance the trade deficit of US.
This study will investigate the severity of trade war to Hong Kong stocks with a focus on HSI
constituents and if there are any industries not being affected by trade war. Comparison will be
made across individual stocks under different industries to identify any top performing stocks that
are worth investing in amid the critical situation under trade war as safe haven
 
## Problems Formulation and Assumptions
### Trade War
The essence of trade war was the continuous disputes over the imbalance of tariffs imposed on the
goods being traded between the two countries.
Trade War was first initiated by the US on 22 March 2018 when the US president a memorandum
to impose additional tariffs on Chinese products such as aerospace, information communication
technology and machinery.
When considering the stocks for this study, we will focus on those that are mainly affected by trade
war.

### Target Stocks of Analysis
The target stocks of this study will focus on the Hong Kong listed companies with international
businesses so that we can track their operating performance (i.e. revenue) and the relevance of
stock price performance with trade war.

The key of identifying the companies for this study is based on the efficiency for programs needed
to read through the financial statements (in PDF format) and the significance of result (whether
the result will give significant meaning to the study).

Given the significant number of listed companies in Hong Kong (over 2,000) and the fact that not
many of them have sufficient international business exposure, this study will focus on Hang Seng
Index constituents. Currently, there are 50 constituents under HSI.

We will also use Tracker Fund (“2800 HK”) as a benchmark of this study and as a proxy of HSI
index performance. The performance of each HSI constituent and the industry that they belong to
will be compared to the performance of Tracker Fund to compare which one has a stronger price
performance amid the trade war period.

### Time Period
The Hong Kong stock market has started to drop since its peak in late Jan 2018. We will compare
the stock price performance pre- and post-trade war. In order to provide a full picture of the stock
performance, we have started the measurement from 20 Dec 2015 to 21 Dec 2018, which is a 3-
year period.


## Ideas:
-  To find undervalued stocks of a specific industry by comparing financial ratios and to check the impact of Trade Wars to its business.
-  The proposed Industry will have business across the globe so that we can calculate the possible effect of Trade Wars on its business.


## Methodology and Limitations:
This study focuses on several skills needed to gather information, process data, and show the endresult.

This study starts by using the latest factsheet of HSI constituents from Hang Seng Index to locate
their stock codes and downloading their latest annual report from Hong Kong Stock Exchange
based on these stock codes for analysis of their global business exposure, particularly towards the
US.

The global business exposure will be measured based on the number of counts of the country
names appeared in their annual report. This is to measure the relative significance of that country
to the business of the company. Spots on countries being mentioned in the annual report are marked
in a world map to show its relative global business exposure.

Stock price performance of each HSI constituent and Tracker Fund will be plotted to show, along
with the time line of the trade war, its performance and whether the percentage exposure of the
companies with the US has direct relationship with the stock price performance.

The industry performance and stock price of top 10 & bottom 10 US and China exposed companies
have also been plotted. The conclusion is made by determining if there are any relationship
between the trade war and any particular industry or percentage of business exposure with the US.


### Web Scraping
After downloading the HSI constituents from the Hang Seng Index, they are converted from pdf
to excel file to store the stock codes and their respective industry.

### Reading PDF
After getting a list of HSI constituents from Hang Seng Index, the annual report of each stock is
downloaded from Hong Kong Stock Exchange to study its international business exposure by
counting the country names shown in the annual report.

In any annual reports, it is not surprised to find a total of more than 100 or even 200 pages. Reading
through the pdf indeed takes a lot of time. In order to speed up, the technique of multithread is
used.

Running several threads is similar to running several different programs concurrently, but with the
following benefits −
-  Multiple threads within a process share the same data space with the main thread and can
therefore share information or communicate with each other more easily than if they were
separate processes.
-  Threads sometimes called light-weight processes and they do not require much memory
overhead; they are cheaper than processes.

A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer
that keeps track of where within its context it is currently running.
-  It can be pre-empted (interrupted)
-  It can temporarily be put on hold while other threads are running.

As a result, the speed is 10x faster with multithread.

There is a limitation to reading financial statements inside annual reports. Since the companies use
different auditor to prepare the financial statements, they are prepared in different format. Hence,
given the scoop of this study is to perform a fundamental analysis such as using PE or sales ratios
etc, we will not cover the financial ratio analysis in this study.

### Data Visualization
There are two main ways of how we show the data gathered above – Mapping of business exposure
in countries across the globe and Stock price chart comparison of individual company and industry
and the companies with the most and least US exposure.

#### Mapping
Our goal is to identify, from annual reports, the business exposure in terms of revenue
generating sources across the globe. However, not many companies disclosed the revenue
breakdown in terms of locations. To deal with this, we used the counts of country names
showing in the respective annual report as a proxy. The reason behind is that if a particular
country is important to the company, it must have been mentioned more times than other
countries.

#### Stock Price Chart
We are interested to know if the trade war has extra effects on any industry or just on some
individual stocks. Industry performance are shown by grouping the individual stock price
performance of the same industry.

We identified the most and least exposed companies to the US and China by counting the
number of names appeared in the annual report and sorted them based the percentage
exposure. The top 10 and bottom 10 exposed companies are kept for further analysis of
stock price performance.

All the above stock price measurements are based on normalized result. Normalization are
calculated by dividing the spot price of the stock on 21 Dec 2018 by the stock price on 20
Dec 2015.

## Result and Conclusion:
From a general world map overview, based on the results, it is observed that different companies
have mentioned quite a lot of countries in their annual report. This is shown by have many “blue”
spots on the map which is referring to <10% coverage of the country name in the report.

It is not surprised to see that the US and China have “orange” to “red” spot which means over 20%
coverage.

Below is the map for stock code 5 for your reference:
![](https://raw.githubusercontent.com/tmclouisluk/Effects-of-Trade-War-on-HSI-Constituents-Performance/master/img/1.JPG)

Furthermore, when looking at industry performance, the “industries” is being affected the most
in that the fluctuation is the biggest for all industries. This is evident that the performance of
industrial sector dropped significantly since Jun 2018 which is close to the start of the entire
trade war.
![](https://raw.githubusercontent.com/tmclouisluk/Effects-of-Trade-War-on-HSI-Constituents-Performance/master/img/2.JPG)

At last, we filtered two lists based on percentage exposure of the company to the US and China
![](https://raw.githubusercontent.com/tmclouisluk/Effects-of-Trade-War-on-HSI-Constituents-Performance/master/img/3.JPG)

As shown in the list, the US and China exposure that a company could get involve with could be
up to as high as almost 50% while at the same time the least exposed company still has 22% of
US and China coverage in their business.

Stock price performance of the stock code: 1113 and 1093 are shown below
![](https://raw.githubusercontent.com/tmclouisluk/Effects-of-Trade-War-on-HSI-Constituents-Performance/master/img/4.JPG)
![](https://raw.githubusercontent.com/tmclouisluk/Effects-of-Trade-War-on-HSI-Constituents-Performance/master/img/5.JPG)

As of 21 Dec 2018, the stock price of 1093 has further dropped whole stock price of 1113 has
started to rebound in late Nov. This result shows that individual stock may not fully reflect the
effect of trade war, but the whole industry performance is a better measurement.

## Appendix:
Please refer all the codes to this repo

## Reference 
-  Hang Seng Index Factsheet:
https://www.hsi.com.hk/static/uploads/contents/en/dl_centre/factsheets/hsie.pdf
-  HKEx Annual Report Download:
http://www3.hkexnews.hk/listedco/listconews/advancedsearch/search_active_main.aspx
