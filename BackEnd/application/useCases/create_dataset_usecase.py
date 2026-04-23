class CreateDatasetUseCase:

    def __init__(self, dataset_repo):
        self.dataset_repo = dataset_repo

    def execute(self, nombre, ruta):
        return self.dataset_repo.create({
            "nombre": nombre,
            "ruta": ruta
        })