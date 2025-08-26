# repository.py
from typing import Type, TypeVar, Generic, List
from mongoengine import Document

T = TypeVar("T", bound=Document)

class Repository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    def get_all(self) -> List[T]:
        return list(self.model.objects)

    def get_by_id(self, id: str) -> T | None:
        return self.model.objects(id=id).first()

    def create(self, **data) -> T:
        obj = self.model(**data)
        obj.save()
        return obj

    def update(self, id: str, **data) -> T | None:
        obj = self.model.objects(id=id).first()
        if not obj:
            return None
        obj.update(**{"set__" + k: v for k, v in data.items()})
        obj.reload()
        return obj

    def delete(self, id: str) -> bool:
        obj = self.model.objects(id=id).first()
        if obj:
            obj.delete()
            return True
        return False
