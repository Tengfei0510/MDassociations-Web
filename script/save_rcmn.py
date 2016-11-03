#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 11/3/16.
"""
import pyexcel as pe
from pymongo import MongoClient

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
db_name = 'rnadb'
collection_name = 'rcnmn'


db_client = MongoClient(MONGODB_HOST, MONGODB_PORT)
db = db_client[db_name]
collection = db[collection_name]


def read_data():
    cancers_list = []
    mirna_list = []
    with open('Cancer.txt') as cancer_txt:
        cancers = cancer_txt.readlines()
        for cancer in cancers:
            cancers_list.append(cancer.strip())

    with open('miRNA.txt') as mirna_txt:
        mirnas = mirna_txt.readlines()
        for mirna in mirnas:
            mirna_list.append(mirna.strip())
    lines = pe.iget_records(file_name="beta9.xlsx")
    current = 0
    for records in lines:
        current_c = 0
        try:
            for record in records:
                collection.insert_one(
                    {
                        'cancer': cancers_list[current_c],
                        'mirna': mirna_list[current],
                        'score': record,
                    }
                )
                current_c += 1
        except:
            print(current)

        current += 1

if __name__ == '__main__':
    read_data()
