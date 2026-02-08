
from subject import subject

db_connection_string = "postgresql://postgres:8426@localhost:5432/postgres"
db = subject(db_connection_string)


def test_create():
    before_create = db.get_list_of_subjects()
    name = 'test'
    db.create_subject(name)
    after_create = db.get_list_of_subjects()
    db.delete_subject(name)
    assert len(before_create) - len(after_create) == -1

def test_edit():
    name = 'test'
    db.create_subject(name)
    new_name = 'test1'
    db.edit_subject(name, new_name)
    result = db.select_by_name(new_name)
    assert result["subject_title"] == new_name 
    db.delete_subject(new_name)
       

def test_delete():
    before_create = db.get_list_of_subjects()
    name = 'test'
    db.create_subject(name)
    db.delete_subject(name)
    after_delete = db.get_list_of_subjects()
    db.delete_subject(name)
    assert len(before_create) - len(after_delete) == 0




    
    

