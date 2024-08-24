import logging
from functools import partial

from fastapi import FastAPI
from tortoise import Tortoise, connections

from database.config import config
from database.migrations import run_migration
from routes import routers
from settings import settings
from utils.logger import configure_logging

configure_logging()

app = FastAPI(
    debug=settings.debug,
    on_startup=[
        run_migration,
        partial(Tortoise.init, config=config),
        Tortoise.generate_schemas,
    ],
    on_shutdown=[connections.close_all],
)

for router in routers:
    app.include_router(router)

if settings.debug:
    logging.info("server running in debug mode")
