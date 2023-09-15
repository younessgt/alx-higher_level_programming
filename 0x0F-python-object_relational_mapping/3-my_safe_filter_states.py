#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument (safe from SQL injection)"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
    )
    cur = db.cursor()  # cursor object
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id", (argv[4],))
    res = cur.fetchall()  # retrieving a list of tuples
    for elem in res:
        print(elem)
    cur.close()
    db.close()
