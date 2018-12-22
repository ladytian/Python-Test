# -*- coding: utf-8 -*-
__author__ = 'tianjiwei'

import requests
from sys import argv

# 解释命令行用法
USAGE = '''USAGE: python get.py https:api.github.com'''

# 判断命令行参数个数
if len(argv) != 2:
	print USAGE
	exit()

# 获取命令行参数，分别是脚本名称和要访问的url
script_name, url = argv

# 判断url组成是否完整
if url[:4] != 'http':
	url = 'http://' + url

# 进行http请求，且请求的时候默认加上指定的请求头
h = {'Content-Type': 'application/json'}
r = requests.get(url, headers=h)

# 输出接口地址、状态码和响应头部
print '接口地址: ' + url
print '状态码: %d' % (r.status_code)
print 'Headers: '
for k, v in r.headers.items():
	print k, ': ', v