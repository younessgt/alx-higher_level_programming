#!/usr/bin/python3
""" script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa """


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
    state_a = (
        session.query(State)
        .order_by(State.id)
        .filter(State.name.like("%a%"))
        .all()
    )
    for state in state_a:
        print(f"{state.id}: {state.name}")
    session.close()
