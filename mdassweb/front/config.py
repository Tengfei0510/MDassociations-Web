#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 10/31/16.
"""
from pymongo import MongoClient

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
db_name = 'rnadb'
mirna = 'mirna'
cancer = 'cancer'
collection_name = 'rna_cancer'

db_client = MongoClient(MONGODB_HOST, MONGODB_PORT)
db = db_client[db_name]
mirna_collection = db[mirna]
cancer_collection = db[cancer]
rna_collection = db[collection_name]
