from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


class JWT(HTTPBearer):
    ISSUER = "WGMaster"
    SUBJECT = "WGM (API)"

    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, _: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(_)

        return credentials.credentials
