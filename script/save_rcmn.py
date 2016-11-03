#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 11/3/16.
"""
import pyexcel
from pymongo import MongoClient

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
db_name = 'rnadb'
collection_name = 'rcnmn'


db_client = MongoClient(MONGODB_HOST, MONGODB_PORT)
db = db_client[db_name]
collection = db[collection_name]


def remove_collection():
    collection.drop()


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

    sheet = pyexcel.get_sheet(file_name="beta9.xlsx")
    print(sheet.row_range())
    for i in sheet.row_range():
        for j in sheet.column_range():
            collection.insert_one(
                {
                    'cancer': cancers_list[j],
                    'mirna': mirna_list[i],
                    'score': sheet[i, j],
                }
            )


def create_index():
    collection.create_index("cancer")

if __name__ == '__main__':
    read_data()
