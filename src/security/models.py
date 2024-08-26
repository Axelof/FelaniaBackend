from ipaddress import IPv4Address

from pydantic import BaseModel


class JWTBase(BaseModel):
    ip: IPv4Address
