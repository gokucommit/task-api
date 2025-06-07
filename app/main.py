from fastapi import FastAPI
from app.api.v1.routes import router as task_router
from app.db.session import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task tracker API")
app.include_router(task_router, prefix="/api/v1")