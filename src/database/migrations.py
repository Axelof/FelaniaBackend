import contextlib

from aerich import Command
from loguru import logger

from database.config import config
from definitions import project_directory

migrations_directory = project_directory / "migrations"


async def run_migration():
    command = Command(tortoise_config=config, location=migrations_directory)
    logger.info("Run database migration...")
    await command.init()
    with contextlib.suppress(FileExistsError):
        await command.init_db(safe=True)
    try:
        await command.migrate()
        await command.upgrade(run_in_transaction=True)
        logger.info("Database successfully upgraded")
    except BaseException as e:
        logger.error(f"Database failed to upgrade: {e}")
