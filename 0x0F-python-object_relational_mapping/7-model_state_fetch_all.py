#!/usr/bin/python3

"""Lists all State instnces from the database """

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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print('{}: {}'.format(state.id, state.name))
