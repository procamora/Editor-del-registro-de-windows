#!/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

def ConectionSQLite(db, query, dict=False):
	conn=sqlite3.connect(db)
	if dict:
		conn.row_factory = __dict_factory
	cursor = conn.cursor()
	cursor.execute(query)

	if query.upper().startswith('SELECT'):
		data = cursor.fetchall()   # Traer los resultados de un select
	else: 
		conn.commit()              # Hacer efectiva la escritura de datos 
		data = None 
		
	cursor.close()
	conn.close()
	
	return data


def __dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d
