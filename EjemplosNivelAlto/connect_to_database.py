#!/usr/bin/env python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="charly",
  database="mydatabase"
)
