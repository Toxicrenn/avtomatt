from sqlalchemy import create_engine, text

class subject:
    __scripts = {
        "select": text("select * from subject"),
        "new_subject": text("insert into subject (subject_title) values (:name)"),
        "delete_subject": text("delete from subject where subject_title = :name"),
        "edit_subject": text(
            "update subject set subject_title = :new_name where subject_title = :name"
        ),
        "select_subject": text("select * from subject where subject_title = :new_name"),
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_list_of_subjects(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def create_subject(self, name):
        conn = self.__db.connect()
        conn.execute(self.__scripts["new_subject"], {"name": name})
        conn.commit()
        conn.close()

    def delete_subject(self, name):
        conn = self.__db.connect()
        conn.execute(self.__scripts["delete_subject"], {"name": name})
        conn.commit()
        conn.close()

    def edit_subject(self, name, new_name):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["edit_subject"], {"name": name, "new_name": new_name}
        )
        conn.commit()
        conn.close()

    def select_by_name(self, new_name):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select_subject"], {"new_name": new_name})
        rows = result.mappings().first()
        conn.close()
        return dict(rows)
