#coding=utf-8
import sys
import json
from zipfile import ZipFile

def utf8escape(str):
    ret = '';
    for char in str:
   	ret += '&#' + hex(ord(char))[1:] + ';'
    return ret

def process(nodes):
    ret = ''
    for node in nodes:
    	ret += '<node text="%s">' % utf8escape(node['title'])
    	if node['children']:
        	ret += process(node['children'])
    	ret += '</node>'
    return ret

mindfile = ZipFile(sys.argv[1], 'r').open('map.json').read()
data = json.loads(mindfile)

export = '<map version="0.9.0">'
export += process([data['root']])
export += '</map>'

exportfile = open(sys.argv[2], 'wb+')
exportfile.write(export.encode('utf-8'))

