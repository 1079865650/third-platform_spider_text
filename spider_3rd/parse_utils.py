from datetime import datetime

import re

def extract_alp_number(string_value):

    string_value = re.sub(r'[^a-zA-Z0-9]', '', string_value)

    return string_value

def extract_number(string_value):

    string_value = re.sub(r'[^0-9]', '', string_value)

    return string_value

def price_parse(string_value):
	# 形如 '169,99.' 处理

    if string_value[-1] == '.':
        string_value = string_value[0:-1]
    if string_value[-3] == ',':
        string_value = string_value.replace(string_value[-3:], string_value[-3:].replace(',','.'))

    return string_value

