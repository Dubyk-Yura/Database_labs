from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import services_dao


class ServicesService(GeneralService):
    _dao = services_dao

    def get_clients_for_service(self, service_id: int):
        return self._dao.get_clients_for_service(service_id)

