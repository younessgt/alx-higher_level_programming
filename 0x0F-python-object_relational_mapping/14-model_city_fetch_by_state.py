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
    state_city = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all()
    for city, state in state_city:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
