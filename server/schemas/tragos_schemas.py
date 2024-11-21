from datetime import datetime

from pydantic import BaseModel


class NuevoTragoRequest(BaseModel):
    title: str
    status: str = 'Nuevo'
    description: str = ''


class TragoRequest(BaseModel):
    title: str = None
    status: str = None
    description: str = None


class TragoResponse(BaseModel):
    id: int
    title: str
    status: str = 'Nuevo'
    description: str = ''
    created_at: datetime
    update_at: datetime
