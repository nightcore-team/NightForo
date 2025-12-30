from pydantic import BaseModel

from . import Totals, LatestUser, Online


class StatsResponse(BaseModel):
    totals: Totals
    latest_user: LatestUser
    online: Online
