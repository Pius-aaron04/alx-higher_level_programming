#!/usr/bin/python3
"""prints all City objects by state from database hbtn_0e_14_usa"""

if __name__ == '__main__':
    import sys
    from model_state import State, Base
    from model_city import City
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
    cities = session.query(City).join(State).order_by(City.id)

    for city in cities:
        print('{}: ({}) {}'.format(city.states.name, city.id, city.name))
