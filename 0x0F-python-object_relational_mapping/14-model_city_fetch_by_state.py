#!/usr/bin/python3
"""script that prints all City objects from the database hbtn_0e_14_usa"""

if __name__ == "__main__":
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_city import City

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    # creating a Sess class for interactiong with database
    Session_class = sessionmaker(bind=engine)
    # create a session
    session = Session_class()
    # retreive all states ordred by state id
    state = session.query(State.name, City.id, City.name).join(City)
    for elem in state:
        print(f"{elem[0]}: ({elem[1]}) {elem[2]}")
    session.close()
