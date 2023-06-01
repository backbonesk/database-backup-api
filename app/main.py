import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from apscheduler.schedulers.asyncio import AsyncIOScheduler


from .router import router
from .schedules import scheduler_job


logging.basicConfig(level=logging.DEBUG)
logging.getLogger("apscheduler").setLevel(logging.WARNING)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # App Start
    scheduler = AsyncIOScheduler()
    scheduler.add_job(scheduler_job, "interval", minutes=1)
    scheduler.start()
    logging.info("APScheduler started")
    yield
    # App Stop
    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
