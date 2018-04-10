#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 10/31/16.
"""

import pyexcel as pe
from pymongo import MongoClient

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
db_name = 'LncCeRBase'
collection_name = 'LMM'

db_client = MongoClient(MONGODB_HOST, MONGODB_PORT)
db = db_client[db_name]
collection = db[collection_name]

def parse_excel_to_save():
    records = pe.iget_records(file_name="lncRNA-miRNA-mRNA_assciations.xlsx")
    for record in records:
        try:
            collection.insert_one({
                'PubMed_ID': record['PubMed ID'],
                'Journal': record['Journal'],
                'Title': record['Title'],
                'Year': record['Year'],
                'Gene': record['Gene'],
                'Gene_ID': record['Gene ID (All)'],
                'LncRNA': record['LncRNA'],
                'Disease_Tissue': record['Disease/Tissue'],
                'MiRNA': record['MiRNA'],
                'Pathway_Name': record['Pathway Name']
            })
        except:
            print('exception')


def create_index():
    collection.create_index("MiRNA")
    collection.create_index('LncRNA')
    collection.create_index('Gene')
    collection.create_index('Gene_ID')
    collection.create_index('Disease_Tissue')


def clear_db():
    collection.remove()


if __name__ == '__main__':
    clear_db()
    parse_excel_to_save()
    create_index()
