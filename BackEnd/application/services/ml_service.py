import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class MLService:

    def train(self, ruta_csv):

        df = pd.read_csv(ruta_csv)

        X = df[["horas_estudio", "asistencia"]]
        y = df["nota"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2
        )

        model = LinearRegression()
        model.fit(X_train, y_train)

        accuracy = model.score(X_test, y_test)

        return accuracy, X_test, y_test, model