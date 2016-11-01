#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 10/31/16.
"""
import requests

from bs4 import BeautifulSoup

base_url = 'https://www.ncbi.nlm.nih.gov/pubmed/?term={}'


def crawler():
    with open('pumid2.txt') as input:
        for line in input.readlines():
            key = line.strip('\n')
            response = requests.get(base_url.format(key))
            page = BeautifulSoup(response.content, 'html.parser')
            try:
                dds = page.find('dl', class_='rprtid').find('dd')
                print(dds.text)
            except:
                print(key)

if __name__ == '__main__':
    crawler()
