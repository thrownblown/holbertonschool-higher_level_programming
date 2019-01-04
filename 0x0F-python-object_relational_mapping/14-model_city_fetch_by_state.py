#!/usr/bin/python3
"""Start link class to table in database """
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1],
            argv[2],
            argv[3]
        ),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(City).join(State).order_by(City.id).all():
        state = session.query(State).filter(State.id == city.state_id).first()
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
