from fastapi import APIRouter, Request


router = APIRouter(prefix="/dostavista", tags=["dostavista"])


@router.post("/")
def callback(request: Request):
    print(request)
    return "ok"