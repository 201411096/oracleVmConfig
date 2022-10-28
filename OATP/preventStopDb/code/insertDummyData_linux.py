"""
python autonomous database
Quick Start: Developing Python Applications for Oracle Autonomous Database

https://www.oracle.com/database/technologies/appdev/python/quickstartpython.html

1. install python



2. install cx_Oracle
python -m pip install cx_Oracle --upgrade --user


3. install the Oracle Instant Client Basic Package
Download the free Oracle Instant Client Basic zip file from Oracle Instant Client for Microsoft Windows (x64) 64-bit. (If your Python is 32-bit, then you will need to download the 32-bit Basic package from here instead). Remember to install the matching VS Redistributable, as shown on the download page.
Extract the libraries to an accessible directory, for example the libraries could be in C:\oracle\instantclient_19_9



4. Unzip the Wallet
Make a network\admin sub-directory in your Instant Client directory, for example C:\oracle\instantclient_19_9\network\admin.
Unzip the previously obtained credentials zip file and move the extracted files to the new network\admin sub-directory.
-> wallet 폴더 안의 파일들만 추출해서 붙여넣기



5. Create a Python Appllication
import cx_Oracle


cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_9")

connection = cx_Oracle.connect(user="admin", password="XXXX", dsn="XXX_dbhigh")

cursor = connection.cursor()

# Create a table

cursor.execute("/""begin
                     execute immediate 'drop table pytab';
                     exception when others then if sqlcode <> -942 then raise; end if;
                  end;""/")
cursor.execute("create table pytab (id number, data varchar2(20))")

# Insert some rows

rows = [ (1, "First" ),
         (2, "Second" ),
         (3, "Third" ),
         (4, "Fourth" ),
         (5, "Fifth" ),
         (6, "Sixth" ),
         (7, "Seventh" ) ]

cursor.executemany("insert into pytab(id, data) values (:1, :2)", rows)

# connection.commit()  # uncomment to make data persistent

# Now query the rows back

for row in cursor.execute('select * from pytab'):
    print(row)



6. Run the Python Application




------------------------------------------------------------------------------------------------------------------------------------------------------------
pip install cx_Oracle --upgrade
pip install oracledb --upgrade

should copy from files in oracle cloud wallet to instantclient/network/admin
------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

import cx_Oracle
import time
import sys

lib_dir = r"./instantclient/instantclient_21_8"
#lib_dir = r"./WALLET_OTP"
user = "admin"
password = "mypassword"
dsn = "dbname_high" # ex) OATP_high

def cx_Oracle_init():
#    cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    cx_Oracle.init_oracle_client(lib_dir=lib_dir)

def insertDummyData():

    connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)
    cursor = connection.cursor()

    cursor.execute('insert into test_connection values(test_connection_seq.nextval, sysdate)')
    connection.commit()

    cursor.close()
    connection.close()

def wait(sleepTime=86400):
    time.sleep(int(sleepTime))

if __name__ == "__main__":
    cx_Oracle_init()

    while True:
        insertDummyData()
        if(len(sys.argv) > 1 ):
            wait(sys.argv[1])
        else:
            wait()