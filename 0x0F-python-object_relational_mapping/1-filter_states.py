#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa
that begin with 'N' """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
    )
    cur = db.cursor()  # cursor object
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    res = cur.fetchall()  # retrieving a list of tuples
    for elem in res:
        print(elem)
    cur.close()
    db.close()
