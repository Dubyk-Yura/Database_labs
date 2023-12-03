from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)

    from .status_route import status_bp
    from .report_route import report_bp
    from .client_route import client_bp
    from .pet_type_route import pet_type_bp
    from .specialists_route import specialists_bp
    from .procedures_route import procedures_bp
    from .diagnoses_route import diagnoses_bp
    from .medicine_route import medicine_bp
    from .treatment_schemes_route import treatment_schemes_bp
    from .treatment_route import treatment_bp
    from .services_route import services_bp
    from .pet_route import pet_bp
    from .treatment_medicine_route import treatment_medicine_bp
    from .medicine_procedures_schemes_route import medicine_procedures_schemes_bp

    app.register_blueprint(status_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint( pet_type_bp)
    app.register_blueprint(specialists_bp)
    app.register_blueprint(procedures_bp)
    app.register_blueprint(diagnoses_bp)
    app.register_blueprint(medicine_bp)
    app.register_blueprint(treatment_schemes_bp)
    app.register_blueprint(treatment_bp)
    app.register_blueprint(services_bp)
    app.register_blueprint(pet_bp)
    app.register_blueprint(treatment_medicine_bp)
    app.register_blueprint(medicine_procedures_schemes_bp)

