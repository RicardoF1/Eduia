from fastapi import FastAPI
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

Base.metadata.create_all(bind=engine)

app = FastAPI()

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