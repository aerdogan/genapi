# main.py
import uvicorn
from fastapi import FastAPI
from db import init_db
from route import api_router
from fastapi.openapi.utils import get_openapi

def create_app():
    app = FastAPI(title="FastAPI + MongoEngine Example")
    init_db()
    app.include_router(api_router)

    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title=app.title,
            version="1.0.0",
            description="API with MongoEngine and BasicAuth",
            routes=app.routes,
        )
        openapi_schema["components"]["securitySchemes"] = {
            "basicAuth": {
                "type": "http",
                "scheme": "basic"
            }
        }
        
        for path in openapi_schema["paths"].values():
            for method in path.values():
                method.setdefault("security", [{"basicAuth": []}])
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = custom_openapi
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
