import hashlib 
from fastapi import Depends, FastAPI
import logging
from sqlalchemy.orm import Session
import secrets

from database import db
from crud import write_access_data


app = FastAPI()


@app.get("/")
async def root():
    """ Root API """
    logging.info("Hello World")
    return {"message": "Hello World"}

@app.post("/access")
async def access(user_id: str, channel_id: str, access_db: Session = Depends(db.get_session)):
    """Access API"""
    logging.info("Access API")
    # make Access_Data
    # generate salt for randomness
    salt = secrets.token_hex(16)
    access_id_raw = user_id + channel_id  + salt
    # hash access_id with salt
    access_id = hashlib.sha256(access_id_raw.encode('utf-8')).hexdigest()
    return write_access_data(access_id, user_id, channel_id, access_db)