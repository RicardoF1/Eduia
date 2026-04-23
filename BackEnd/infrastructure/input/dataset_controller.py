from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from infrastructure.db.session import get_db


from application.useCases.train_model_usecase import TrainModelUseCase
from application.services.ml_service import MLService

from infrastructure.output.mysql.dataset_repository_impl import MySQLDatasetRepository
from infrastructure.output.mysql.entrenamiento_repository_impl import MySQLEntrenamientoRepository
from infrastructure.output.mysql.resultado_repository_impl import MySQLResultadoRepository

from application.useCases.create_dataset_usecase import CreateDatasetUseCase
from fastapi import UploadFile, File


router = APIRouter()

#Labo normal
@router.post("/train/by-dataset/{dataset_id}")
def train_model(dataset_id: int, db: Session = Depends(get_db)):

    use_case = TrainModelUseCase(
        dataset_repo=MySQLDatasetRepository(db),
        entrenamiento_repo=MySQLEntrenamientoRepository(db),
        resultado_repo=MySQLResultadoRepository(db),
        ml_service=MLService()
    )

    return use_case.execute(dataset_id)

#Labo Interectivo
@router.post("/train/custom")
def train_custom(ruta: str, modelo: str, test_size: float):

    use_case = TrainCustomUseCase()

    return use_case.execute(ruta, modelo, test_size)


