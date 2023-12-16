#!/usr/bin/python3

""" lists the first state object."""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    import sqlalchemy
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    conn_string = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                              sys.argv[2],
                                                              sys.argv[3])
    engine = create_engine(conn_string, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).\
        filter(State.name.like('%a%'))
    for state in states:
        print('{}: {}'.format(state.id, state.name))
