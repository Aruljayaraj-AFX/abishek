from fastapi import FastAPI
import uvicorn
from routers.die_push import router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or use the exact frontend origin like ["http://localhost:3000"]
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router,prefix="/codework/v1/dad", tags=["die_push"])



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)