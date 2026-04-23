class LoginUseCase:

    def __init__(self, user_repo, auth_service):
        self.user_repo = user_repo
        self.auth_service = auth_service

    def execute(self, email, password):

        user = self.user_repo.get_by_email(email)

        if not user:
            return {"error": "Usuario no encontrado"}

        if not self.auth_service.verify_password(password, user.password):
            return {"error": "Contraseña incorrecta"}

        token = self.auth_service.create_access_token({"sub": user.email})

        return {"access_token": token}