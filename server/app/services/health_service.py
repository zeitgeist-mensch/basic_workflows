from app.repositories.base_repository import BaseRepository


class HealthService:
    def __init__(self, repo: BaseRepository):
        self.repo = repo

    def get_health(self):
        return {
            "status": "ok",
            "db_connected": self.repo.health_check(),
        }
