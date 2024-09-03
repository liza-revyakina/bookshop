from models import Publisher, Book, Stock, Sale


def query_maker(session, decision, publisher_name=None, publisher_id=None):
    if int(decision) == 0:
        subq_book = session.query(Book).join(Publisher.book).filter(Publisher.name == publisher_name).subquery()
    elif int(decision) == 1:
        subq_book = session.query(Book).join(Publisher.book).filter(Publisher.id == publisher_id).subquery()
    else:
        print("Пожалуйста, введите данные")
        subq_book = None
    subq_stock = session.query(Stock).join(subq_book, Stock.id_book == subq_book.c.id).subquery()
    subq_sale = session.query(Sale).join(subq_stock, Sale.id_stock == subq_stock.c.id)

    for s in subq_sale:
        print(f"\n{s.stock.book} | {s.stock.shop} | {s.price} | {s.date_sale}")
