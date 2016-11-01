#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 10/31/16.
"""

from pymongo import MongoClient

MONGODB_HOST = '120.27.39.12'
MONGODB_PORT = 27017
db_name = 'rnadb'
mirna = 'mirna'
cancer = 'cancer'

db_client = MongoClient(MONGODB_HOST, MONGODB_PORT)
db = db_client[db_name]
mirna_collection = db[mirna]
cancer_collection = db[cancer]


def parse_mirna():
    with open('miRNAName.txt') as mirna:
        for line in mirna.readlines():
            print(line)
            mirna_collection.insert_one(
                {'mirna': line.strip()}
            )


def parse_cancer():
    with open('CancerName.txt') as cancers:
        for line in cancers.readlines():
            cancer_collection.insert_one({
                'cancer': line.strip()
            })

if __name__ == '__main__':
    parse_cancer()
    parse_mirna()
