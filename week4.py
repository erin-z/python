import requests
import re
import json
import pandas as pd
from datetime import date

def retrieve_quotes_historical(stock_code):
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item] 

'''
quotes = retrieve_quotes_historical('AXP')
quotesdf = pd.DataFrame(quotes)
print(quotesdf)  
'''
quotes = retrieve_quotes_historical('IBM')
list1 = []
for i in range(len(quotes)):
    x = date.fromtimestamp(quotes[i]['date'])
    y = date.strftime(x,'%Y-%m-%d')
    list1.append(y)
quotesdf_ori = pd.DataFrame(quotes, index = list1)
#quotesdf = quotesdf_ori.drop(['date'], axis = 1)
#print(quotesdf)

list1 = []
tmpdf = quotesdf_ori['2016-07-01':'2016-12-31']
for i in range(len(tmpdf)):
    list1.append(int(tmpdf.index[i][5:7]))
tmpdf['month'] = list1

sortedf = tmpdf.sort_values('close')
#print(pd.concat([sortedf[:5], sortedf[len(tmpdf)-5:]]))

#print(tmpdf)
print(tmpdf.groupby('month')['volume'].sum())