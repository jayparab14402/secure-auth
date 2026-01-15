from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn
import os
from user_routes import sub_router

# load_dotenv()
# env_val = os.environ['X-API-KEY'] 


app = FastAPI(
    title="Secure Auth Application"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=['*']
)

app.include_router(sub_router, prefix="/auth/user")

@app.get("/")
def root():
    return {
        "message": "Hello world"
    }


if __name__=="__main__":
    uvicorn.run("server:app", host='0.0.0.0', port=9876, reload=True)



