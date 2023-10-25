#url逆转义

import urllib.parse

with open('test.txt', 'r', encoding='utf-8') as input_file:
    with open('unescaped_urls.txt', 'w', encoding='utf-8') as output_file:
        for line in input_file:
            line = line.strip()
            unescaped_line = urllib.parse.unquote(line, encoding='utf-8', errors='replace')
            output_file.write(unescaped_line + '\n')

#去掉空行
'''
with open('test.txt', 'r') as f:
    lines = f.readlines()

with open('out.txt', 'w') as f:
    for line in lines:
        if line.strip():
            f.write(line)
'''
