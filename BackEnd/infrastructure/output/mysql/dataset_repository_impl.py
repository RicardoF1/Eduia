from domain.ports.dataset_repository import DatasetRepository
from infrastructure.db.models import Dataset as DatasetModel

class MySQLDatasetRepository(DatasetRepository):

    def __init__(self, db):
        self.db = db

    def get_by_id(self, dataset_id: int):
        dataset = self.db.query(DatasetModel).filter(
            DatasetModel.id == dataset_id
        ).first()

        return dataset