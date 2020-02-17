#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conexion=sqlite3.connect("bd1.db")
try:
    conexion.execute("""create table alternativas (
                              codigo integer primary key AUTOINCREMENT,
                              nombre text,
                              car1 text,
                              car2 text,
                              car3 text,
                              car4 text,
                              car5 text,
                              precio real
                        )""")
    print("Se creo la tabla alternativas")
except sqlite3.OperationalError:
    print("La tabla alternativas ya existe")
conexion.close()
