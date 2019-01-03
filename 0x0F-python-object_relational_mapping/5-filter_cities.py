#!/usr/bin/python3
"""prints all the states in db"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute(
        """
        SELECT cities.name, states.id
        FROM cities, states
        WHERE cities.state_id=states.id
        AND states.name = %s
        ORDER BY id ASC;
        """,
        (argv[4],)
    )

    citis = cur.fetchall()
    print(', '.join([c[0] for c in citis]))
    db.close()
