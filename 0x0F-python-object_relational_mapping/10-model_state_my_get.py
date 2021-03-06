#!/usr/bin/python3
"""Start link class to table in database """
from sys import argv
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1],
            argv[2],
            argv[3]
        ),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        state = session.query(State).filter_by(
            name=argv[4]
        ).first()
        print(state.id)
    except:
        print("Not found")
    session.close()
