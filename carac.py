# -*- coding: utf-8 -*-
# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import sqlite3

class carac:

    def abrir(self):
        conexion=sqlite3.connect("alternativas.db")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into alternativas(nombre, car1, car2, car3, car4, car5, car6, car7, car8, precio) values (?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        
    def baja(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="delete from alternativas where codigo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()

    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select nombre, car1, car2, car3, car4, car5, car6, car7, car8, precio from alternativas where codigo=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select codigo, nombre, car1, car2, car3, car4, car5, car6, car7, car8, precio from alternativas"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()
            
            
    def modificacion(self, datos):
           try:
               cone=self.abrir()
               cursor=cone.cursor()
               sql="update alternativas set nombre=?, car1=?, car2=?, car3=?, car4=?, car5=?, car6=?, car7=?, car8=?, precio=? where codigo=?"
               cursor.execute(sql, datos)
               cone.commit()
               return cursor.rowcount
           except:
               cone.close()
    def view(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select codigo, nombre, car1, car2, car3, car4, car5, car6, car7, car8, precio from alternativas"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

