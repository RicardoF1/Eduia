from infrastructure.db.models import Resultado

class MySQLResultadoRepository:

    def __init__(self, db):
        self.db = db

    def save(self, entrenamiento_id, y_real, y_pred):

        resultado_json = str({
            "y_real": y_real,
            "y_pred": y_pred
        })

        nuevo = Resultado(
            entrenamiento_id=entrenamiento_id,
            resultado_json=resultado_json
        )

        self.db.add(nuevo)
        self.db.commit()