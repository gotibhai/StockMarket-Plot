import quandl
quandl.ApiConfig.api_key = 'yjq-xbLnXxoAsxFDmjVs'
quandl.ApiConfig.api_version = '2015-04-09'

import urllib2
urllib2.urlopen("http://example.com/foo/bar").read()

data = quandl.get('WIKI/AAPL',start_date='2016-1-1', end_date='2017-1-1', column_index='4')
print data