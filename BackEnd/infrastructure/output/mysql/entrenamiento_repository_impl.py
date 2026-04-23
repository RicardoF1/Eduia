from infrastructure.db.models import Entrenamiento

class MySQLEntrenamientoRepository:

    def __init__(self, db):
        self.db = db

    def save(self, dataset_id, accuracy):
        nuevo = Entrenamiento(
            dataset_id=dataset_id,
            modelo_id=1,
            accuracy=accuracy
        )
        self.db.add(nuevo)
        self.db.commit()
        self.db.refresh(nuevo)
        return nuevo