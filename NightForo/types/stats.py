from pydantic import BaseModel


class Totals(BaseModel):
    thread: int
    messages: int
    users: int


class LatestUser(BaseModel):
    user_id: int
    username: str
    register_date: int


class Online(BaseModel):
    total: int
    members: int
    guests: int


class StatsResponse(BaseModel):
    totals: Totals
    latest_user: LatestUser
    online: Online
