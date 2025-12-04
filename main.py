from fastapi import FastAPI, HTTPException

app = FastAPI()

# Fake consultants data
consultants = [
    {
        "id": "1",
        "navn": "Anna K.",
        "ferdigheter": ["python", "react"],
        "belastning_prosent": 40
    },
    {
        "id": "2",
        "navn": "Lars M.",
        "ferdigheter": ["java", "spring", "kubernetes"],
        "belastning_prosent": 75
    },
    {
        "id": "3",
        "navn": "Ingrid S.",
        "ferdigheter": ["javascript", "vue", "node.js"],
        "belastning_prosent": 60
    },
    {
        "id": "4",
        "navn": "Erik P.",
        "ferdigheter": ["c#", ".net", "azure"],
        "belastning_prosent": 90
    },
    {
        "id": "5",
        "navn": "Kari H.",
        "ferdigheter": ["python", "django", "postgresql"],
        "belastning_prosent": 55
    },
    {
        "id": "6",
        "navn": "Magnus T.",
        "ferdigheter": ["react", "typescript", "graphql"],
        "belastning_prosent": 30
    },
    {
        "id": "7",
        "navn": "Sofie N.",
        "ferdigheter": ["go", "docker", "microservices"],
        "belastning_prosent": 80
    },
    {
        "id": "8",
        "navn": "Bjørn A.",
        "ferdigheter": ["rust", "webassembly", "systems programming"],
        "belastning_prosent": 45
    },
    {
        "id": "9",
        "navn": "Emma L.",
        "ferdigheter": ["angular", "typescript", "rxjs"],
        "belastning_prosent": 70
    },
    {
        "id": "10",
        "navn": "Ole F.",
        "ferdigheter": ["python", "machine learning", "tensorflow"],
        "belastning_prosent": 50
    }
]

@app.get("/konsulenter")
def get_all_consultants():
    """Get all consultants"""
    return consultants

@app.get("/konsulenter/{consultant_id}")
def get_consultant_by_id(consultant_id: str):
    """Get a specific consultant by ID"""
    for consultant in consultants:
        if consultant["id"] == consultant_id:
            return consultant
    raise HTTPException(status_code=404, detail="Konsulent ikke funnet")