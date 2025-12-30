"""NightForo XenForo API Client."""

from typing import Optional

from .errors import NoApiKeyProvidedError
from .http import HTTPClient

# Params imports
from .types.alert.params import (
    AlertMarkParams,
    AlertSendParams,
    AlertsGetParams,
    AlertsMarkAllParams,
)

# Response imports
from .types.alert.response import (
    AlertGetResponse,
    AlertMarkResponse,
    AlertSendResponse,
    AlertsGetResponse,
    AlertsMarkAllResponse,
)
from .types.attachment.params import (
    AttachmentsCreateNewKeyParams,
    AttachmentsGetParams,
    AttachmentUploadParams,
)
from .types.attachment.response import (
    AttachmentDeleteResponse,
    AttachmentGetData,
    AttachmentGetResponse,
    AttachmentGetThumbnail,
    AttachmentsCreateNewKeyResponse,
    AttachmentsGetResponse,
    AttachmentUploadResponse,
)
from .types.auth.params import (
    AuthFromSessionParams,
    AuthLoginTokenParams,
    AuthTestParams,
)
from .types.auth.response import (
    AuthFromSessionResponse,
    AuthLoginTokenResponse,
    AuthTestResponse,
)
from .types.conversation.params import (
    ConversationCreateParams,
    ConversationDeleteParams,
    ConversationGetMessagesParams,
    ConversationGetParams,
    ConversationInviteParams,
    ConversationMarkReadParams,
    ConversationsGetParams,
    ConversationStarParams,
    ConversationUpdateParams,
)
from .types.conversation.response import (
    ConversationCreateResponse,
    ConversationDeleteResponse,
    ConversationGetResponse,
    ConversationInviteResponse,
    ConversationMarkReadResponse,
    ConversationMarkUnreadResponse,
    ConversationMessagesGetResponse,
    ConversationsGetResponse,
    ConversationStarResponse,
    ConversationUpdateResponse,
)
from .types.conversation_message.params import (
    ConversationMessageReactParams,
    ConversationMessageReplyParams,
    ConversationMessageUpdateParams,
)
from .types.conversation_message.response import (
    ConversationMessageGetResponse,
    ConversationMessageReactResponse,
    ConversationMessageReplyResponse,
    ConversationMessageUpdateResponse,
)
from .types.forum.params import (
    ForumGetParams,
    ForumMarkReadParams,
    ForumThreadsGetParams,
)
from .types.forum.response import (
    ForumGetResponse,
    ForumMarkReadResponse,
    ForumThreadsGetResponse,
)
from .types.me.params import (
    MeAvatarUpdateParams,
    MeEmailUpdateParams,
    MePasswordUpdateParams,
    MeUpdateParams,
)
from .types.me.response import (
    MeAvatarDeleteResponse,
    MeAvatarUpdateResponse,
    MeEmailUpdateResponse,
    MeGetResponse,
    MePasswordUpdateResponse,
    MeUpdateResponse,
)
from .types.node.params import (
    NodeCreateParams,
    NodeDeleteParams,
    NodeUpdateParams,
)
from .types.node.response import (
    NodeCreateResponse,
    NodeDeleteResponse,
    NodeGetResponse,
    NodesFlattenedGetResponse,
    NodesGetResponse,
    NodeUpdateResponse,
)
from .types.page.response import IndexGetResponse
from .types.post.params import (
    PostCreateParams,
    PostDeleteParams,
    PostReactParams,
    PostUpdateParams,
    PostVoteParams,
)
from .types.post.response import (
    PostCreateResponse,
    PostDeleteResponse,
    PostGetResponse,
    PostMarkSolutionResponse,
    PostReactResponse,
    PostUpdateResponse,
    PostVoteResponse,
)
from .types.profile_post.params import (
    ProfilePostCreateParams,
    ProfilePostDeleteParams,
    ProfilePostGetParams,
    ProfilePostReactParams,
    ProfilePostUpdateParams,
)
from .types.profile_post.response import (
    ProfilePostCommentsGetResponse,
    ProfilePostCreateResponse,
    ProfilePostDeleteResponse,
    ProfilePostGetResponse,
    ProfilePostReactResponse,
    ProfilePostUpdateResponse,
)
from .types.profile_post_comment.params import (
    ProfilePostCommentCreateParams,
    ProfilePostCommentDeleteParams,
    ProfilePostCommentReactParams,
    ProfilePostCommentsGetParams,
    ProfilePostCommentUpdateParams,
)
from .types.profile_post_comment.response import (
    ProfilePostCommentCreateResponse,
    ProfilePostCommentDeleteResponse,
    ProfilePostCommentGetResponse,
    ProfilePostCommentReactResponse,
    ProfilePostCommentUpdateResponse,
)
from .types.stats.response import StatsResponse
from .types.thread.params import (
    ThreadChangeTypeParams,
    ThreadCreateParams,
    ThreadDeleteParams,
    ThreadGetParams,
    ThreadMarkReadParams,
    ThreadMoveParams,
    ThreadPostsGetParams,
    ThreadsGetParams,
    ThreadUpdateParams,
    ThreadVoteParams,
)
from .types.thread.response import (
    ThreadChangeTypeResponse,
    ThreadCreateResponse,
    ThreadDeleteResponse,
    ThreadGetResponse,
    ThreadMarkReadResponse,
    ThreadMoveResponse,
    ThreadPostsGetResponse,
    ThreadsGetResponse,
    ThreadUpdateResponse,
    ThreadVoteResponse,
)
from .types.user.params import (
    UserAvatarChangeParams,
    UserCreateParams,
    UserGetParams,
    UserProfilePostsGetParams,
    UserRenameParams,
    UsersFindEmailParams,
    UsersFindNameParams,
    UsersGetParams,
    UserUpdateParams,
)
from .types.user.response import (
    UserAvatarDeleteResponse,
    UserAvatarUpdateResponse,
    UserCreateResponse,
    UserDeleteResponse,
    UserFindEmailResponse,
    UserFindNameResponse,
    UserGetResponse,
    UserProfilePostsGetResponse,
    UsersGetResponse,
    UserUpdateResponse,
)


