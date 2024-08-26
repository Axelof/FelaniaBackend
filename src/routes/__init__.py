from fastapi import APIRouter

from routes import dostavista

routers: tuple["APIRouter", ...] = (dostavista.router,)
