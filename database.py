#!/bin/python2.7
# -*- coding: utf-8 -*-

import sqlite3 as sql

import time
from time import gmtime, strftime

class Database:
    def __init__(self):
        self.dbFile = 'data.db'
        self.initDB()

    def initDB(self):
        # checking if table exists is done in side schema.sql
        with sql.connect(self.dbFile) as con:
            cur = con.cursor()
            with open('schema.sql', 'r') as schema_file:
                cur.executescript(schema_file.read())

    def createQuery(self, data):
        # http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python
        time.sleep(1)
        query = 'INSERT INTO data VALUES ("{}",'.format(strftime("%Y-%m-%d %H:%M:%S",
        gmtime()))
        attributes = 'light', 'acc', 'tmp', 'baro'
        for i, attr in enumerate(attributes):
            if i < len(attributes)-1:
                query += str(data[attr]) + ','
            else:
                query += str(data[attr]) + ')'
        return query

    def insert(self, data):
        query = self.createQuery(data)
        print query
        with sql.connect(self.dbFile) as con:
            cur = con.cursor()
            cur.execute(query)

    def retreive(self, type_, from_, to):
        if type_ == 'all':
            pass
        elif type_ == 'range':
            pass
        elif type_ == 'to':
            pass
