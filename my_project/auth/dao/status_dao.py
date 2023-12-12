from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Status
from sqlalchemy import text


class StatusDAO(GeneralDAO):
    _domain_type = Status

    def convert_rows_in_databases(self):
        try:
            session = self.get_session()
            sql_expression = text("CALL convert_rows_in_databases()")
            session.execute(sql_expression)
            session.commit()
        except Exception as e:
            print(f"Error in converting rows in databases: {e}")
