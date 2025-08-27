# routes.py
from fastapi import APIRouter
from controller import create_generic_routes

from models.laptop import Laptop
from schemas.laptop import LaptopBase, LaptopResponse

from models.case import Case
from schemas.case import CaseBase, CaseResponse

from models.user import User
from schemas.user import UserCreate, UserUpdate, UserResponse

api_router = APIRouter()

# User endpoints
user_router = create_generic_routes(User, UserCreate, UserUpdate, UserResponse, "users")
api_router.include_router(user_router, prefix="/users", tags=["Users"])

#laptop
laptop_router = create_generic_routes(Laptop, LaptopBase, LaptopBase, LaptopResponse, "laptops")
api_router.include_router(laptop_router, prefix="/laptops", tags=["Laptops"])

# case
case_router = create_generic_routes(Case, CaseBase, CaseBase, CaseResponse, "cases")
api_router.include_router(case_router, prefix="/cases", tags=["Cases"])
