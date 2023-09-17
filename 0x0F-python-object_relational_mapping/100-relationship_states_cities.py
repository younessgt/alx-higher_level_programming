#!/usr/bin/python3
"""script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa"""

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
    california = State(name="California")
    san_Fran = City(name="San Francisco")
    # cities is an attribute of California object
    california.cities.append(san_Fran)
    session.add(california)
    session.commit()
    session.close()
