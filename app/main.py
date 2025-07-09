from fastapi import FastAPI
from .router.github_webhook import router as github_router
from .router.issues import router as issues_router
from dotenv import load_dotenv

load_dotenv(override=True)
app = FastAPI()
app.include_router(github_router)
app.include_router(issues_router)