#Contex managers => objects that define a temporary context for ablock of code.
#Multithreading/ multiprocessing => Carrying out several processes at the same time.

#Exercise one :A context manager for opening and closing a file automatically
#Using with creates a working context manager in action to do work automatically during openng and closing a file
class File_context_manager:
    def __init__(self):
        print("File context manager started")
    def __enter__(self):
        print("Beginning context management")
    def __exit__(self,exc_type,exc_val,exc_tb):
        print("End of file context manager")
with File_context_manager():
    with open("data.txt","w") as file:
        file.write("Helo Jeff")
        
    with open("data.txt","r") as file:
        data = file.read()
        print("Content : ",data)
        file.close()
        
        
#Exercise two : Database management context manager

"""

import mysql.connector as db
class Database_context_manager:
    def __init__(self):
        print("database context manager started")
    def __enter__(self):
        print("beginning database context management")
    def __exit__(self,exc_type,exc_val,exc_tb):
        print("End of database context manager")
with Database_context_manager():
    con = db.connect(host ="localhost",user ="root",password ="")
    if(con):
        print("Database connection established")
        
"""
        
#EXerecise three : multthredaing and multiprocessing that runs functions at different times

import threading as td
from queue import Queue as que
import time as tm

print("MULTI-THREADING")
def Thread_one(num):
    print(num)
    tm.sleep(2) # waits for two seconds to execute
def Thread_two():
    print("one")
if __name__ == '__main__':
    for i in range(5):
        t1 = td.Thread(target=Thread_one, args= (i,))
        t2 = td.Thread(target=Thread_two)
        t1.start()
        t2.start()

#join makes one process to wait for another
        t1.join()
        t2.join()
        
print("MULTI-PROCESSES")
        
import multiprocessing as mtp
def job_one (nmb):
    print(nmb)
def job_two():
    print("Cow")
if __name__ == '__main__':
    for k in range(5):
        p1 = mtp.Process(target=job_one, args=(i,))
        p2 = mtp.Process(target=job_two)
        p1.start()
        p2.start()
        
#join makes one process to wait for another
        p1.join()
        p2.join()


