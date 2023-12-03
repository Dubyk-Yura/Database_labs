from .status_service import StatusService
from .report_service import ReportService
from .client_service import ClientService
from .pet_type_service import PetTypeService
from .specialists_service import SpecialistsService
from .procedures_service import ProceduresService
from .diagnoses_service import DiagnosesService
from .medicine_service import MedicineService
from .treatment_schemes_service import TreatmentSchemesService
from .treatment_service import TreatmentService
from .services_service import ServicesService
from .pet_service import PetService
from .treatment_medicine_service import TreatmentMedicineService
from .medicine_procedures_schemes_service import MedicineProceduresSchemesService

status_service = StatusService()
report_service = ReportService()
client_service = ClientService()
pet_type_service = PetTypeService()
specialists_service = SpecialistsService()
procedures_service = ProceduresService()
diagnoses_service = DiagnosesService()
medicine_service = MedicineService()
treatment_schemes_service = TreatmentSchemesService()
treatment_service = TreatmentService()
services_service = ServicesService()
pet_service = PetService()
treatment_medicine_service = TreatmentMedicineService()
medicine_procedures_schemes_service = MedicineProceduresSchemesService()
