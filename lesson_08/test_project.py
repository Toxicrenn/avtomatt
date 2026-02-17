import requests
import pytest

BASE_URL = "https://yougile.com/api-v2"

LOGIN = 
PASSWORD = 
COMPANY_ID =  

def get_api_token():
    payload = {
        "login": LOGIN,
        "password": PASSWORD,
        "companyId": COMPANY_ID
    }

    response = requests.post(f"{BASE_URL}/auth/keys/get", json=payload)

    assert response.status_code == 200

    keys_list = response.json()

    latest = keys_list[-1]
    token = latest.get("key")

    assert token is not None

    return token


@pytest.fixture(scope="session")
def auth_headers():
    token = get_api_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    return headers

def create_new_project(auth_headers, title = 'hate this lesson'):
    body = {
        'title':title
    }
    response = requests.post(f"{BASE_URL}/projects", json=body, headers=auth_headers)
    return response
    
def test_create_project_positive(auth_headers):
    response = create_new_project(auth_headers, title='test1')
    project_id = response.json()['id']
    assert response.status_code == 201
    
    requests.delete(f"{BASE_URL}/projects/{project_id}", headers=auth_headers)

def test_create_project_negative(auth_headers):
    resp = create_new_project(auth_headers, title='')
    assert resp.status_code == 400

def test_edit_project_positive(auth_headers):
    project_id = create_new_project(auth_headers, title= 'hot dog')
    body_for_edit = {
        'title':'cold dog'
    }
    response = requests.put(f"{BASE_URL}/projects/{project_id}", json=body_for_edit, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()['title'] == 'cold dog'
    
def test_edit_project_negative(auth_headers):
    project_id = create_new_project(auth_headers, title= 'hottest dog in the world')
    body_for_edit = {
        'title':''
    }
    response = requests.put(f"{BASE_URL}/projects/{project_id}", json=body_for_edit, headers=auth_headers)
    assert response.status_code == 400


def test_get_info_project_positive(auth_headers):
    project_id = create_new_project(auth_headers)
    response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=auth_headers)
    assert response.status_code == 200
    
def test_get_info_project_negative(auth_headers):
    project_id = '4f6f0391-0f94-4d30-9b0e-99430a36d4fb'
    response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=auth_headers)
    assert response.status_code == 404
    

