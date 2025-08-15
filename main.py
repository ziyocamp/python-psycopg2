from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from models import User, Address


engine = create_engine('postgresql+psycopg2://djumanov:Djcoder1120@localhost/test', echo=True)

Session = sessionmaker(bind=engine)

user = User(
    id=2,
    name='Ali',
    fullname = 'Ali Valiyev'
)

s = Session()
s.add(user)
s.commit()
s.close()

