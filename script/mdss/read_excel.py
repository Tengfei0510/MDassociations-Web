#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 10/31/16.
"""

import pyexcel as pe
from pymongo import MongoClient

MONGODB_HOST = '120.27.39.12'
MONGODB_PORT = 27017
db_name = 'rnadb'
collection_name = 'rna_cancer'


db_client = MongoClient(MONGODB_HOST, MONGODB_PORT)
db = db_client[db_name]
collection = db[collection_name]


def parse_excel():
    pmid_dict = dict()
    records = pe.iget_records(file_name="pmid2.xlsx")
    for record in records:
        pmid_dict[record['name']] = record['pmid']

    rna_data = pe.iget_records(file_name="rnadb.xlsx")
    for rna in rna_data:
        if rna['pmid'] in pmid_dict:
            rna['pmid'] = pmid_dict[rna['pmid']]
        try:
            collection.insert_one({
                'rna': rna['rna'],
                'mirbase': rna['mirbase'],
                'pmid': rna['pmid'],
                'cancer': rna['cancer'],
                'details': rna['detail']
            })
        except:
            print('exception')


if __name__ == '__main__':
    parse_excel()
