from fastapi import FastAPI
import json

app = FastAPI()

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
