import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression

class TrainCustomUseCase:

    def execute(self, ruta, modelo, test_size):

        df = pd.read_csv(ruta)

        X = df[["horas_estudio", "asistencia"]]
        y = df["nota"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size
        )

        if modelo == "linear":
            model = LinearRegression()
        else:
            model = LogisticRegression()

        model.fit(X_train, y_train)

        acc = model.score(X_test, y_test)

        return {
            "accuracy": acc
        }