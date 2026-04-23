from infrastructure.db.models import Modelo

class MySQLModeloRepository:

    def __init__(self, db):
        self.db = db

    def create(self, data):
        modelo = Modelo(
            nombre=data["nombre"],
            tipo=data["tipo"],
            ruta=data["ruta"]
        )

        self.db.add(modelo)
        self.db.commit()
        self.db.refresh(modelo)

        return modelo

    def get_by_id(self, model_id):
        return self.db.query(Modelo).filter(Modelo.id == model_id).first()