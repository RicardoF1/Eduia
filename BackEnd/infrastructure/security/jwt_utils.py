from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError

security = HTTPBearer()

SECRET_KEY = "clave_super_secreta"
ALGORITHM = "HS256"

def get_current_user(token=Depends(security)):
    try:
        payload = jwt.decode(
            token.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload  # aquí viene {"sub": email, "rol": ...}

    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")