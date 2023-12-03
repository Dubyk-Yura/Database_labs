from .status_controller import StatusController
from .report_controller import ReportController
from .client_controller import ClientController
from .pet_type_controller import PetTypeController
from .specialists_controller import SpecialistsController
from .procedures_controller import ProceduresController
from .diagnoses_controller import DiagnosesController
from .medicine_controller import MedicineController
from .treatment_schemes_controller import TreatmentSchemesController
from .treatment_controller import TreatmentController
from .services_controller import ServicesController
from .pet_controller import PetController
from .treatment_medicine_controller import TreatmentMedicineController
from .medicine_procedures_schemes_controller import MedicineProceduresSchemesController

status_controller = StatusController()
report_controller = ReportController()
client_controller = ClientController()
pet_type_controller = PetTypeController()
specialists_controller = SpecialistsController()
procedures_controller = ProceduresController()
diagnoses_controller = DiagnosesController()
medicine_controller = MedicineController()
treatment_schemes_controller = TreatmentSchemesController()
treatment_controller = TreatmentController()
services_controller = ServicesController()
pet_controller = PetController()
treatment_medicine_controller = TreatmentMedicineController()
medicine_procedures_schemes_controller = MedicineProceduresSchemesController()
