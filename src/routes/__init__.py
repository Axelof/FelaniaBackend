from fastapi import APIRouter

from routes import node

routers: tuple["APIRouter"] = (node.router,)
