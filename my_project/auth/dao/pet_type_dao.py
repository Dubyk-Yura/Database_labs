from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import PetType
from sqlalchemy import text


class PetTypeDAO(GeneralDAO):
    _domain_type = PetType

    def insert_ten_rows_into_pet_type(self):
        try:
            session = self.get_session()
            sql_expression = text("CALL insert_ten_rows_into_pet_type()")
            session.execute(sql_expression)
            session.commit()
        except Exception as e:
            print(f"Error inserting ten rows in pet type: {e}")

    def insert_in_pet_type(self, new_type: str):
        try:
            session = self.get_session()
            sql_expression = text("CALL insert_in_pet_type(:new_type)")
            session.execute(sql_expression,{'new_type':new_type})
            session.commit()
        except Exception as e:
            print(f"Error inserting in pet type: {e}")
