from pandas.core.frame import DataFrame
from pandas.core.indexes.base import Index
import requests 
import pandas as pd
# from varname import nameof
import os,sys
from io import StringIO

if len(sys.argv)<3:
   print(f"Usage: python {sys.argv[0]} filename url")
   exit(-1)
url=sys.argv[2]
filename=sys.argv[1]

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

if "http" not in url:
    url='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_dup&ft=4&o=-change'
    url='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_13w20o&ft=4&o=-change'
    url='https://finviz.com/screener.ashx?v=111&f=sec_technology,sh_curvol_o50,sh_price_o5,ta_perf_dup&ft=4&o=-change'
#url to parameterize
# url = 'https://finviz.com/screener.ashx?v=111&s=ta_topgainers&f=sh_curvol_o100,sh_price_o1'
# url = 'https://finviz.com/screener.ashx?v=111&f=cap_microover,sh_curvol_o50,sh_price_o5,ta_perf_d5o&ft=4&o=-change'
# url = 'https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o3,ta_perf_d5o&ft=3&o=-change'
# health = 'https://finviz.com/screener.ashx?v=111&f=sec_healthcare,sh_curvol_o50,sh_price_o3,ta_perf_d5o&ft=4&o=-change'
# ETF='https://finviz.com/screener.ashx?v=111&f=ind_exchangetradedfund,sh_curvol_o50,sh_price_o3,ta_perf_d5o&ft=4&o=-change'

# down5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o10,ta_perf_d5u&ft=4&o=sector&r=21'
# down5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o10,ta_perf_d5u&ft=4&o=change'
# down5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o10,ta_perf_d5u&ft=4&o=change'
# down5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o10,ta_perf_d5u&ft=4&o=change'

# down5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o10,ta_perf_dup&ft=4&o=-change&r=2741'
# down5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o1,ta_perf_d5o&ft=4&o=-change'

# down5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o5,ta_perf_dup&ft=4&o=-change'
# down5='https://finviz.com/screener.ashx?v=111&f=ind_stocksonly,sh_curvol_o50,sh_price_o10,ta_perf_dup&ft=4&o=-change'
# down5='https://finviz.com/screener.ashx?v=111&f=ind_exchangetradedfund,sh_curvol_o50,sh_price_o10,ta_perf_dup&ft=4&o=-change&r=41'
# # down5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o10,ta_perf_d5o&ft=4&o=-change&r=61'
# # down5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o10,ta_perf_d5o&ft=4&o=-change'
# # up5= 'https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_d5o&ft=4&o=-change'
# down5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_d5u&ft=4&o=change'
# health='https://finviz.com/screener.ashx?v=111&f=sec_healthcare,sh_curvol_o50,sh_price_o7,ta_perf_d5u&ft=4&o=change'
# tech='https://finviz.com/screener.ashx?v=111&f=sec_technology,sh_curvol_o50,sh_price_o7,ta_perf_d5u&ft=4&o=change'
# down5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_d5u&ft=4&o=change'
# up5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_dup&ft=4&o=-change'
# up5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_d5o&ft=4&o=-change'
# upall='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_dup&ft=4&o=-change'
# upETF='https://finviz.com/screener.ashx?v=111&f=ind_exchangetradedfund,sh_curvol_o50,sh_price_o7,ta_perf_dup&ft=4&o=-change'
# nonus='https://finviz.com/screener.ashx?v=111&f=geo_notusa,sh_curvol_o50,sh_price_o7,ta_perf_d5o&ft=4&o=-change'
# up5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_d5o&ft=4&o=-sector'
# down5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o10,ta_perf_d5u&ft=4&o=change'
# up5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_d5o&ft=4&o=-change'
# down5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o10,ta_perf_d5u&ft=4&o=change'
# up5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_d5o&ft=4&o=-change'
# down5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_d5u&ft=4&o=change'
# up55='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o5,ta_perf_d5o&ft=4&o=-change'
# up105='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_d5o&ft=4&o=-change'
# ETF='https://finviz.com/screener.ashx?v=111&f=ind_exchangetradedfund,sh_curvol_o50,sh_price_o10,ta_perf_d5o&ft=4&o=-change'
# nonUSup5='https://finviz.com/screener.ashx?v=111&f=geo_notusa,sh_curvol_o50,sh_price_o5,ta_perf_d5o&ft=4&o=-change'
# china='https://finviz.com/screener.ashx?v=111&f=geo_asia,sh_curvol_o50,sh_price_o1,ta_perf_d5o&ft=4&o=-change'
# up75='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_d5o&ft=4&o=-change'
# down5='https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_d5u&ft=4&o=change'
# energy='https://finviz.com/screener.ashx?v=111&f=sec_energy,sh_curvol_o50,sh_price_o10,ta_perf_d5o&ft=4&o=-change'

# https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o10,ta_perf_d15o&ft=4&o=-change
# https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o10,ta_perf_d10u&ft=4&o=-change

# if updown ==  'up':
#     url = f'https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_d{percent}o&ft=4&o=-change'
# elif updown == 'down':
#     url = f'https://finviz.com/screener.ashx?v=111&f=sh_curvol_o50,sh_price_o7,ta_perf_d{percent}u&ft=4&o=-change'
# else:
#     url=energy
# url=down5
# url=nonUSup5
# url=up105
# url=china
# url=up75
# ETFDown='https://finviz.com/screener.ashx?v=111&f=ind_exchangetradedfund,sh_curvol_o50,sh_price_o10,ta_perf_d5u&ft=4&o=change'
# url=ETFDown

outfile=f'2023-summer-bull1000.csv'
if filename!="":
    outfile=filename

import sys
# print(sys.version_info)
import time
def get_screener(num=0):
    screen = requests.get(url+'&r='+str(num), headers = headers).text
    # tables = pd.read_html(screen)
    tables = pd.read_html(StringIO(screen))
    tables = tables[-2]
    tables.columns = tables.iloc[0]
    tables = tables[1:]
    #removes the number column from the table
    # del tables["No."]
    return tables 


def push_csv(file, table,headerVar):
    table.to_csv(file,mode='a',header=headerVar,index=False)


#gets the total amount 
# def get_total():
#     screen = requests.get(url, headers = headers).text
#     tables = pd.read_html(screen)
#     total = tables[-3][0][0][7:11]
#     total=total.split()[0] #29 #1
#     return total
# #outfile=f'2022-down-March4-crash500.csv'
# print("total stocks:",get_total())
# items=outfile.split(".")
# outfile=f"{items[0]}-{get_total()}.{items[1]}"
#gets the total amount 
def get_total():
    screen = requests.get(url, headers = headers).text
    # tables = pd.read_html(screen)
    tables = pd.read_html(StringIO(screen))
    #total = tables[-3][0][0][7:11]
    # total = tables[-3][0][0].split(" ")[-2]
    # total=total.split()[0] #29 #1

    row=tables[-5].iloc[2].iloc[0]
    total=float(row.split(" ")[2])
    return total
#outfile=f'2022-down-March4-crash500.csv'
print("total stocks:",int(get_total()))
items=outfile.split(".")
if len(items)>=2:
    outfile=f"{items[0]}-{get_total()}.{items[1]}"
else:
    outfile=f"{items[0]}-{get_total()}"

push_csv(outfile,get_screener(0),True)
i = 20
#runs through all the values between 0 and the max total value and adds them to the csv
while(i<int(get_total())):
    time.sleep(2)
    push_csv(outfile,get_screener(i),False)
    i+=20
    print(i)

print(f"check file {outfile}")
