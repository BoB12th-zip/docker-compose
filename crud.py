from sqlalchemy.orm import Session
from datetime import datetime, timedelta


import models


def write_access_data(access_id: str, user_id: str, channel_id: str, db: Session):
    query_result = db.query(models.Access_Table).filter(models.Access_Table.access_id == access_id).first()

    if query_result is None:
        # Homework: write access data to database fill all column
        access_time = datetime.now()
        korea_time_difference = timedelta(hours=9)
        access_time = access_time + korea_time_difference
        # Create a new Access_Table object and fill its attributes
        access_data = models.Access_Table(
            access_id=access_id,
            user_id=user_id,
            channel_id = channel_id,
            access_time=access_time
        )

        # Add the new_access object to the session and commit the changes
        db.add(access_data)
        db.commit()
        message = f"Access Data.. user id : {user_id}, access time : {access_time}"
        return {"message": message, 'result': True}
    else:
        return {"message": "already access id", 'result': False}