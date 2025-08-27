# routes.py
from fastapi import APIRouter
from controller import create_generic_routes
from models.user import User
from schemas.user import UserCreate, UserUpdate, UserResponse

api_router = APIRouter()

# User endpoints
user_router = create_generic_routes(User, UserCreate, UserUpdate, UserResponse, "users")

api_router.include_router(user_router, prefix="/users", tags=["Users"])


#from models.product import Product
#from schemas.product import ProductCreate, ProductUpdate, ProductResponse

#product_router = create_generic_routes(Product, ProductCreate, ProductUpdate, ProductResponse, "products")
#api_router.include_router(product_router, prefix="/products", tags=["Products"])
