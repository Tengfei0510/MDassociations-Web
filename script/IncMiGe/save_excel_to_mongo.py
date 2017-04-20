#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 10/31/16.
"""

import pyexcel as pe
from pymongo import MongoClient

MONGODB_HOST = '120.27.39.12'
MONGODB_PORT = 27017
db_name = 'INCMIM'
collection_name = 'LMM'

db_client = MongoClient(MONGODB_HOST, MONGODB_PORT)
db = db_client[db_name]
collection = db[collection_name]


def parse_excel_to_save():
    records = pe.iget_records(file_name="lncRNA-miRNA-mRNA.xlsx")
    for record in records:
        try:
            collection.insert_one({
                'PubMed_ID': record['PubMed ID'],
                'Journal': record['Journal'],
                'Title': record['Title'],
                'Year': record['Year'],
                'Gene': record['Gene'],
                'LncRNA': record['LncRNA'],
                'Disease/Tissue': record['Disease/Tissue'],
                'MiRNA': record['MiRNA']
            })
        except:
            print('exception')


def clear_db():
    collection.remove()


if __name__ == '__main__':
    parse_excel_to_save()
