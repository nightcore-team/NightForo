from pydantic import BaseModel


class Option(BaseModel):
    creation_watch_state: str
    interaction_watch_state: str
    content_show_signature: bool
    email_on_conversation: bool
    push_on_conversation: bool
    receive_admin_email: bool
    show_dob_year: bool
    show_dob_date: bool


class Profile(BaseModel):
    location: str
    website: str
    about: str
    signature: str


class Privacy(BaseModel):
    allow_view_profile: str
    allow_post_profile: str
    allow_receive_news_feed: str
    allow_send_personal_conversation: str
    allow_view_identities: str
