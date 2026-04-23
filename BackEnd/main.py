from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from infrastructure.input.auth_controller import router as auth_router
from infrastructure.input.dataset_controller import router as dataset_router
from infrastructure.input.model_controller import router as model_router

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(auth_router)
app.include_router(dataset_router)
app.include_router(model_router)

@app.get("/")
def root():
    return {"mensaje": "API funcionando"}




""" from fastapi import FastAPI
from model import entrenar_modelo

from database import engine
from models import Base

from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario
from auth import hash_password
from auth import verify_password, create_access_token

#Proteccion rutas co libreria JwT
from fastapi.security import HTTPBearer
from fastapi import Depends
from jose import jwt, JWTError

from schemas import UserCreate
from schemas import UserLogin

from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
from models import Dataset, Entrenamiento, Resultado
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression



Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}

@app.post("/train")
def train():
    resultado = entrenar_modelo()
    return resultado



# dependencia para BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Proteger rutas con JWT
security = HTTPBearer()
SECRET_KEY = "clave_super_secreta"
ALGORITHM = "HS256"

def verificar_token(token=Depends(security)):
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return {"error": "Token inválido"}

# Proteger endpoint con JWT
@app.get("/perfil")
def perfil(user=Depends(verificar_token)):
    return {"usuario": user}

# EndPoint para registrar usuario
@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    hashed_password = hash_password(user.password)

    nuevo_usuario = Usuario(
        email=user.email,
        password=hashed_password,
        rol=user.rol
    )

    db.add(nuevo_usuario)
    db.commit()

    return {"mensaje": "Usuario creado"}


#EndPoint loguearse 
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    usuario = db.query(Usuario).filter(Usuario.email == user.email).first()

    if not usuario:
        return {"error": "Usuario no encontrado"}

    if not verify_password(user.password, usuario.password):
        return {"error": "Contraseña incorrecta"}

    token = create_access_token({"sub": usuario.email})

    return {"access_token": token}


#Endpoint dataset
@app.post("/train/{dataset_id}")
def train_model(dataset_id: int, db: Session = Depends(get_db)):

    # 1. buscar dataset en BD
    dataset = db.query(Dataset).filter(Dataset.id == dataset_id).first()

    if not dataset:
        return {"error": "Dataset no encontrado"}

    # 2. leer CSV
    df = pd.read_csv(dataset.ruta)

    # 3. preparar datos
    X = df[["horas_estudio", "asistencia"]]
    y = df["nota"]

    # 4. dividir
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2
    )

    # 5. modelo
    model = LinearRegression()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    # 6. guardar entrenamiento
    nuevo_entrenamiento = Entrenamiento(
        dataset_id=dataset_id,
        modelo_id=1,
        accuracy=accuracy
    )

    db.add(nuevo_entrenamiento)
    db.commit()
    db.refresh(nuevo_entrenamiento)

    # 7. predicciones
    y_pred = model.predict(X_test).tolist()
    y_real = y_test.tolist()

    resultado_json = str({
        "y_real": y_real,
        "y_pred": y_pred
    })

    # 8. guardar resultados
    nuevo_resultado = Resultado(
        entrenamiento_id=nuevo_entrenamiento.id,
        resultado_json=resultado_json
    )

    db.add(nuevo_resultado)
    db.commit()

    return {
        "accuracy": accuracy,
        "entrenamiento_id": nuevo_entrenamiento.id
    }


#ver resultados
@app.get("/resultados/{id}")
def get_resultados(id: int, db: Session = Depends(get_db)):

    resultado = db.query(Resultado).filter(
        Resultado.entrenamiento_id == id
    ).first()

    return resultado """