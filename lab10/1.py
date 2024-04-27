import csv
import psycopg2 as pgsql 

connection=pgsql.connect(host="localhost", dbname="postgres", user="postgres", 
                         password="ridik2003", port=5432)
cur=connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS PhoneBook (
    surname VARCHAR(255),
    name VARCHAR(255),
    number INT
);
""")

def update(sn, mode, newv):
    cur.execute("""UPDATE PhoneBook
    SET {} = '{}'
    WHERE surname = '{}'
    """.format(mode,newv,sn))

def delete(sn):
    cur.execute("""DELETE FROM PhoneBook
    WHERE surname='{}'
    """.format(sn))

#INSERTING DATA--------------------------

mode="enter";
while True:
    print("Type 'enter' if you want to add more data and type 'stop' to break")
    mode=input()
    if mode=="stop":
        break
    mytuple=[]
    print("enter surname:")
    mytuple.append(input())
    print("enter name:")
    mytuple.append(input())
    print("enter number:")
    mytuple.append(input())
    mytuple=tuple(mytuple)
    cur.execute("""INSERT INTO PhoneBook (surname, name ,number) VALUES
    {};
    """.format(mytuple))

while True:
    print("Want to insert data from csv file? yes/no:")
    mode=input()
    if mode=="no":
        break
    print("Enter the name of the file (without extension)")
    filename=input()
    filepath = f"C:/Users/user/Desktop/PP2s/lab10/{filename}.csv"  # Измененный путь к файлу
    try:
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                cur.execute("INSERT INTO PhoneBook VALUES (%s,%s,%s)",row)
                
    except FileNotFoundError:
        print("File not found")

#UPDATING DATA---------
while True:
    print("Type 'update' to update some data or 'stop' to break")
    mode=input()
    if mode=="stop":
        break
    cur.execute("""SELECT * FROM PhoneBook""")
    print(cur.fetchall())
    print("Enter surname")
    idtochange=input()
    print("What you want to change? name/number")
    mode=input()
    print("Enter new name/number")
    newvalue=input()
    update(idtochange, mode, newvalue)

#DELETING DATA-----------
while True:
    print("want to delete some data? yes/no")
    mode=input()
    if mode=="no":
        break
    cur.execute("""SELECT * FROM PhoneBook""")
    print(cur.fetchall())
    print("Enter surname")
    idtodelete=input()
    delete(idtodelete)

connection.commit()
cur.close()
connection.close()
