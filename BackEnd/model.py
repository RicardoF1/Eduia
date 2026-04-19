import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def entrenar_modelo():
    data = pd.read_csv("dataset.csv")

    X = data[["horas_estudio", "promedio", "asistencia"]]
    y = data["aprueba"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)

    return {"accuracy": float(acc)}