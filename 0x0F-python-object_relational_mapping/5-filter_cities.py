#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
    )
    cur = db.cursor()  # cursor object
    sql_query = """
    SELECT cities.name
    FROM cities WHERE cities.state_id = (SELECT id FROM states WHERE
    name = %s)
    """
    cur.execute(sql_query, (argv[4],))
    res = cur.fetchall()  # retrieving a list of tuples
    print(", ".join(elem[0] for elem in res))
    cur.close()
    db.close()
