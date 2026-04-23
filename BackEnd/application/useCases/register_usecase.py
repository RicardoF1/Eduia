class RegisterUseCase:

    def __init__(self, user_repo, auth_service):
        self.user_repo = user_repo
        self.auth_service = auth_service

    def execute(self, email, password, rol):

        hashed = self.auth_service.hash_password(password)

        self.user_repo.create(email, hashed, rol)

        return {"mensaje": "Usuario creado"}