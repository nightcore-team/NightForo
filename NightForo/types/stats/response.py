from pydantic import BaseModel

from . import LatestUser, Online, Totals


class StatsResponse(BaseModel):
    totals: Totals
    latest_user: LatestUser
    online: Online
