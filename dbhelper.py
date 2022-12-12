from mysql.connector import connect

db = connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='student_database'
)
def query(sql: str)->list:
    cursor: object = db.cursor(dictionary=True)
    cursor.execute(sql)
    rows: list=cursor.fetchall()
    db.commit()
    cursor.close()
    return rows
    
def getallrecord(table: str)->list:
    sql: str = f"SELECT * FROM `{table}`"
    cursor: object = db.cursor(dictionary=True)
    cursor.execute(sql)
    rows: list = cursor.fetchall()
    return rows

def getrecord(table: str, **kwargs)->dict:
    keys: list = list(kwargs.keys())
    values: list = list(kwargs.values())
    sql: str = f"SELECT * FROM `{table}` WHERE `{keys[0]}`='{values[0]}'"
    cursor: object = db.cursor(dictionary=True)
    cursor.execute(sql)
    rows: dict = cursor.fetchone()
    cursor.close()
    return rows

def deleterecord(table: str, **kwargs)->bool:
    keys: list = list(kwargs.keys())
    values: list = list(kwargs.values())
    sql: str = f"DELETE FROM `{table}` WHERE `{keys[0]}`='{values[0]}'"
    cursor: object = db.cursor()
    cursor.execute(sql)
    rows_affected= cursor.rowcount
    db.commit()
    cursor.close()
    okey: bool = False
    if rows_affected>0:
        okey = True
    return okey

def addrecord(table: str, **kwargs)->bool:
    keys: list = list(kwargs.keys())
    values: list = list(kwargs.values())
    flds: str = "`,`".join(keys)
    data: str = "','".join(values)
    sql: str = f"INSERT INTO `{table}`(`{flds}`) VALUES ('{data}')"
    cursor: object = db.cursor()
    cursor.execute(sql)
    rows_affected= cursor.rowcount
    db.commit()
    cursor.close()
    okey: bool = False
    if rows_affected>0:
        okey = True
    return okey


def updaterecord(table: str, **kwargs)->bool:
    keys: list = list(kwargs.keys())
    values: list = list(kwargs.values())
    flds: list = list()
    for i in range(1, len(keys)):
        flds.append("`"+keys[i]+"`='"+values[i]+"'")
    fld: str =",".join(flds)
    sql: str = f"UPDATE `{table}` SET {fld} WHERE `{keys[0]}`='{values[0]}'"
    cursor: object = db.cursor()
    cursor.execute(sql)
    rows_affected= cursor.rowcount
    db.commit()
    cursor.close()
    okey: bool = False
    if rows_affected>0:
        okey = True
    return okey

def userlogin(table: str, **kwargs)->list:
    keys: list = list(kwargs.keys())
    values: list = list(kwargs.values())
    sql: str = f"SELECT * FROM `{table}` WHERE `{keys[0]}`='{values[0]}' AND `{keys[1]}`='{values[1]}'"
    cursor: object = db.cursor(dictionary=True)
    cursor.execute(sql)
    rows: dict = cursor.fetchone()
    cursor.close()
    return rows

user: dict = userlogin('users',username='admin',password='')
print(user)
