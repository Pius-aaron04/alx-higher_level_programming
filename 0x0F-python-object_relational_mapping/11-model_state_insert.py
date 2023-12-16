#!/usr/bin/python3
"""
Adds a new state to the states tables in the database
"""

if __name__ == '__main__':
    import sqlalchemy
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    conn_string = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                              sys.argv[2],
                                                              sys.argv[3])

    engine = create_engine(conn_string, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    # new state object
    new_state = State(name='Louisiana')
    # adds state to the database table
    session.add(new_state)
    session.commit()
    print(new_state.id)
