from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from . import models
# from .database import engine
from .routers import social, project, about, contact, skill
# models.Base.metadata.create_all(bind=engine)

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
# app.include_router(post.router)
# app.include_router(user.router)
# app.include_router(auth.router)
app.include_router(social.router)
app.include_router(project.router)
app.include_router(about.router)
app.include_router(contact.router)
app.include_router(skill.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
