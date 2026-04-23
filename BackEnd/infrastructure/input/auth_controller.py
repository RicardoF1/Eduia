from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from infrastructure.db.session import get_db

from application.useCases.login_usecase import LoginUseCase
from application.useCases.register_usecase import RegisterUseCase

from application.services.auth_service import AuthService

from infrastructure.output.mysql.usuario_repository_impl import MySQLUsuarioRepository

from application.schemas.user_schema import UserCreate, UserLogin

from infrastructure.security.jwt_utils import get_current_user
from infrastructure.db.models import Usuario

router = APIRouter()

# Register
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    use_case = RegisterUseCase(
        user_repo=MySQLUsuarioRepository(db),
        auth_service=AuthService()
    )

    return use_case.execute(user.email, user.password, user.rol)


# Login
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    use_case = LoginUseCase(
        user_repo=MySQLUsuarioRepository(db),
        auth_service=AuthService()
    )

    return use_case.execute(user.email, user.password)


#Perfil
@router.get("/perfil")
def perfil(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    usuario = db.query(Usuario).filter(
        Usuario.email == user.get("sub")
    ).first()

    if not usuario:
        return {"error": "Usuario no encontrado"}

    return {
        "email": usuario.email,
        "rol": usuario.rol
    }