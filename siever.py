from handler import *
import os
import re



to_be_popped = []
        
def sieve(main_file_name, file_name):
    file1 = ionize(main_file_name)
    file2 = ionize(file_name)
    #contacts found count
    cts_count = 0 
    for num,details in file1.items():
        for num2 ,details2 in file2.items():
            try:
                
                if details[4].strip('TEL;CELL:+') == details2[4].strip('TEL;CELL:+'):
                    #print(details[3], details[4].strip('TEL;CELL:') )
                    to_be_popped.append(num)
                    cts_count += 1
            except IndexError as x:
                print(x)
                print(f"{num} : {details} ")
                print(f"{num2} : {details2} ")
                
    for inmates in to_be_popped:
        file1.pop(inmates)
    return file1,cts_count        

for num2 ,details2 in file2.items():
    
