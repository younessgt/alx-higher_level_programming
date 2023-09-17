#!/usr/bin/python3
"""script that lists all City objects from the database hbtn_0e_101_usa"""

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
    city = session.query(City).order_by(City.id).all()
    for city_obj in city:
        print(f"{city_obj.id}: {city_obj.name} -> {city_obj.state.name}")
    session.close()
