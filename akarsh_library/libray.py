import numpy as np 
import pandas as pd
import os
from datetime import datetime

if os.path.exists('books.csv') == True :
    dfbooks = pd.read_csv('books.csv')
else:
    
    dfbooks = pd.DataFrame()
    
    dfbooks['book_id']=[]
    dfbooks['books']=[]
    dfbooks['authers']=[]
    dfbooks['publishers']=[]
    #dfbooks['issued']=[]
    
    dfbooks = dfbooks.set_index('book_id')
    
    dfbooks.to_csv('books.csv',index=True)
    print(dfbooks)

if os.path.exists('students.csv') == True :
    dfstudents = pd.read_csv('students.csv')
else:
    
    dfstudents = pd.DataFrame()
    
    dfstudents['names']=[]
    dfstudents['reg_nos']=[]
    dfstudents['issued_dates']=[]
    dfstudents['book_id']=[]
    
    dfstudents = dfstudents.set_index('book_id')
    
    dfstudents.to_csv('students.csv', index='False')

while True:
    
    print('1. Add book')
    print('2. Issue book')
    print('3. Show books table')
    print('4. Show Student table')
    print('5. Exit')


    x = str(input('Enter your choise : '))
    print('You entered ' + x)
    
    if x == str(1):
        book = str(input('Enter book name : '))
        auth = str(input('Enter auther name : '))
        publ = str(input('Enter publisher name : '))

        df2 = pd.DataFrame()
        
        df2['book_id']=[book+'_'+auth]
        df2['books']=[book]
        df2['authers']=[auth]
        df2['publishers']=[publ]
        #df2['issued']=['False']
             
        print('\n Printing added data \n',df2,'\n')
        
        dfbooks = dfbooks.append(df2, ignore_index=True)
        
        #print(dfbooks)

        dfbooks.to_csv('books.csv',index=False)

    elif x == str(2):
        
        valid = False
        while valid == False:
        
            bookid = input('Enter book_id to issue : ')


            try:
                selected_book = (dfbooks.loc[dfbooks['book_id'] == bookid])

                if selected_book.empty == True:
                    print('no such book in this library')
                else :
                    bookid = bookid
                    valid = True
                    
            except:
                print('error occoured')
               
        	
        name = input('Enter student name :  ')
        regn = input('Enter registration number : ')
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        issu = dt_string
        
        df3 = pd.DataFrame()
        
        df3['names']=[name]
        df3['reg_nos']=[regn]
        df3['issued_dates']=[issu]
        df3['book_id']=[bookid]
    
        dfstudents = dfstudents.append(df3, ignore_index=True)
        
        print(df3)
        
        #print(dfstudents)
        dfstudents.to_csv('students.csv', index=False)
        


    elif x == str(3):
        print(dfbooks)
        
    elif x == str(4):
        print(dfstudents)
    
    elif x== str(5):
        exit()
        

    else:
        print('Please give valid input.') 
        
