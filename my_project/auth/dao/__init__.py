from .status_dao import StatusDAO
from .report_dao import ReportDAO
from .client_dao import ClientDAO
from .pet_type_dao import PetTypeDAO
from .specialists_dao import SpecialistsDAO
from .procedures_dao import ProceduresDAO
from .diagnoses_dao import DiagnosesDAO
from .medicine_dao import MedicineDAO
from .treatment_schemes_dao import TreatmentSchemesDAO
from .treatment_dao import TreatmentDAO
from .services_dao import ServicesDAO
from .pet_dao import PetDAO
from .treatment_medicine_dao import TreatmentMedicineDAO
from .medicine_procedures_schemes_dao import MedicineProceduresSchemesDAO

status_dao = StatusDAO()
report_dao = ReportDAO()
client_dao = ClientDAO()
pet_type_dao = PetTypeDAO()
specialists_dao = SpecialistsDAO()
procedures_dao = ProceduresDAO()
diagnoses_dao = DiagnosesDAO()
medicine_dao = MedicineDAO()
treatment_schemes_dao = TreatmentSchemesDAO()
treatment_dao = TreatmentDAO()
services_dao = ServicesDAO()
pet_dao = PetDAO()
treatment_medicine_dao = TreatmentMedicineDAO()
medicine_procedures_schemes_dao = MedicineProceduresSchemesDAO()
