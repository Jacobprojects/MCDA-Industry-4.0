#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conexion=sqlite3.connect("alternativas.db")
try:
    conexion.execute("""create table alternativas (
                              codigo integer primary key AUTOINCREMENT,
                              nombre text,
                              car1 text,
                              car2 text,
                              car3 text,
                              car4 text,
                              car5 text,
                              car6 text,
                              car7 text,
                              car8 text,
                              precio real
                        )""")
    print("La base de datos se creo correctamente.")
except sqlite3.OperationalError:
    print("La base de datos ya existe.")
conexion.close()
