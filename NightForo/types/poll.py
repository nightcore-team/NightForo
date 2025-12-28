from typing import List
from pydantic import BaseModel


class Response(BaseModel):
    text: str
    vote_count: int
    voted_for_each: bool


class Poll(BaseModel):
    can_vote: bool
    has_voted: bool
    responses: List[
        Response
    ]  # List of possible responses with text, vote count (if visible) and whether the API user has voted for each
    poll_id: int
    question: str
    voter_count: int
    public_votes: bool
    max_votes: int
    close_date: int
    change_vote: bool
    view_results_unvoted: bool
