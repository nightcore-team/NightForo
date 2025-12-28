from typing import Final

from .endpoint import create_endpoint, HTTPMethod

ENDPOINT_API: Final[str] = "https://forum.arzguard.com/api"

# ============================================================================
# ALERTS
# ============================================================================

endpoint_alerts = create_endpoint(
    ENDPOINT_API + "/alerts",
    HTTPMethod.GET,
    HTTPMethod.POST,
)

endpoint_alerts_mark_all = create_endpoint(
    ENDPOINT_API + "/alerts/mark-all",
    HTTPMethod.POST,
)


def endpoint_alert(alert_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/alerts/{alert_id}",
        HTTPMethod.GET,
    )


def endpoint_alert_mark(alert_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/alerts/{alert_id}/mark",
        HTTPMethod.POST,
    )


# ============================================================================
# ATTACHMENTS
# ============================================================================

endpoint_attachments = create_endpoint(
    ENDPOINT_API + "/attachments",
    HTTPMethod.GET,
    HTTPMethod.POST,
)

endpoint_attachments_new_key = create_endpoint(
    ENDPOINT_API + "/attachments/new-key",
    HTTPMethod.POST,
)


def endpoint_attachment(attachment_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/attachments/{attachment_id}",
        HTTPMethod.GET,
        HTTPMethod.DELETE,
    )


def endpoint_attachment_data(attachment_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/attachments/{attachment_id}/data",
        HTTPMethod.GET,
    )


def endpoint_attachment_thumbnail(attachment_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/attachments/{attachment_id}/thumbnail",
        HTTPMethod.GET,
    )


# ============================================================================
# AUTH
# ============================================================================

endpoint_auth = create_endpoint(
    ENDPOINT_API + "/auth",
    HTTPMethod.POST,
)

endpoint_auth_from_session = create_endpoint(
    ENDPOINT_API + "/auth/from-session",
    HTTPMethod.POST,
)

endpoint_auth_login_token = create_endpoint(
    ENDPOINT_API + "/auth/login-token",
    HTTPMethod.POST,
)


# ============================================================================
# CONVERSATION MESSAGES
# ============================================================================

endpoint_conversation_messages = create_endpoint(
    ENDPOINT_API + "/conversation-messages",
    HTTPMethod.POST,
)


def endpoint_conversation_message(message_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/conversation-messages/{message_id}",
        HTTPMethod.GET,
        HTTPMethod.POST,
    )


def endpoint_conversation_message_react(message_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/conversation-messages/{message_id}/react",
        HTTPMethod.POST,
    )


# ============================================================================
# CONVERSATIONS
# ============================================================================

endpoint_conversations = create_endpoint(
    ENDPOINT_API + "/conversations",
    HTTPMethod.GET,
    HTTPMethod.POST,
)


def endpoint_conversation(conversation_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/conversations/{conversation_id}",
        HTTPMethod.GET,
        HTTPMethod.POST,
        HTTPMethod.DELETE,
    )


def endpoint_conversation_invite(conversation_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/conversations/{conversation_id}/invite",
        HTTPMethod.POST,
    )


def endpoint_conversation_mark_read(conversation_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/conversations/{conversation_id}/mark-read",
        HTTPMethod.POST,
    )


def endpoint_conversation_mark_unread(conversation_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/conversations/{conversation_id}/mark-unread",
        HTTPMethod.POST,
    )


def endpoint_conversation_messages_list(conversation_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/conversations/{conversation_id}/messages",
        HTTPMethod.GET,
    )


def endpoint_conversation_star(conversation_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/conversations/{conversation_id}/star",
        HTTPMethod.POST,
    )


# ============================================================================
# FORUMS
# ============================================================================


def endpoint_forum(forum_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/forums/{forum_id}",
        HTTPMethod.GET,
    )


def endpoint_forum_mark_read(forum_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/forums/{forum_id}/mark-read",
        HTTPMethod.POST,
    )


def endpoint_forum_threads(forum_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/forums/{forum_id}/threads",
        HTTPMethod.GET,
    )


# ============================================================================
# INDEX
# ============================================================================

endpoint_index = create_endpoint(
    ENDPOINT_API + "/index",
    HTTPMethod.GET,
)


# ============================================================================
# ME (Current User)
# ============================================================================

endpoint_me = create_endpoint(
    ENDPOINT_API + "/me",
    HTTPMethod.GET,
    HTTPMethod.POST,
)

endpoint_me_avatar = create_endpoint(
    ENDPOINT_API + "/me/avatar",
    HTTPMethod.POST,
    HTTPMethod.DELETE,
)

endpoint_me_email = create_endpoint(
    ENDPOINT_API + "/me/email",
    HTTPMethod.POST,
)

endpoint_me_password = create_endpoint(
    ENDPOINT_API + "/me/password",
    HTTPMethod.POST,
)


# ============================================================================
# NODES
# ============================================================================

endpoint_nodes = create_endpoint(
    ENDPOINT_API + "/nodes",
    HTTPMethod.GET,
    HTTPMethod.POST,
)

