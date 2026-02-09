from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[3] == "app_users"


def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM company"))
    rows = result.mappings().all()
    row1 = rows[0]
    assert row1["id"] == 1
    assert row1["name"] == "QA Студия 'ТестировщикЪ'"
    connection.close()


def test_select_1_row():
    connection = db.connect()
    sql_statement = text("SELECT * FROM company where id =:company_id")
    result = connection.execute(sql_statement, {"company_id": 1})
    rows = result.mappings().all()
    assert len(rows) == 1
    assert rows[0]["name"] == "QA Студия 'ТестировщикЪ'"

    connection.close()


def test_select_1_row_with_two_filters():
    connection = db.connect()
    sql_statement = text(
        "SELECT * FROM company " 'WHERE "is_active" = :is_active AND id >= :id'
    )
    my_params = {"id": 2, "is_active": True}
    result = connection.execute(sql_statement, my_params)
    rows = result.mappings().all()
    assert len(rows) == 3

    connection.close()


def test_insert():
    connection = db.connect()
    transaction = connection.begin()
    sql = text(
        'INSERT INTO company("name", "is_active") VALUES (:new_name, :is_active)'
    )
    my_params = {"new_name": "Test", "is_active": True}
    rows = connection.execute(sql, my_params)
    transaction.commit()
    connection.close()


def test_updaate():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("UPDATE company SET description = :descr WHERE id = :id")
    my_params = {"descr": "Test1", "id": 6}
    rows = connection.execute(sql, my_params)
    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("delete from company WHERE id = :id")
    my_params = {"id": 6}
    rows = connection.execute(sql, my_params)
    transaction.commit()
    connection.close()
