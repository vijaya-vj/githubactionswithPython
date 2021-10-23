#print('Happy Python Programming!!!')
import numpy as np
import pandas as pd
import xlrd
import time
import sys

"""Sample script for Automating sql statements using Python"""
"""Excel sheet should not have any empty columns/rows"""

SourceFile = r'src/Source.xlsx'
#------------------------------------------------------------------------------------------
#start = time.time()
sys.stdout = open("./destination/AutomateQueries.sql", 'w') # write output in InsertStatement.sql
df = pd.read_excel(SourceFile, None)  # gets all Excel Sheet Names
""" loops through each excel tab"""
for pageTab in df:
    insertColumns = ''
    insertValues = []
    insertSql = ''
    print('-- ' + pageTab)
    # load tab to df
    page_df = pd.read_excel(SourceFile, sheet_name=pageTab)
    dframe=pd.DataFrame(page_df)
    dframe=dframe.replace({np.nan: 'null'})
    records = dframe.to_records(index=False)
    result = list(records)
    data=dframe.shape
    columns=data[1]
    for col in range(0,columns):
      insertColumns += str(dframe.columns[col]) + ","
    for col in range(0,len(dframe)):
      insertValues.append(str(result[col]))
    for value in insertValues:
     insertSql+= 'Insert into ' + pageTab + ' (' + insertColumns[:-1] + ') values ' + value + ';'
    print(insertSql)
    print("\n\n")

#"""Calculate total time"""
#end = time.time()
#print("--Time taken to execute:",end-start)
sys.stdout.close()







