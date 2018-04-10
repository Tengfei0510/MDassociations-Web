#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 10/31/16.
"""

from pymongo import MongoClient

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
db_name = 'LncCeRBase'
collection_name = 'LMM'

db_client = MongoClient(MONGODB_HOST, MONGODB_PORT)
db = db_client[db_name]
collection = db[collection_name]


def query_select_items():
    mirnas = collection.find({}, {'MiRNA': 1}).distinct('MiRNA')
    lncrnas = collection.find({}, {'LncRNA': 1}).distinct('LncRNA')
    genes = collection.find({}, {'Gene': 1}).distinct('Gene')
    gene_ids = collection.find({}, {'Gene_ID': 1}).distinct('Gene_ID')
    diseases = collection.find({}, {'Disease_Tissue': 1}).distinct('Disease_Tissue')

    return {
        'mirnas': mirnas,
        'lncrnas': lncrnas,
        'genes': genes,
        'gene_ids': gene_ids,
        'diseases': diseases
    }


def query_search_item(query_item_value, item_type):
    if item_type == 'mirna':
        query = collection.find({'MiRNA': {'$eq': query_item_value}})
    elif item_type == 'lncrna':
        query = collection.find({'LncRNA': {'$eq': query_item_value}})
    elif item_type == 'gene':
        query = collection.find({'Gene': {'$eq': query_item_value}})
    elif item_type == 'gene_id':
        query = collection.find({'Gene_ID': {'$eq': query_item_value}})
    else:
        query = collection.find({'Disease_Tissue': {'$eq': query_item_value}})
    return query
