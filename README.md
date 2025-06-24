# Customer API

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
uvicorn app.main:app --reload
```

## Test
```bash
pytest
```

## Docker
```bash
docker build -t vertex-api .
docker run -p 8000:8000 vertex-api
```

## Kubernetes
```bash
kubectl apply -f k8s/
```

## CLI
```bash
python client/cli.py
```