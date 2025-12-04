# Consult AI Server

A FastAPI-based REST API for managing consultant information.

## Running the Docker Container

### Build the image:
```bash
docker build -t consult-ai-server .
```

### Run the container:
```bash
docker run -p 8000:8000 consult-ai-server
```

### Run with hot reload (for development):
```bash
docker run -p 8000:8000 -v $(pwd):/app consult-ai-server
```

The server will be available at `http://localhost:8000`

## API Endpoints

### Get All Consultants
```
GET /konsulenter
```
Returns a list of all consultants with their skills and workload.

### Get Consultant by ID
```
GET /konsulenter/{consultant_id}
```
Returns details for a specific consultant by their ID.

## Example Response
```json
{
  "id": "1",
  "navn": "Anna K.",
  "ferdigheter": ["python", "react"],
  "belastning_prosent": 40
}
```

