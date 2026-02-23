dev:
	poetry run uivorn app.main:app --reload --host 0.0.0.0 --port 8080

prod:
	poerty run gunicorn -k uvicorn.workers.UvicornWorker app.main:app