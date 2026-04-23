from infrastructure.db.models import Usuario

class MySQLUsuarioRepository:

    def __init__(self, db):
        self.db = db

    def create(self, email, password, rol):
        nuevo = Usuario(
            email=email,
            password=password,
            rol=rol
        )
        self.db.add(nuevo)
        self.db.commit()

    def get_by_email(self, email):
        return self.db.query(Usuario).filter(
            Usuario.email == email
        ).first()