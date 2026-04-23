from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from infrastructure.db.session import get_db

from infrastructure.output.mysql.modelo_repository_impl import MySQLModeloRepository
from application.useCases.train_and_save_usecase import TrainAndSaveModelUseCase

router = APIRouter()

@router.post("/train/file")
def train_upload(file: UploadFile = File(...), db: Session = Depends(get_db)):

    use_case = TrainAndSaveModelUseCase(
        modelo_repo=MySQLModeloRepository(db)
    )

    return use_case.execute(file)