class Client:
    """XenForo API Client

    Main client for interacting with XenForo REST API.

    Parameters
    ----------
    api_key : str
        XenForo API key for authentication

    Raises:
    ------
    NoApiKeyProvidedError
        If api_key is empty string
    """

    def __init__(self, api_key: str) -> None:
        if api_key == "":
            raise NoApiKeyProvidedError()

        self._http = HTTPClient(api_key)

    # ============================================================================
    # ALERTS
    # ============================================================================

    async def get_alerts(
        self, params: Optional[AlertsGetParams] = None
    ) -> AlertsGetResponse:
        """GET alerts/ - Gets the API user's list of alerts

        Parameters
        ----------
        params : AlertsGetParams, optional
            page : int, optional
                Page number of results
            cutoff : int, optional
                Unix timestamp of oldest alert to include
            unviewed : bool, optional
                If true, gets only unviewed alerts
            unread : bool, optional
                If true, gets only unread alerts

        Returns:
        -------
        AlertsGetResponse
            alerts : List[UserAlert]
                List of user alerts
            pagination : Pagination
                Pagination information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_alerts(params)
        return AlertsGetResponse.model_validate(payload)

    async def send_alert(self, params: AlertSendParams) -> AlertSendResponse:
        """POST alerts/ - Sends an alert to the specified user

        Only available to super user keys.

        Parameters
        ----------
        params : AlertSendParams
            to_user_id : int
                ID of the user to receive the alert
            alert : str
                Text of the alert
            from_user_id : int, optional
                User to send the alert from
            link_url : str, optional
                URL user will be taken to
            link_title : str, optional
                Text of the link URL

        Returns:
        -------
        AlertSendResponse
            success : bool
                True if alert was sent successfully

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.send_alert(params)
        return AlertSendResponse.model_validate(payload)

    async def mark_all_alerts(
        self, params: AlertsMarkAllParams
    ) -> AlertsMarkAllResponse:
        """POST alerts/mark-all - Marks all of the API user's alerts as read or viewed

        Parameters
        ----------
        params : AlertsMarkAllParams
            read : bool, optional
                Marks all alerts as read
            viewed : bool, optional
                Marks all alerts as viewed

        Returns:
        -------
        AlertsMarkAllResponse
            success : bool
                True if operation was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.mark_all_alerts(params)
        return AlertsMarkAllResponse.model_validate(payload)

    async def get_alert(self, alert_id: int) -> AlertGetResponse:
        """GET alerts/{id}/ - Gets information about the specified alert

        Parameters
        ----------
        alert_id : int
            ID of the alert

        Returns:
        -------
        AlertGetResponse
            alert : UserAlert
                Alert information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_alert(alert_id)
        return AlertGetResponse.model_validate(payload)

    async def mark_alert(
        self, alert_id: int, params: AlertMarkParams
    ) -> AlertMarkResponse:
        """POST alerts/{id}/mark - Marks the alert as viewed/read/unread

        Parameters
        ----------
        alert_id : int
            ID of the alert
        params : AlertMarkParams
            read : bool, optional
                Marks the alert as read
            unread : bool, optional
                Marks the alert as unread
            viewed : bool, optional
                Marks all alerts as viewed

        Returns:
        -------
        AlertMarkResponse
            success : bool
                True if operation was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.mark_alert(alert_id, params)
        return AlertMarkResponse.model_validate(payload)

    # ============================================================================
    # ATTACHMENTS
    # ============================================================================

    async def get_attachments(
        self, params: AttachmentsGetParams
    ) -> AttachmentsGetResponse:
        """GET attachments/ - Gets the attachments associated with the provided API attachment key

        Parameters
        ----------
        params : AttachmentsGetParams
            key : str
                The API attachment key

        Returns:
        -------
        AttachmentsGetResponse
            attachments : List[Attachment]
                List of attachments

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_attachments(params)
        return AttachmentsGetResponse.model_validate(payload)

    async def upload_attachment(
        self, params: AttachmentUploadParams
    ) -> AttachmentUploadResponse:
        """POST attachments/ - Uploads an attachment

        Must be submitted using multipart/form-data encoding.

        Parameters
        ----------
        params : AttachmentUploadParams
            key : str
                The API attachment key
            attachment : BinaryIO
                The attachment file

        Returns:
        -------
        AttachmentUploadResponse
            attachment : Attachment
                Uploaded attachment information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.upload_attachment(params)
        return AttachmentUploadResponse.model_validate(payload)

    async def create_attachment_key(
        self, params: AttachmentsCreateNewKeyParams
    ) -> AttachmentsCreateNewKeyResponse:
        """POST attachments/new-key - Creates a new attachment key

        Parameters
        ----------
        params : AttachmentsCreateNewKeyParams
            type : str
                Content type of the attachment
            context : List[str], optional
                Key-value pairs representing context
            attachment : BinaryIO, optional
                First attachment to be associated

        Returns:
        -------
        AttachmentsCreateNewKeyResponse
            key : str
                The attachment key created
            attachment : Attachment, optional
                Attachment information if provided

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.create_attachment_key(params)
        return AttachmentsCreateNewKeyResponse.model_validate(payload)

    async def get_attachment(
        self, attachment_id: int
    ) -> AttachmentGetResponse:
        """GET attachments/{id}/ - Gets information about the specified attachment

        Parameters
        ----------
        attachment_id : int
            ID of the attachment

        Returns:
        -------
        AttachmentGetResponse
            attachment : Attachment
                Attachment information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_attachment(attachment_id)
        return AttachmentGetResponse.model_validate(payload)

    async def delete_attachment(
        self, attachment_id: int
    ) -> AttachmentDeleteResponse:
        """DELETE attachments/{id}/ - Deletes the specified attachment

        Parameters
        ----------
        attachment_id : int
            ID of the attachment

        Returns:
        -------
        AttachmentDeleteResponse
            success : bool
                True if deletion was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.delete_attachment(attachment_id)
        return AttachmentDeleteResponse.model_validate(payload)

    async def get_attachment_data(
        self, attachment_id: int
    ) -> AttachmentGetData:
        """GET attachments/{id}/data - Gets the data that makes up the specified attachment

        Parameters
        ----------
        attachment_id : int
            ID of the attachment

        Returns:
        -------
        AttachmentGetData
            data : BinaryIO
                The binary data

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_attachment_data(attachment_id)
        return AttachmentGetData.model_validate(payload)

    async def get_attachment_thumbnail(
        self, attachment_id: int
    ) -> AttachmentGetThumbnail:
        """GET attachments/{id}/thumbnail - Gets the URL to the attachment's thumbnail

        Parameters
        ----------
        attachment_id : int
            ID of the attachment

        Returns:
        -------
        AttachmentGetThumbnail
            url : str
                URL via 301 redirect

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_attachment_thumbnail(attachment_id)
        return AttachmentGetThumbnail.model_validate(payload)

    # ============================================================================
    # AUTH
    # ============================================================================

    async def test_auth(self, params: AuthTestParams) -> AuthTestResponse:
        """POST auth/ - Tests a login and password for validity

        Only available to super user keys.

        Parameters
        ----------
        params : AuthTestParams
            login : str
                Username or email address
            password : str
                The password
            limit_ip : str, optional
                IP that should be considered making the request

        Returns:
        -------
        AuthTestResponse
            user : User
                User information if authentication successful

        Raises:
        ------
        XenForoError
            If authentication fails or API request fails
        """
        payload = await self._http.test_auth(params)
        return AuthTestResponse.model_validate(payload)

    async def auth_from_session(
        self, params: AuthFromSessionParams
    ) -> AuthFromSessionResponse:
        """POST auth/from-session - Looks up the active XenForo user based on session ID or remember cookie

        Parameters
        ----------
        params : AuthFromSessionParams
            session_id : str, optional
                Checks for active session
            remember_cookie : str, optional
                Checks for active "remember me" cookie

        Returns:
        -------
        AuthFromSessionResponse
            success : bool
                True if session is valid
            user : User
                User information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.auth_from_session(params)
        return AuthFromSessionResponse.model_validate(payload)

    async def create_login_token(
        self, params: AuthLoginTokenParams
    ) -> AuthLoginTokenResponse:
        """POST auth/login-token - Generates a token that can automatically log into a specific XenForo user

        Parameters
        ----------
        params : AuthLoginTokenParams
            user_id : int
                User ID to generate token for
            limit_ip : str, optional
                Locks token to specified IP
            return_url : str, optional
                URL to return user after login
            force : bool, optional
                Forcibly replace currently logged in user
            remember : bool, optional
                Set "remember me" cookie

        Returns:
        -------
        AuthLoginTokenResponse
            login_token : str
                Generated login token
            login_url : str
                URL to use for login
            expiry_date : int
                Unix timestamp of expiration

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.create_login_token(params)
        return AuthLoginTokenResponse.model_validate(payload)

    # ============================================================================
    # CONVERSATION MESSAGES
    # ============================================================================

    async def reply_conversation_message(
        self, params: ConversationMessageReplyParams
    ) -> ConversationMessageReplyResponse:
        """POST conversation-messages/ - Replies to a conversation

        Parameters
        ----------
        params : ConversationMessageReplyParams
            conversation_id : int
                ID of the conversation
            message : str
                Message content
            attachment_key : str, optional
                Attachment key if including attachments

        Returns:
        -------
        ConversationMessageReplyResponse
            success : bool
                True if message was posted
            message : ConversationMessage
                Posted message information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.reply_conversation_message(params)
        return ConversationMessageReplyResponse.model_validate(payload)

    async def get_conversation_message(
        self, message_id: int
    ) -> ConversationMessageGetResponse:
        """GET conversation-messages/{id}/ - Gets the specified conversation message

        Parameters
        ----------
        message_id : int
            ID of the conversation message

        Returns:
        -------
        ConversationMessageGetResponse
            message : ConversationMessage
                Message information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_conversation_message(message_id)
        return ConversationMessageGetResponse.model_validate(payload)

    async def update_conversation_message(
        self, message_id: int, params: ConversationMessageUpdateParams
    ) -> ConversationMessageUpdateResponse:
        """POST conversation-messages/{id}/ - Updates the specified conversation message

        Parameters
        ----------
        message_id : int
            ID of the conversation message
        params : ConversationMessageUpdateParams
            message : str
                Updated message content
            attachment_key : str, optional
                Attachment key if including attachments

        Returns:
        -------
        ConversationMessageUpdateResponse
            success : bool
                True if update was successful
            message : ConversationMessage
                Updated message information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.update_conversation_message(
            message_id, params
        )
        return ConversationMessageUpdateResponse.model_validate(payload)

    async def react_conversation_message(
        self, message_id: int, params: ConversationMessageReactParams
    ) -> ConversationMessageReactResponse:
        """POST conversation-messages/{id}/react - Reacts to the specified conversation message.

        Parameters
        ----------
        message_id : int
            ID of the conversation message
        params : ConversationMessageReactParams
            reaction_id : int
                ID of the reaction

        Returns:
        -------
        ConversationMessageReactResponse
            success : bool
                True if reaction was added/removed
            action : str
                "insert" or "delete"

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.react_conversation_message(
            message_id, params
        )
        return ConversationMessageReactResponse.model_validate(payload)

    # ============================================================================
    # CONVERSATIONS
    # ============================================================================

    async def get_conversations(
        self, params: Optional[ConversationsGetParams] = None
    ) -> ConversationsGetResponse:
        """GET conversations/ - Gets the API user's list of conversations.

        Parameters
        ----------
        params : ConversationsGetParams, optional
            page : int, optional
                Page number
            starter_id : int, optional
                Filter by starter user ID
            receiver_id : int, optional
                Filter by receiver user ID
            starred : bool, optional
                Only gets starred conversations
            unread : bool, optional
                Only gets unread conversations

        Returns:
        -------
        ConversationsGetResponse
            conversations : List[Conversation]
                List of conversations
            pagination : Pagination
                Pagination information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_conversations(params)
        return ConversationsGetResponse.model_validate(payload)

    async def create_conversation(
        self, params: ConversationCreateParams
    ) -> ConversationCreateResponse:
        """POST conversations/ - Creates a conversation.

        Parameters
        ----------
        params : ConversationCreateParams
            recipient_ids : List[int]
                IDs of recipient users
            title : str
                Conversation title
            message : str
                First message content
            attachment_key : str, optional
                Attachment key if including attachments
            conversation_open : bool, optional
                Whether conversation is open
            open_invite : bool, optional
                Whether open for invites

        Returns:
        -------
        ConversationCreateResponse
            success : bool
                True if conversation was created
            conversation : Conversation
                Created conversation information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.create_conversation(params)
        return ConversationCreateResponse.model_validate(payload)

    async def get_conversation(
        self,
        conversation_id: int,
        params: Optional[ConversationGetParams] = None,
    ) -> ConversationGetResponse:
        """GET conversations/{id}/ - Gets information about the specified conversation.

        Parameters
        ----------
        conversation_id : int
            ID of the conversation
        params : ConversationGetParams, optional
            with_messages : bool, optional
                Include a page of messages
            page : int, optional
                Page number

        Returns:
        -------
        ConversationGetResponse
            conversation : Conversation
                Conversation information
            messages : List[ConversationMessage], optional
                Messages if requested
            pagination : Pagination, optional
                Pagination if messages included

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_conversation(conversation_id, params)
        return ConversationGetResponse.model_validate(payload)

    async def update_conversation(
        self, conversation_id: int, params: ConversationUpdateParams
    ) -> ConversationUpdateResponse:
        """POST conversations/{id}/ - Updates the specified conversation.

        Parameters
        ----------
        conversation_id : int
            ID of the conversation
        params : ConversationUpdateParams
            title : str, optional
                New conversation title
            open_invite : bool, optional
                Whether open for invites
            conversation_open : bool, optional
                Whether conversation is open

        Returns:
        -------
        ConversationUpdateResponse
            success : bool
                True if update was successful
            conversation : Conversation
                Updated conversation information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.update_conversation(conversation_id, params)
        return ConversationUpdateResponse.model_validate(payload)

    async def delete_conversation(
        self,
        conversation_id: int,
        params: Optional[ConversationDeleteParams] = None,
    ) -> ConversationDeleteResponse:
        """DELETE conversations/{id}/ - Deletes the specified conversation from the API user's list

        Parameters
        ----------
        conversation_id : int
            ID of the conversation
        params : ConversationDeleteParams, optional
            ignore : bool, optional
                Ignore further replies

        Returns:
        -------
        ConversationDeleteResponse
            success : bool
                True if deletion was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.delete_conversation(conversation_id, params)
        return ConversationDeleteResponse.model_validate(payload)

    async def invite_conversation(
        self, conversation_id: int, params: ConversationInviteParams
    ) -> ConversationInviteResponse:
        """POST conversations/{id}/invite - Invites the specified users to this conversation

        Parameters
        ----------
        conversation_id : int
            ID of the conversation
        params : ConversationInviteParams
            recipient_ids : List[int]
                IDs of users to invite

        Returns:
        -------
        ConversationInviteResponse
            success : bool
                True if invites were sent

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.invite_conversation(conversation_id, params)
        return ConversationInviteResponse.model_validate(payload)

    async def mark_conversation_read(
        self,
        conversation_id: int,
        params: Optional[ConversationMarkReadParams] = None,
    ) -> ConversationMarkReadResponse:
        """POST conversations/{id}/mark-read - Marks the conversation as read up until the specified time

        Parameters
        ----------
        conversation_id : int
            ID of the conversation
        params : ConversationMarkReadParams, optional
            date : int, optional
                Unix timestamp

        Returns:
        -------
        ConversationMarkReadResponse
            success : bool
                True if operation was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.mark_conversation_read(
            conversation_id, params
        )
        return ConversationMarkReadResponse.model_validate(payload)

    async def mark_conversation_unread(
        self, conversation_id: int
    ) -> ConversationMarkUnreadResponse:
        """POST conversations/{id}/mark-unread - Marks a conversation as unread

        Parameters
        ----------
        conversation_id : int
            ID of the conversation

        Returns:
        -------
        ConversationMarkUnreadResponse
            success : bool
                True if operation was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.mark_conversation_unread(conversation_id)
        return ConversationMarkUnreadResponse.model_validate(payload)

    async def get_conversation_messages(
        self,
        conversation_id: int,
        params: Optional[ConversationGetMessagesParams] = None,
    ) -> ConversationMessagesGetResponse:
        """GET conversations/{id}/messages - Gets a page of messages in the specified conversation

        Parameters
        ----------
        conversation_id : int
            ID of the conversation
        params : ConversationGetMessagesParams, optional
            page : int, optional
                Page number

        Returns:
        -------
        ConversationMessagesGetResponse
            messages : List[ConversationMessage]
                List of messages
            pagination : Pagination
                Pagination information

        Raises:
        ------
        XenForoError
            If the API request fails
        """

        payload = await self._http.get_conversation_messages(
            conversation_id, params
        )
        return ConversationMessagesGetResponse.model_validate(payload)

    async def star_conversation(
        self, conversation_id: int, params: ConversationStarParams
    ) -> ConversationStarResponse:
        """POST conversations/{id}/star - Sets the star status of the specified conversation

        Parameters
        ----------
        conversation_id : int
            ID of the conversation
        params : ConversationStarParams
            star : bool
                Sets the star status

        Returns:
        -------
        ConversationStarResponse
            success : bool
                True if operation was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.star_conversation(conversation_id, params)
        return ConversationStarResponse.model_validate(payload)

    # ============================================================================
    # FORUMS
    # ============================================================================

    async def get_forum(
        self, forum_id: int, params: Optional[ForumGetParams] = None
    ) -> ForumGetResponse:
        """GET forums/{id}/ - Gets information about the specified forum

        Parameters
        ----------
        forum_id : int
            ID of the forum
        params : ForumGetParams, optional
            with_threads : bool, optional
                Gets a page of threads
            page : int, optional
                Page number
            prefix_id : int, optional
                Filter by prefix
            starter_id : int, optional
                Filter by user ID
            last_days : int, optional
                Filter by reply in last X days
            unread : bool, optional
                Filter to unread threads
            thread_type : str, optional
                Filter by thread type
            order : str, optional
                Method of ordering
            direction : str, optional
                "asc" or "desc"

        Returns:
        -------
        ForumGetResponse
            forum : Forum
                Forum information
            threads : List[Thread], optional
                Threads if requested
            pagination : Pagination, optional
                Pagination if threads included
            sticky : List[Thread], optional
                Sticky threads

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_forum(forum_id, params)
        return ForumGetResponse.model_validate(payload)

    async def mark_forum_read(
        self, forum_id: int, params: Optional[ForumMarkReadParams] = None
    ) -> ForumMarkReadResponse:
        """POST forums/{id}/mark-read - Marks the forum as read up until the specified time

        Parameters
        ----------
        forum_id : int
            ID of the forum
        params : ForumMarkReadParams, optional
            date : int, optional
                Unix timestamp

        Returns:
        -------
        ForumMarkReadResponse
            success : bool
                True if operation was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.mark_forum_read(forum_id, params)
        return ForumMarkReadResponse.model_validate(payload)

    async def get_forum_threads(
        self, forum_id: int, params: Optional[ForumThreadsGetParams] = None
    ) -> ForumThreadsGetResponse:
        """GET forums/{id}/threads - Gets a page of threads from the specified forum

        Parameters
        ----------
        forum_id : int
            ID of the forum
        params : ForumThreadsGetParams, optional
            page : int, optional
                Page number
            prefix_id : int, optional
                Filter by prefix
            starter_id : int, optional
                Filter by user ID
            last_days : int, optional
                Filter by reply in last X days
            unread : bool, optional
                Filter to unread threads
            thread_type : str, optional
                Filter by thread type
            order : str, optional
                Method of ordering
            direction : str, optional
                "asc" or "desc"

        Returns:
        -------
        ForumThreadsGetResponse
            threads : List[Thread]
                List of threads
            pagination : Pagination
                Pagination information
            sticky : List[Thread], optional
                Sticky threads

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_forum_threads(forum_id, params)
        return ForumThreadsGetResponse.model_validate(payload)

    # ============================================================================
    # INDEX
    # ============================================================================

    async def get_index(self) -> IndexGetResponse:
        """GET index/ - Gets general information about the site and the API

        Returns:
        -------
        IndexGetResponse
            version_id : int
                XenForo version ID
            site_title : str
                Site title
            base_url : str
                Base URL
            api_url : str
                API URL
            key : ApiKey
                API key information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_index()
        return IndexGetResponse.model_validate(payload)

    # ============================================================================
    # ME (Current User)
    # ============================================================================

    async def get_me(self) -> MeGetResponse:
        """GET me/ - Gets information about the current API user

        Returns:
        -------
        MeGetResponse
            me : User
                Current user information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_me()
        return MeGetResponse.model_validate(payload)

    async def update_me(self, params: MeUpdateParams) -> MeUpdateResponse:
        """POST me/ - Updates information about the current user

        Parameters
        ----------
        params : MeUpdateParams
            Various user settings including:
            - option : dict with creation_watch_state, interaction_watch_state, etc.
            - profile : dict with location, website, about, signature
            - privacy : dict with allow_view_profile, allow_post_profile, etc.
            - visible : bool
            - activity_visible : bool
            - timezone : str
            - custom_title : str
            - custom_fields : dict

        Returns:
        -------
        MeUpdateResponse
            success : bool
                True if update was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.update_me(params)
        return MeUpdateResponse.model_validate(payload)

    async def update_my_avatar(
        self, params: MeAvatarUpdateParams
    ) -> MeAvatarUpdateResponse:
        """POST me/avatar - Updates the current user's avatar

        Parameters
        ----------
        params : MeAvatarUpdateParams
            avatar : BinaryIO
                Avatar file

        Returns:
        -------
        MeAvatarUpdateResponse
            success : bool
                True if update was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.update_my_avatar(params)
        return MeAvatarUpdateResponse.model_validate(payload)

    async def delete_my_avatar(self) -> MeAvatarDeleteResponse:
        """DELETE me/avatar - Deletes the current user's avatar

        Returns:
        -------
        MeAvatarDeleteResponse
            success : bool
                True if deletion was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.delete_my_avatar()
        return MeAvatarDeleteResponse.model_validate(payload)

    async def update_my_email(
        self, params: MeEmailUpdateParams
    ) -> MeEmailUpdateResponse:
        """POST me/email - Updates the current user's email address

        Parameters
        ----------
        params : MeEmailUpdateParams
            current_password : str
                Current password for verification
            email : str
                New email address

        Returns:
        -------
        MeEmailUpdateResponse
            success : bool
                True if update was successful
            confirmation_required : bool
                Whether email confirmation is required

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.update_my_email(params)
        return MeEmailUpdateResponse.model_validate(payload)

    async def update_my_password(
        self, params: MePasswordUpdateParams
    ) -> MePasswordUpdateResponse:
        """POST me/password - Updates the current user's password

        Parameters
        ----------
        params : MePasswordUpdateParams
            current_password : str
                Current password
            new_password : str
                New password

        Returns:
        -------
        MePasswordUpdateResponse
            success : bool
                True if update was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.update_my_password(params)
        return MePasswordUpdateResponse.model_validate(payload)

    # ============================================================================
    # NODES
    # ============================================================================

    async def get_nodes(self) -> NodesGetResponse:
        """GET nodes/ - Gets the node tree

        Returns:
        -------
        NodesGetResponse
            tree_map : List
                Tree structure mapping
            nodes : List[Node]
                List of nodes

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_nodes()
        return NodesGetResponse.model_validate(payload)

    async def create_node(
        self, params: NodeCreateParams
    ) -> NodeCreateResponse:
        """POST nodes/ - Creates a new node

        Parameters
        ----------
        params : NodeCreateParams
            node : dict with title, node_name, description, parent_node_id, display_order, display_in_list
            type_data : dict, optional
                Type-specific data
            node_type_id : str
                Node type ID

        Returns:
        -------
        NodeCreateResponse
            node : Node
                Created node information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.create_node(params)
        return NodeCreateResponse.model_validate(payload)

    async def get_nodes_flattened(self) -> NodesFlattenedGetResponse:
        """GET nodes/flattened - Gets a flattened node tree

        Returns:
        -------
        NodesFlattenedGetResponse
            nodes_flat : List
                Flattened node list

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_nodes_flattened()
        return NodesFlattenedGetResponse.model_validate(payload)

    async def get_node(self, node_id: int) -> NodeGetResponse:
        """GET nodes/{id}/ - Gets information about the specified node

        Parameters
        ----------
        node_id : int
            ID of the node

        Returns:
        -------
        NodeGetResponse
            node : Node
                Node information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_node(node_id)
        return NodeGetResponse.model_validate(payload)

    async def update_node(
        self, node_id: int, params: NodeUpdateParams
    ) -> NodeUpdateResponse:
        """POST nodes/{id}/ - Updates the specified node

        Parameters
        ----------
        node_id : int
            ID of the node
        params : NodeUpdateParams
            node : dict with title, node_name, description, parent_node_id, display_order, display_in_list
            type_data : dict, optional
                Type-specific data

        Returns:
        -------
        NodeUpdateResponse
            node : Node
                Updated node information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.update_node(node_id, params)
        return NodeUpdateResponse.model_validate(payload)

    async def delete_node(
        self, node_id: int, params: Optional[NodeDeleteParams] = None
    ) -> NodeDeleteResponse:
        """DELETE nodes/{id}/ - Deletes the specified node

        Parameters
        ----------
        node_id : int
            ID of the node
        params : NodeDeleteParams, optional
            delete_children : bool, optional
                Whether to delete child nodes

        Returns:
        -------
        NodeDeleteResponse
            success : bool
                True if deletion was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.delete_node(node_id, params)
        return NodeDeleteResponse.model_validate(payload)

    # ============================================================================
    # POSTS
    # ============================================================================

    async def create_post(
        self, params: PostCreateParams
    ) -> PostCreateResponse:
        """POST posts/ - Adds a new reply to a thread

        Parameters
        ----------
        params : PostCreateParams
            thread_id : int
                ID of the thread to reply to
            message : str
                Post message content
            attachment_key : str, optional
                Attachment key if including attachments

        Returns:
        -------
        PostCreateResponse
            success : bool
                True if post was created
            post : Post
                Created post information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.create_post(params)
        return PostCreateResponse.model_validate(payload)

    async def get_post(self, post_id: int) -> PostGetResponse:
        """GET posts/{id}/ - Gets information about the specified post

        Parameters
        ----------
        post_id : int
            ID of the post

        Returns:
        -------
        PostGetResponse
            post : Post
                Post information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_post(post_id)
        return PostGetResponse.model_validate(payload)

    async def update_post(
        self, post_id: int, params: PostUpdateParams
    ) -> PostUpdateResponse:
        """POST posts/{id}/ - Updates the specified post

        Parameters
        ----------
        post_id : int
            ID of the post
        params : PostUpdateParams
            message : str
                Updated message content
            silent : bool, optional
                Silent edit
            clear_edit : bool, optional
                Clear edit history
            author_alert : bool, optional
                Send alert to author
            author_alert_reason : str, optional
                Reason for alert
            attachment_key : str, optional
                Attachment key if including attachments

        Returns:
        -------
        PostUpdateResponse
            success : bool
                True if update was successful
            post : Post
                Updated post information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.update_post(post_id, params)
        return PostUpdateResponse.model_validate(payload)

    async def delete_post(
        self, post_id: int, params: Optional[PostDeleteParams] = None
    ) -> PostDeleteResponse:
        """DELETE posts/{id}/ - Deletes the specified post

        Default to soft deletion.

        Parameters
        ----------
        post_id : int
            ID of the post
        params : PostDeleteParams, optional
            hard_delete : bool, optional
                Whether to hard delete
            reason : str, optional
                Deletion reason
            author_alert : bool, optional
                Send alert to author
            author_alert_reason : str, optional
                Reason for alert

        Returns:
        -------
        PostDeleteResponse
            success : bool
                True if deletion was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.delete_post(post_id, params)
        return PostDeleteResponse.model_validate(payload)

    async def mark_post_solution(
        self, post_id: int
    ) -> PostMarkSolutionResponse:
        """POST posts/{id}/mark-solution - Toggle the specified post as the solution to its containing thread

        Parameters
        ----------
        post_id : int
            ID of the post

        Returns:
        -------
        PostMarkSolutionResponse
            true : Any
                Success indicator
            new_solution_post : Post, optional
                New solution post if set
            old_solution_post : Post, optional
                Old solution post if changed

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.mark_post_solution(post_id)
        return PostMarkSolutionResponse.model_validate(payload)

    async def react_post(
        self, post_id: int, params: PostReactParams
    ) -> PostReactResponse:
        """POST posts/{id}/react - Reacts to the specified post

        Parameters
        ----------
        post_id : int
            ID of the post
        params : PostReactParams
            reaction_id : int
                ID of the reaction

        Returns:
        -------
        PostReactResponse
            success : bool
                True if reaction was added/removed
            action : str
                "insert" or "delete"

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.react_post(post_id, params)
        return PostReactResponse.model_validate(payload)

    async def vote_post(
        self, post_id: int, params: PostVoteParams
    ) -> PostVoteResponse:
        """POST posts/{id}/vote - Votes on the specified post

        Parameters
        ----------
        post_id : int
            ID of the post
        params : PostVoteParams
            type : str
                "up" or "down"

        Returns:
        -------
        PostVoteResponse
            success : bool
                True if vote was cast/removed
            action : str
                "insert" or "delete"

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.vote_post(post_id, params)
        return PostVoteResponse.model_validate(payload)

    # ============================================================================
    # PROFILE POST COMMENTS
    # ============================================================================

    async def create_profile_post_comment(
        self, params: ProfilePostCommentCreateParams
    ) -> ProfilePostCommentCreateResponse:
        """POST profile-post-comments/ - Creates a new profile post comment

        Parameters
        ----------
        params : ProfilePostCommentCreateParams
            profile_post_id : int
                ID of the profile post
            message : str
                Comment message content
            attachment_key : str, optional
                Attachment key if including attachments

        Returns:
        -------
        ProfilePostCommentCreateResponse
            success : bool
                True if comment was created
            comment : ProfilePostComment
                Created comment information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.create_profile_post_comment(params)
        return ProfilePostCommentCreateResponse.model_validate(payload)

    async def get_profile_post_comment(
        self, comment_id: int
    ) -> ProfilePostCommentGetResponse:
        """GET profile-post-comments/{id}/ - Gets information about the specified profile post comment

        Parameters
        ----------
        comment_id : int
            ID of the comment

        Returns:
        -------
        ProfilePostCommentGetResponse
            comment : ProfilePostComment
                Comment information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_profile_post_comment(comment_id)
        return ProfilePostCommentGetResponse.model_validate(payload)

    async def update_profile_post_comment(
        self, comment_id: int, params: ProfilePostCommentUpdateParams
    ) -> ProfilePostCommentUpdateResponse:
        """POST profile-post-comments/{id}/ - Updates the specified profile post comment

        Parameters
        ----------
        comment_id : int
            ID of the comment
        params : ProfilePostCommentUpdateParams
            message : str
                Updated message content
            author_alert : bool, optional
                Send alert to author
            author_alert_reason : str, optional
                Reason for alert
            attachment_key : str, optional
                Attachment key if including attachments

        Returns:
        -------
        ProfilePostCommentUpdateResponse
            success : bool
                True if update was successful
            comment : ProfilePostComment
                Updated comment information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.update_profile_post_comment(
            comment_id, params
        )
        return ProfilePostCommentUpdateResponse.model_validate(payload)

    async def delete_profile_post_comment(
        self,
        comment_id: int,
        params: Optional[ProfilePostCommentDeleteParams] = None,
    ) -> ProfilePostCommentDeleteResponse:
        """DELETE profile-post-comments/{id}/ - Deletes the specified profile post comment

        Parameters
        ----------
        comment_id : int
            ID of the comment
        params : ProfilePostCommentDeleteParams, optional
            hard_delete : bool, optional
                Whether to hard delete
            reason : str, optional
                Deletion reason
            author_alert : bool, optional
                Send alert to author
            author_alert_reason : str, optional
                Reason for alert

        Returns:
        -------
        ProfilePostCommentDeleteResponse
            success : bool
                True if deletion was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.delete_profile_post_comment(
            comment_id, params
        )
        return ProfilePostCommentDeleteResponse.model_validate(payload)

    async def react_profile_post_comment(
        self, comment_id: int, params: ProfilePostCommentReactParams
    ) -> ProfilePostCommentReactResponse:
        """POST profile-post-comments/{id}/react - Reacts to the specified profile post comment

        Parameters
        ----------
        comment_id : int
            ID of the comment
        params : ProfilePostCommentReactParams
            reaction_id : int
                ID of the reaction

        Returns:
        -------
        ProfilePostCommentReactResponse
            success : bool
                True if reaction was added/removed
            action : str
                "insert" or "delete"

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.react_profile_post_comment(
            comment_id, params
        )
        return ProfilePostCommentReactResponse.model_validate(payload)

    # ============================================================================
    # PROFILE POSTS
    # ============================================================================

    async def create_profile_post(
        self, params: ProfilePostCreateParams
    ) -> ProfilePostCreateResponse:
        """POST profile-posts/ - Creates a new profile post

        Parameters
        ----------
        params : ProfilePostCreateParams
            user_id : int
                ID of the user whose profile to post on
            message : str
                Post message content
            attachment_key : str, optional
                Attachment key if including attachments

        Returns:
        -------
        ProfilePostCreateResponse
            success : bool
                True if post was created
            profile_post : ProfilePost
                Created profile post information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.create_profile_post(params)
        return ProfilePostCreateResponse.model_validate(payload)

    async def get_profile_post(
        self,
        profile_post_id: int,
        params: Optional[ProfilePostGetParams] = None,
    ) -> ProfilePostGetResponse:
        """GET profile-posts/{id}/ - Gets information about the specified profile post

        Parameters
        ----------
        profile_post_id : int
            ID of the profile post
        params : ProfilePostGetParams, optional
            with_comments : bool, optional
                Include comments
            page : int, optional
                Page number
            direction : str, optional
                "desc" or "asc"

        Returns:
        -------
        ProfilePostGetResponse
            profile_post : ProfilePost
                Profile post information
            comments : List[ProfilePostComment], optional
                Comments if requested
            pagination : Pagination, optional
                Pagination if comments included

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_profile_post(profile_post_id, params)
        return ProfilePostGetResponse.model_validate(payload)

    async def update_profile_post(
        self, profile_post_id: int, params: ProfilePostUpdateParams
    ) -> ProfilePostUpdateResponse:
        """POST profile-posts/{id}/ - Updates the specified profile post

        Parameters
        ----------
        profile_post_id : int
            ID of the profile post
        params : ProfilePostUpdateParams
            message : str
                Updated message content
            author_alert : bool, optional
                Send alert to author
            author_alert_reason : str, optional
                Reason for alert
            attachment_key : str, optional
                Attachment key if including attachments

        Returns:
        -------
        ProfilePostUpdateResponse
            success : bool
                True if update was successful
            profile_post : ProfilePost
                Updated profile post information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.update_profile_post(profile_post_id, params)
        return ProfilePostUpdateResponse.model_validate(payload)

    async def delete_profile_post(
        self,
        profile_post_id: int,
        params: Optional[ProfilePostDeleteParams] = None,
    ) -> ProfilePostDeleteResponse:
        """DELETE profile-posts/{id}/ - Deletes the specified profile post

        Parameters
        ----------
        profile_post_id : int
            ID of the profile post
        params : ProfilePostDeleteParams, optional
            hard_delete : bool, optional
                Whether to hard delete
            reason : str, optional
                Deletion reason
            author_alert : bool, optional
                Send alert to author
            author_alert_reason : str, optional
                Reason for alert

        Returns:
        -------
        ProfilePostDeleteResponse
            success : bool
                True if deletion was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.delete_profile_post(profile_post_id, params)
        return ProfilePostDeleteResponse.model_validate(payload)

    async def get_profile_post_comments(
        self,
        profile_post_id: int,
        params: Optional[ProfilePostCommentsGetParams] = None,
    ) -> ProfilePostCommentsGetResponse:
        """GET profile-posts/{id}/comments - Gets a page of comments on the specified profile post

        Parameters
        ----------
        profile_post_id : int
            ID of the profile post
        params : ProfilePostCommentsGetParams, optional
            page : int, optional
                Page number
            direction : str, optional
                "desc" or "asc"

        Returns:
        -------
        ProfilePostCommentsGetResponse
            comments : List[ProfilePostComment]
                List of comments
            pagination : Pagination
                Pagination information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_profile_post_comments(
            profile_post_id, params
        )
        return ProfilePostCommentsGetResponse.model_validate(payload)

    async def react_profile_post(
        self, profile_post_id: int, params: ProfilePostReactParams
    ) -> ProfilePostReactResponse:
        """POST profile-posts/{id}/react - Reacts to the specified profile post

        Parameters
        ----------
        profile_post_id : int
            ID of the profile post
        params : ProfilePostReactParams
            reaction_id : int
                ID of the reaction

        Returns:
        -------
        ProfilePostReactResponse
            success : bool
                True if reaction was added/removed
            action : str
                "insert" or "delete"

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.react_profile_post(profile_post_id, params)
        return ProfilePostReactResponse.model_validate(payload)

    # ============================================================================
    # STATS
    # ============================================================================

    async def get_stats(self) -> StatsResponse:
        """GET stats/ - Gets site statistics and general activity information

        Returns:
        -------
        StatsResponse
            totals : dict
                Total counts for threads, messages, users
            latest_user : dict
                Latest registered user information
            online : dict
                Online user counts

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_stats()
        return StatsResponse.model_validate(payload)

    # ============================================================================
    # THREADS
    # ============================================================================

    async def get_threads(
        self, params: Optional[ThreadsGetParams] = None
    ) -> ThreadsGetResponse:
        """GET threads/ - Gets a list of threads

        Parameters
        ----------
        params : ThreadsGetParams, optional
            page : int, optional
                Page number
            prefix_id : int, optional
                Filter by prefix
            starter_id : int, optional
                Filter by starter user ID
            last_days : int, optional
                Filter by reply in last X days
            unread : bool, optional
                Filter to unread threads
            thread_type : str, optional
                Filter by thread type
            order : str, optional
                Method of ordering
            direction : str, optional
                "asc" or "desc"

        Returns:
        -------
        ThreadsGetResponse
            threads : List[Thread]
                List of threads
            pagination : Pagination
                Pagination information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_threads(params)
        return ThreadsGetResponse.model_validate(payload)

    async def create_thread(
        self, params: ThreadCreateParams
    ) -> ThreadCreateResponse:
        """POST threads/ - Creates a thread

        Parameters
        ----------
        params : ThreadCreateParams
            node_id : int
                ID of the forum to create thread in
            title : str
                Thread title
            message : str
                First post message content
            discussion_type : str, optional
                Discussion type
            prefix_id : int, optional
                Thread prefix ID
            tags : List[str], optional
                Thread tags
            custom_fields : dict, optional
                Custom field values
            discussion_open : bool, optional
                Whether discussion is open
            sticky : bool, optional
                Whether thread is sticky
            attachment_key : str, optional
                Attachment key if including attachments

        Returns:
        -------
        ThreadCreateResponse
            success : bool
                True if thread was created
            thread : Thread
                Created thread information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.create_thread(params)
        return ThreadCreateResponse.model_validate(payload)

    async def get_thread(
        self, thread_id: int, params: Optional[ThreadGetParams] = None
    ) -> ThreadGetResponse:
        """GET threads/{id}/ - Gets information about the specified thread

        Parameters
        ----------
        thread_id : int
            ID of the thread
        params : ThreadGetParams, optional
            with_posts : bool, optional
                Include posts
            with_first_post : bool, optional
                Include first post
            page : int, optional
                Page number

        Returns:
        -------
        ThreadGetResponse
            thread : Thread
                Thread information
            posts : List[Post], optional
                Posts if requested
            pagination : Pagination, optional
                Pagination if posts included

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_thread(thread_id, params)
        return ThreadGetResponse.model_validate(payload)

    async def update_thread(
        self, thread_id: int, params: ThreadUpdateParams
    ) -> ThreadUpdateResponse:
        """POST threads/{id}/ - Updates the specified thread

        Parameters
        ----------
        thread_id : int
            ID of the thread
        params : ThreadUpdateParams
            title : str, optional
                New thread title
            prefix_id : int, optional
                Thread prefix ID
            tags : List[str], optional
                Thread tags
            custom_fields : dict, optional
                Custom field values
            discussion_open : bool, optional
                Whether discussion is open
            sticky : bool, optional
                Whether thread is sticky

        Returns:
        -------
        ThreadUpdateResponse
            success : bool
                True if update was successful
            thread : Thread
                Updated thread information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.update_thread(thread_id, params)
        return ThreadUpdateResponse.model_validate(payload)

    async def delete_thread(
        self, thread_id: int, params: Optional[ThreadDeleteParams] = None
    ) -> ThreadDeleteResponse:
        """DELETE threads/{id}/ - Deletes the specified thread

        Parameters
        ----------
        thread_id : int
            ID of the thread
        params : ThreadDeleteParams, optional
            hard_delete : bool, optional
                Whether to hard delete
            reason : str, optional
                Deletion reason
            author_alert : bool, optional
                Send alert to author
            author_alert_reason : str, optional
                Reason for alert
            starter_alert : bool, optional
                Send alert to starter
            starter_alert_reason : str, optional
                Reason for starter alert

        Returns:
        -------
        ThreadDeleteResponse
            success : bool
                True if deletion was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.delete_thread(thread_id, params)
        return ThreadDeleteResponse.model_validate(payload)

    async def change_thread_type(
        self, thread_id: int, params: ThreadChangeTypeParams
    ) -> ThreadChangeTypeResponse:
        """POST threads/{id}/change-type - Changes the thread type

        Parameters
        ----------
        thread_id : int
            ID of the thread
        params : ThreadChangeTypeParams
            discussion_type : str
                New discussion type

        Returns:
        -------
        ThreadChangeTypeResponse
            success : bool
                True if type was changed
            thread : Thread
                Updated thread information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.change_thread_type(thread_id, params)
        return ThreadChangeTypeResponse.model_validate(payload)

    async def mark_thread_read(
        self, thread_id: int, params: ThreadMarkReadParams
    ) -> ThreadMarkReadResponse:
        """POST threads/{id}/mark-read - Marks the thread as read up until the specified time

        Parameters
        ----------
        thread_id : int
            ID of the thread
        params : ThreadMarkReadParams
            date : int
                Unix timestamp

        Returns:
        -------
        ThreadMarkReadResponse
            success : bool
                True if operation was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.mark_thread_read(thread_id, params)
        return ThreadMarkReadResponse.model_validate(payload)

    async def move_thread(
        self, thread_id: int, params: ThreadMoveParams
    ) -> ThreadMoveResponse:
        """POST threads/{id}/move - Moves the thread to a different forum

        Parameters
        ----------
        thread_id : int
            ID of the thread
        params : ThreadMoveParams
            node_id : int
                ID of the target forum
            notify_watchers : bool, optional
                Notify watchers of move
            starter_alert : bool, optional
                Send alert to thread starter
            starter_alert_reason : str, optional
                Reason for starter alert
            prefix_id : int, optional
                New prefix ID

        Returns:
        -------
        ThreadMoveResponse
            success : bool
                True if move was successful
            thread : Thread
                Moved thread information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.move_thread(thread_id, params)
        return ThreadMoveResponse.model_validate(payload)

    async def get_thread_posts(
        self, thread_id: int, params: Optional[ThreadPostsGetParams] = None
    ) -> ThreadPostsGetResponse:
        """GET threads/{id}/posts - Gets a page of posts from the specified thread

        Parameters
        ----------
        thread_id : int
            ID of the thread
        params : ThreadPostsGetParams, optional
            page : int, optional
                Page number

        Returns:
        -------
        ThreadPostsGetResponse
            posts : List[Post]
                List of posts
            pagination : Pagination
                Pagination information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_thread_posts(thread_id, params)
        return ThreadPostsGetResponse.model_validate(payload)

    async def vote_thread(
        self, thread_id: int, params: ThreadVoteParams
    ) -> ThreadVoteResponse:
        """POST threads/{id}/vote - Votes on the specified thread

        Parameters
        ----------
        thread_id : int
            ID of the thread
        params : ThreadVoteParams
            type : str
                "up" or "down"

        Returns:
        -------
        ThreadVoteResponse
            success : bool
                True if vote was cast/removed
            action : str
                "insert" or "delete"

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.vote_thread(thread_id, params)
        return ThreadVoteResponse.model_validate(payload)

    # ============================================================================
    # USERS
    # ============================================================================

    async def get_users(
        self, params: Optional[UsersGetParams] = None
    ) -> UsersGetResponse:
        """GET users/ - Gets a list of users

        Parameters
        ----------
        params : UsersGetParams, optional
            page : int, optional
                Page number

        Returns:
        -------
        UsersGetResponse
            users : List[User]
                List of users
            pagination : Pagination
                Pagination information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_users(params)
        return UsersGetResponse.model_validate(payload)

    async def create_user(
        self, params: UserCreateParams
    ) -> UserCreateResponse:
        """POST users/ - Creates a new user

        Parameters
        ----------
        params : UserCreateParams
            username : str
                Username
            email : str
                Email address
            password : str
                Password

        Returns:
        -------
        UserCreateResponse
            success : bool
                True if user was created
            user : User
                Created user information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.create_user(params)
        return UserCreateResponse.model_validate(payload)

    async def find_user_by_email(
        self, params: UsersFindEmailParams
    ) -> UserFindEmailResponse:
        """GET users/find-email - Finds a user by email address

        Parameters
        ----------
        params : UsersFindEmailParams
            email : str
                Email address to search for

        Returns:
        -------
        UserFindEmailResponse
            exact : User, optional
                Exact match user

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.find_user_by_email(params)
        return UserFindEmailResponse.model_validate(payload)

    async def find_user_by_name(
        self, params: UsersFindNameParams
    ) -> UserFindNameResponse:
        """GET users/find-name - Finds users by username

        Parameters
        ----------
        params : UsersFindNameParams
            username : str
                Username to search for

        Returns:
        -------
        UserFindNameResponse
            exact : User, optional
                Exact match user
            recommendations : List[User], optional
                Similar usernames

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.find_user_by_name(params)
        return UserFindNameResponse.model_validate(payload)

    async def get_user(
        self, user_id: int, params: Optional[UserGetParams] = None
    ) -> UserGetResponse:
        """GET users/{id}/ - Gets information about the specified user

        Parameters
        ----------
        user_id : int
            ID of the user
        params : UserGetParams, optional
            with_posts : bool, optional
                Include recent posts

        Returns:
        -------
        UserGetResponse
            user : User
                User information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_user(user_id, params)
        return UserGetResponse.model_validate(payload)

    async def update_user(
        self, user_id: int, params: UserUpdateParams
    ) -> UserUpdateResponse:
        """POST users/{id}/ - Updates the specified user

        Parameters
        ----------
        user_id : int
            ID of the user
        params : UserUpdateParams
            username : str, optional
                New username
            email : str, optional
                New email
            user_group_id : int, optional
                Primary user group
            secondary_group_ids : List[int], optional
                Secondary groups
            custom_title : str, optional
                Custom title
            is_staff : bool, optional
                Staff status
            visible : bool, optional
                Visibility

        Returns:
        -------
        UserUpdateResponse
            success : bool
                True if update was successful
            user : User
                Updated user information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.update_user(user_id, params)
        return UserUpdateResponse.model_validate(payload)

    async def delete_user(
        self, user_id: int, params: Optional[UserRenameParams] = None
    ) -> UserDeleteResponse:
        """DELETE users/{id}/ - Deletes the specified user

        Parameters
        ----------
        user_id : int
            ID of the user
        params : UserRenameParams, optional
            rename_to : str, optional
                New name for content attribution

        Returns:
        -------
        UserDeleteResponse
            success : bool
                True if deletion was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.delete_user(user_id, params)
        return UserDeleteResponse.model_validate(payload)

    async def update_user_avatar(
        self, user_id: int, params: UserAvatarChangeParams
    ) -> UserAvatarUpdateResponse:
        """POST users/{id}/avatar - Updates the specified user's avatar

        Parameters
        ----------
        user_id : int
            ID of the user
        params : UserAvatarChangeParams
            avatar : BinaryIO
                Avatar file

        Returns:
        -------
        UserAvatarUpdateResponse
            success : bool
                True if update was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.update_user_avatar(user_id, params)
        return UserAvatarUpdateResponse.model_validate(payload)

    async def delete_user_avatar(
        self, user_id: int
    ) -> UserAvatarDeleteResponse:
        """DELETE users/{id}/avatar - Deletes the specified user's avatar

        Parameters
        ----------
        user_id : int
            ID of the user

        Returns:
        -------
        UserAvatarDeleteResponse
            success : bool
                True if deletion was successful

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.delete_user_avatar(user_id)
        return UserAvatarDeleteResponse.model_validate(payload)

    async def get_user_profile_posts(
        self, user_id: int, params: Optional[UserProfilePostsGetParams] = None
    ) -> UserProfilePostsGetResponse:
        """GET users/{id}/profile-posts - Gets a page of profile posts from the specified user's profile

        Parameters
        ----------
        user_id : int
            ID of the user
        params : UserProfilePostsGetParams, optional
            page : int, optional
                Page number

        Returns:
        -------
        UserProfilePostsGetResponse
            profile_posts : List[ProfilePost]
                List of profile posts
            pagination : Pagination
                Pagination information

        Raises:
        ------
        XenForoError
            If the API request fails
        """
        payload = await self._http.get_user_profile_posts(user_id, params)
        return UserProfilePostsGetResponse.model_validate(payload)