endpoint_nodes_flattened = create_endpoint(
    ENDPOINT_API + "/nodes/flattened",
    HTTPMethod.GET,
)


def endpoint_node(node_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/nodes/{node_id}",
        HTTPMethod.GET,
        HTTPMethod.POST,
        HTTPMethod.DELETE,
    )


# ============================================================================
# POSTS
# ============================================================================

endpoint_posts = create_endpoint(
    ENDPOINT_API + "/posts",
    HTTPMethod.POST,
)


def endpoint_post(post_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/posts/{post_id}",
        HTTPMethod.GET,
        HTTPMethod.POST,
        HTTPMethod.DELETE,
    )


def endpoint_post_mark_solution(post_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/posts/{post_id}/mark-solution",
        HTTPMethod.POST,
    )


def endpoint_post_react(post_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/posts/{post_id}/react",
        HTTPMethod.POST,
    )


def endpoint_post_vote(post_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/posts/{post_id}/vote",
        HTTPMethod.POST,
    )


# ============================================================================
# PROFILE POST COMMENTS
# ============================================================================

endpoint_profile_post_comments = create_endpoint(
    ENDPOINT_API + "/profile-post-comments",
    HTTPMethod.POST,
)


def endpoint_profile_post_comment(comment_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/profile-post-comments/{comment_id}",
        HTTPMethod.GET,
        HTTPMethod.POST,
        HTTPMethod.DELETE,
    )


def endpoint_profile_post_comment_react(comment_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/profile-post-comments/{comment_id}/react",
        HTTPMethod.POST,
    )


# ============================================================================
# PROFILE POSTS
# ============================================================================

endpoint_profile_posts = create_endpoint(
    ENDPOINT_API + "/profile-posts",
    HTTPMethod.POST,
)


def endpoint_profile_post(profile_post_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/profile-posts/{profile_post_id}",
        HTTPMethod.GET,
        HTTPMethod.POST,
        HTTPMethod.DELETE,
    )


def endpoint_profile_post_comments_list(profile_post_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/profile-posts/{profile_post_id}/comments",
        HTTPMethod.GET,
    )


def endpoint_profile_post_react(profile_post_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/profile-posts/{profile_post_id}/react",
        HTTPMethod.POST,
    )


# ============================================================================
# STATS
# ============================================================================

endpoint_stats = create_endpoint(
    ENDPOINT_API + "/stats",
    HTTPMethod.GET,
)


# ============================================================================
# THREADS
# ============================================================================

endpoint_threads = create_endpoint(
    ENDPOINT_API + "/threads",
    HTTPMethod.GET,
    HTTPMethod.POST,
)


def endpoint_thread(thread_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/threads/{thread_id}",
        HTTPMethod.GET,
        HTTPMethod.POST,
        HTTPMethod.DELETE,
    )


def endpoint_thread_change_type(thread_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/threads/{thread_id}/change-type",
        HTTPMethod.POST,
    )


def endpoint_thread_mark_read(thread_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/threads/{thread_id}/mark-read",
        HTTPMethod.POST,
    )


def endpoint_thread_move(thread_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/threads/{thread_id}/move",
        HTTPMethod.POST,
    )


def endpoint_thread_posts(thread_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/threads/{thread_id}/posts",
        HTTPMethod.GET,
    )


def endpoint_thread_vote(thread_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/threads/{thread_id}/vote",
        HTTPMethod.POST,
    )


# ============================================================================
# USERS
# ============================================================================

endpoint_users = create_endpoint(
    ENDPOINT_API + "/users",
    HTTPMethod.GET,
    HTTPMethod.POST,
)

endpoint_users_find_email = create_endpoint(
    ENDPOINT_API + "/users/find-email",
    HTTPMethod.GET,
)

endpoint_users_find_name = create_endpoint(
    ENDPOINT_API + "/users/find-name",
    HTTPMethod.GET,
)


def endpoint_user(user_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/users/{user_id}",
        HTTPMethod.GET,
        HTTPMethod.POST,
        HTTPMethod.DELETE,
    )


def endpoint_user_avatar(user_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/users/{user_id}/avatar",
        HTTPMethod.POST,
        HTTPMethod.DELETE,
    )


def endpoint_user_profile_posts(user_id: int):
    return create_endpoint(
        ENDPOINT_API + f"/users/{user_id}/profile-posts",
        HTTPMethod.GET,
    )


# ============================================================================
# OAUTH2
# ============================================================================

endpoint_oauth2_revoke = create_endpoint(
    ENDPOINT_API + "/oauth2/revoke",
    HTTPMethod.POST,
)

endpoint_oauth2_token = create_endpoint(
    ENDPOINT_API + "/oauth2/token",
    HTTPMethod.GET,
    HTTPMethod.POST,
)


# ============================================================================
# OEMBED
# ============================================================================

endpoint_oembed = create_endpoint(
    ENDPOINT_API + "/oembed",
    HTTPMethod.GET,
)
