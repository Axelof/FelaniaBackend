from fastapi import APIRouter, Depends

from security import jwt

router = APIRouter(dependencies=[Depends(jwt)])


@router.get("/")
async def nodes():
    return "ok"
