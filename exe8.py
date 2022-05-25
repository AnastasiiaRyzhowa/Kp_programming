import json
import re
with open('periodic_table.json', 'r', encoding='utf-8') as f:
    data=json.load(f)
def decode_ch(sting_of_elements):
    s=re.findall('[A-Z][a-z]*', sting_of_elements)#разделяет на элементы если находит заглавную букву
    for i in s:
        if i in data.keys():
           print(data[i], end='')
(decode_ch('NOTiFICaTiON'))


