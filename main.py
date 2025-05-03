from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def health_check():
    # Get the current date and time
    current_datetime = datetime.now()
    
    # Return the current date and time as a string
    return {"message": "Happy", "current_datetime": current_datetime.strftime("%Y-%m-%d %H:%M:%S")}
