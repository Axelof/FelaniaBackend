from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field


class Error(BaseModel):
    code: int = Field(..., description="Error code", ge=400, le=500)
    label: str = Field(..., description="Error label (shortcut)", max_length=12)
    detail: str = Field(..., description="Error detail", max_length=4096)

    def __call__(self):
        return JSONResponse(status_code=self.code, content=self.model_dump(mode="json"))
