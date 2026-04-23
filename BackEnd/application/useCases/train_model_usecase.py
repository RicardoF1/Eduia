import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class TrainModelUseCase:

    def __init__(self, dataset_repo, entrenamiento_repo, resultado_repo, ml_service):
        self.dataset_repo = dataset_repo
        self.entrenamiento_repo = entrenamiento_repo
        self.resultado_repo = resultado_repo
        self.ml_service = ml_service

    def execute(self, dataset_id: int):

        dataset = self.dataset_repo.get_by_id(dataset_id)

        if not dataset:
            return {"error": "Dataset no encontrado"}

        accuracy, X_test, y_test, model = self.ml_service.train(dataset.ruta)

        entrenamiento = self.entrenamiento_repo.save(dataset_id, accuracy)

        y_pred = model.predict(X_test).tolist()
        y_real = y_test.tolist()

        self.resultado_repo.save(entrenamiento.id, y_real, y_pred)

        return {
            "accuracy": accuracy,
            "entrenamiento_id": entrenamiento.id
        }