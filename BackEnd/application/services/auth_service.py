from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "clave_super_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"])

# 🔑 Hash de contraseña
def hash_password(password: str):
    return pwd_context.hash(password)

# 🔍 Verificar contraseña
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

# 🎟 Crear token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

class AuthService:

    def hash_password(self, password: str):
        return hash_password(password)

    def verify_password(self, plain, hashed):
        return verify_password(plain, hashed)

    def create_access_token(self, data: dict):
        return create_access_token(data)