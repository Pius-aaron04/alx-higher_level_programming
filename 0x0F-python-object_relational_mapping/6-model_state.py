#!/usr/bin/python3

"""Start link class to the table in database
"""

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],sys.argv[2], sys.argv[3], poo_pre_ping=True))
    Base.metadata.create_all(engine)
