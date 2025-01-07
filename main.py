from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Define allowed origins for CORS
origins = [
    "*",  # Allow all origins, change to specific origins if necessary
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load user data from a file
with open("user_list.json", "r") as file:
    users = json.load(file)

@app.get("/api/search_users/")
async def search_users(q: str = ""):
    filtered_users = [
        user for user in users
        if q.lower() in user["first_name"].lower() or q.lower() in user["last_name"].lower()
    ]
    if not filtered_users:
        return {"message": "No results found", "results": []}
    return {"results": filtered_users}
