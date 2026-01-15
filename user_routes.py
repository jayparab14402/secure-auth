from routes.login_routes.user_routes import get_user
from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session
from database import db_session
import traceback



sub_router = APIRouter()
@sub_router.get("/get_client_records", name="user table records")
def get_records_router(
    request: Request,
    session_user: Session = Depends(db_session)):
    try:
        req_json = request.query_params
        get_res = get_user(req_json, session_user)
        return JSONResponse(f"{get_res}")
    except Exception as e:
        print(f"Error in get_client_records api {traceback.format_exc()}")
        return JSONResponse(status_code=400, content={"message": "Invalid Request"})