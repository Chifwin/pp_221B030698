from configparser import ConfigParser
import psycopg2
import csv

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception("Error")
    return db


def execute(command, need_to_commit=False):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if type(command) == str:
            cur.execute(command)
            if need_to_commit: conn.commit()
        else:
            for c in command:
                cur.execute(c)
                if need_to_commit: conn.commit()

        result = cur.fetchall()
    except Exception as e:
        print(str(e))
    else:
        return result
    finally:
        if conn is not None:
            cur.close()
            conn.close()


def read_csv(name):
    names=[] 
    numbers=[]
    try:
        with open(name,'r') as csvfile: 
            reader=csv.reader(csvfile) 
            for row in reader: 
                numbers.append(row[0])
                names.append(row[1])
    except Exception as e:
        print(e)
        return
    return names,numbers

while True:
    query = input("""Help:
1 - querying data
2 - update
3 - insert
4 - delete
0 - quit\n""")
    if not query.isdigit() or int(query) > 4:
        continue
    query = int(query)
    if query == 0: 
        break

    if query == 1:
        t = input("""0 - get all
1 - get by name
2 - get by phone number
3 - sort by name
4 - sort by phone number\n""")
        if not t.isdigit() or int(t) > 4:
            continue
        t = int(t)

        if t == 0: res = execute("SELECT * FROM numbers")
        elif t == 1:
            name = input("Name ")
            res = execute(f"SELECT * FROM numbers where name='{name}'")
        elif t == 2:
            num = input("Phone number ")
            res = execute(f"SELECT * FROM numbers where phone_number='{num}'")
        elif t == 3:
            res = execute("SELECT * FROM numbers BY ORDER BY name ASC")
        elif t == 4:
            res = execute("SELECT * FROM numbers BY ORDER BY phone_number ASC")

        if res != None:
            print("Number         Name")
            for i in res:
                print(f"{i[2]}    {i[1]}")

    elif query == 2:
        name, num = input("Name: "), input("Phone number: ")
        t = input("Change name? (y/n) ")
        if t == 'y':
            res = execute(f"UPDATE numbers set 'phone_number'='{num}' where 'name'='{name}'")
        else:
            res = execute(f"UPDATE numbers set 'name'='{name}' where 'phone_number'='{num}'")
            if res:
                print(res)

    elif query == 3:
        t = input("From console? (y/n) ")
        if t == 'y':
            name, num = input("Name: "), input("Phone number: ")
            res = execute(
                          f"INSERT INTO numbers(name, phone_number) VALUES('{name}', '{num}')",
                          need_to_commit=True)
        else:
            file = input("Path to file: ")
            res = read_csv(file)
            if res:
                res = execute(
                    (f"INSERT INTO numbers VALUES('{name}','{num}')" for name,num in zip(res)),
                    need_to_commit=True
                )
        if res:
            print(res)
    
    elif query == 4:
        name = input("Name ")
        execute(
                f"DELETE from numbers where name='{name}'",
                need_to_commit=True)
