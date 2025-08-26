# controller.py
from fastapi import APIRouter, HTTPException, Depends
from typing import Type
from repository import Repository
from auth import get_current_user

def create_generic_routes(
    model: Type,
    schema_create: Type,
    schema_update: Type,
    schema_response: Type,
    prefix: str
) -> APIRouter:
    """
    Belirtilen model için CRUD endpointlerini döndürür.
    """
    router = APIRouter()
    repo = Repository(model)

    @router.get("/GetAll", response_model=list[schema_response])
    def get_all(user: str = Depends(get_current_user)):
        return [schema_response(**obj.to_mongo().to_dict(), id=str(obj.id)) for obj in repo.get_all()]

    @router.post("/Create", response_model=schema_response)
    def create(item: schema_create, user: str = Depends(get_current_user)):
        obj = repo.create(**item.dict())
        return schema_response(**obj.to_mongo().to_dict(), id=str(obj.id))

    @router.get("/Get/{id}", response_model=schema_response)
    def get_by_id(id: str, user: str = Depends(get_current_user)):
        obj = repo.get_by_id(id)
        if not obj:
            raise HTTPException(status_code=404, detail="Not found")
        return schema_response(**obj.to_mongo().to_dict(), id=str(obj.id))

    @router.put("/Update/{id}", response_model=schema_response)
    def update(id: str, item: schema_update, user: str = Depends(get_current_user)):
        obj = repo.update(id, **item.dict(exclude_unset=True))
        if not obj:
            raise HTTPException(status_code=404, detail="Not found")
        return schema_response(**obj.to_mongo().to_dict(), id=str(obj.id))

    @router.delete("/Delete/{id}")
    def delete(id: str, user: str = Depends(get_current_user)):
        if repo.delete(id):
            return {"detail": "Deleted"}
        raise HTTPException(status_code=404, detail="Not found")

    return router
