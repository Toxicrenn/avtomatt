import allure
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable

api = CompanyApi("http://5.101.50.27:8000")
db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")

@allure.id("test -1")
@allure.title("получение списка компаний")
@allure.epic("компании")
@allure.story("получение компаний")
@allure.feature("новое")
@allure.description("запрос организация с параметром актив = тру")
def test_get_companies():
    # Шаг1: получить список компаний через API:
    api_result = api.get_company_list()

    # Шаг2: получить список компаний из БД:
    db_result = db.get_companies()

    # Шаг2: проверить, что списки равны
    assert len(api_result) == len(db_result)

@allure.id("test -2")
@allure.title("создание компании")
def test_add_new():
    body = api.get_company_list()
    len_before = len(body)

    name = "Autotest"
    descr = "Descr"
    result = api.create_company(name, descr)
    new_id = result["id"]

    body = api.get_company_list()
    len_after = len(body)

    db.delete(new_id)

    assert len_after - len_before == 1

    found = False
    for company in body:
        if company["name"] == name:
            found = True
            assert company["description"] == descr
            break

    assert found

@allure.id("test -3")
def test_get_ones_company():
    name = "Skypro"

    # Создаём компанию с is_active=True
    db.create(name, is_active=True)

    max_id = db.get_max_id()

    # Получаем через API
    new_company = api.get_company(max_id)

    # Удаляем
    db.delete(max_id)

    # Проверки
    assert new_company["name"] == name
    assert new_company["is_active"] is True

@allure.id("test -4")
def test_edit():
    name = "Skypro"

    # Создаём компанию с is_active=True
    db.create(name, is_active=True)

    max_id = db.get_max_id()

    new_name = "Updated"
    new_descr = "_upd_"
    edited = api.edit_company(max_id, new_name, new_descr)

    # Удаляем компанию:
    db.delete(max_id)

    assert edited["name"] == new_name
    assert edited["description"] == new_descr

@allure.id("test -5")
def test_delete():
    name = "Skypro"

    # Создаём компанию с is_active=True
    db.create(name, is_active=True)

    max_id = db.get_max_id()

    deleted = api.delete_company(max_id)

    # Удаляем компанию:
    db.delete(max_id)

    assert deleted["company_id"] == max_id
    assert deleted["detail"] == "Компания успешно удалена"

    rows = db.get_company_by_id(max_id)
    assert len(rows) == 0

@allure.id("test -6")
def test_deactivate():
    name = "Skypro"

    # Создаём компанию с is_active=True
    db.create(name, is_active=True)

    max_id = db.get_max_id()

    body = api.set_active_state(max_id, False)

    # Удаляем
    db.delete(max_id)

    assert body["is_active"] is False

@allure.id("test -7")
def test_deactivate_and_activate_back():
    name = "Skypro"

    # Создаём компанию с is_active=True
    db.create(name, is_active=True)

    max_id = db.get_max_id()

    body = api.set_active_state(max_id, False)

    assert body["is_active"] is False

    body = api.set_active_state(max_id, True)

    db.delete(max_id)

    assert body["is_active"] is True
