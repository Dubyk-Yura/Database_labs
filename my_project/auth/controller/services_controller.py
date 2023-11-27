from my_project.auth.service import services_service
from my_project.auth.controller.general_controller import GeneralController


class ServicesController(GeneralController):
    _service = services_service

    def get_clients_for_service(self, service_id: int):
        return self._service.get_clients_for_service(service_id)
