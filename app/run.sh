#!bin/sh
python app/database.py 
uvicorn api:apps --host 0.0.0.0 --port 80