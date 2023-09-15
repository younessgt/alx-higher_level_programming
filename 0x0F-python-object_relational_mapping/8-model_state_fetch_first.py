#!/usr/bin/python3
"""  script that prints the first State object from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    # creating a Sess class for interactiong with database
    Session_class = sessionmaker(bind=engine)
    # create a session
    session = Session_class()
    # retreive all states ordred by state id
    first_state = session.query(State).order_by(State.id).first()
    print(f"{first_state.id}: {first_state.name}")

    session.close()
