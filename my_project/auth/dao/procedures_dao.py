from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Procedures
from sqlalchemy import text


class ProceduresDAO(GeneralDAO):
    _domain_type = Procedures

    def get_statistics_from_procedures_price(self, stat_type):
        try:
            session = self.get_session()
            sql_expression = text("CALL get_statistics_from_procedures_price_P(:stat_type)")
            result = session.execute(sql_expression, {'stat_type': stat_type}).scalar()
            return result
        except Exception as e:
            print(f"Error getting procedures statistics: {e}")
            return None
