from fastapi import APIRouter, Depends
from app.services.health_service import HealthService
from app.repositories.base_repository import BaseRepository

router = APIRouter()


def get_health_service():
    repo = BaseRepository()
    return HealthService(repo)


@router.get("/health")
async def health(service: HealthService = Depends(get_health_service)):
    return service.get_health()
