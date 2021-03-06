from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from collections import ChainMap
import csv
from datetime import datetime
import re

options = Options()
options.headless = True

res = []
json_data_list = []
output_res = []
output_res_arr = []
output_result = []
params = ["DAL", "TSLA"]
for param in params:
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("https://finviz.com/quote.ashx?t=" + param)

    for tr in driver.find_elements_by_xpath('//html/body/div[4]/div/table[2]/tbody//tr'):
        res = [td.text for td in tr.find_elements_by_tag_name('td')]
        output = dict(zip(res[::2], res[1::2]))
        json_data_list.append(output.copy())
    output_res = dict(ChainMap(*json_data_list))
    output_res_arr.append(output_res.copy())
timestamp = datetime.now().strftime("%d-%b-%Y-%H:%M:%S.%f")
with open('finviz-'+timestamp+'.csv', 'w', encoding='utf8', newline='') as output_file:
    fc = csv.DictWriter(output_file, fieldnames=output_res_arr[0].keys(),)
    fc.writeheader()
    fc.writerows(output_res_arr)
