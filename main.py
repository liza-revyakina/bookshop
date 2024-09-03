import sqlalchemy
from sqlalchemy.orm import sessionmaker
from config import LOGIN, PASSWORD
from models import create_tables, Publisher, Shop, Book, Stock, Sale
from json_data import data_test
from query import query_maker


DSN = f'postgresql://{LOGIN}:{PASSWORD}@localhost:5432/bookshop'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

for record in data_test:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()

decision = input("Введите 0 для поиска по названию\nВведите 1 для поиска по индексу: \n")
if int(decision) == 0:
    publisher_name = input("Введите название издателя: \n")
    publisher_id = None
elif int(decision) == 1:
    publisher_id = input("Введите индекс издателя: \n")
    publisher_name = None
else:
    print("Пожалуйста, введите корректную информацию")
    publisher_id = None
    publisher_name = None

query_maker(session, decision, publisher_name, publisher_id)

session.close()
