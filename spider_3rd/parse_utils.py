from datetime import datetime

import re

def extract_alp_number(string_value):

    string_value = re.sub(r'[^a-zA-Z0-9]', '', string_value)

    return string_value

def extract_number(string_value):

    string_value = re.sub(r'[^0-9]', '', string_value)

    return string_value

def extract_price(string_value):
    #  处理 '\n\t\t\t\t\t89<sup>€99</sup>\n\t\t\t' or '199<sup>€</sup>' 转换为89.99  199.00
    # print(type(string_value)) <class 'str'>
    print("string_value=============")
    print(string_value)
    price_split = str(string_value).split("€")
    price_pre = re.sub(r'[^0-9]', '', price_split[0])
    price_suf = re.sub(r'[^0-9]', '', price_split[1])
    if price_suf == '':
        price_suf = '00'
    price = price_pre+'.'+price_suf
    return price

def price_parse(string_value):
	# 形如 '169,99.' 处理

    if string_value[-1] == '.':
        string_value = string_value[0:-1]
    if string_value[-3] == ',':
        string_value = string_value.replace(string_value[-3:], string_value[-3:].replace(',','.'))

    return string_value

