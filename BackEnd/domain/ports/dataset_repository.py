from abc import ABC, abstractmethod

class DatasetRepository(ABC):

    @abstractmethod
    def get_by_id(self, dataset_id: int):
        pass