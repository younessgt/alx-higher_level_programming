#!/usr/bin/python3
"""script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""

if __name__ == "__main__":
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    # creating a Sess class for interactiong with database
    Session_class = sessionmaker(bind=engine)
    # create a session
    session = Session_class()
    state = session.query(State).order_by(State.id).all()
    for state_obj in state:
        print(f"{state_obj.id}: {state_obj.name}")
        for city_obj in state_obj.cities:
            print(f"\t{city_obj.id}: {city_obj.name}")
    session.close()
