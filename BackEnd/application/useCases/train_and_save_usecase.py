import pandas as pd
import joblib
import uuid
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class TrainAndSaveModelUseCase:

    def __init__(self, modelo_repo):
        self.modelo_repo = modelo_repo

    def execute(self, file):

        # 🔹 Leer CSV
        try:
            df = pd.read_csv(file.file)
        except Exception as e:
            return {"error": f"Error al leer CSV: {str(e)}"}

        # 🔹 Validar columnas necesarias
        required_columns = ["horas_estudio", "asistencia", "nota"]

        for col in required_columns:
            if col not in df.columns:
                return {"error": f"Falta la columna: {col}"}

        # 🔹 Preparar datos
        X = df[["horas_estudio", "asistencia"]]
        y = df["nota"]

        # 🔹 Dividir datos
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2
        )

        # 🔹 Modelo
        model = LinearRegression()

        try:
            model.fit(X_train, y_train)
        except Exception as e:
            return {"error": f"Error al entrenar modelo: {str(e)}"}

        # 🔹 Evaluación
        accuracy = model.score(X_test, y_test)

        # 🔹 Predicciones (OPCIONAL)
        try:
            y_pred = model.predict(X_test).tolist()
            y_real = y_test.tolist()
        except Exception as e:
            return {"error": f"Error en predicción: {str(e)}"}

        # 🔹 Crear carpeta si no existe
        os.makedirs("models", exist_ok=True)

        # 🔹 Guardar modelo en disco
        model_uuid = str(uuid.uuid4())
        path = f"models/{model_uuid}.pkl"

        try:
            joblib.dump(model, path)
        except Exception as e:
            return {"error": f"Error al guardar modelo: {str(e)}"}

        # 🔹 Guardar en BD
        try:
            modelo = self.modelo_repo.create({
                "nombre": "modelo_entrenado",
                "tipo": "linear",
                "ruta": path
            })
        except Exception as e:
            return {"error": f"Error al guardar en BD: {str(e)}"}

        # 🔥 RESPUESTA FINAL COMPLETA
        return {
            "model_id": modelo.id,
            "accuracy": float(accuracy),
            "y_real": y_real,
            "y_pred": y_pred
        }