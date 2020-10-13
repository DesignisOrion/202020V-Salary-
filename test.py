# Author : Orion Ford
# Project: Accessing SQLite 202020V database into pandas.
# Datbase created using DB Browser SQLite


import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
#import gzip

# Create a SQL connection to our SQLite database
con = sqlite3.connect("202020V.db")

df = pd.read_sql_query("SELECT * from EmployeeSalary", con)

print(df)
con.close()
