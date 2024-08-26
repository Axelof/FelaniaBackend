from settings import settings

config = {
    "connections": {
        "default": f"postgres://{settings.database.user}:{settings.database.password}@database:5432/{settings.database.db}"
    },
    "apps": {
        "models": {
            "models": ["database.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}
