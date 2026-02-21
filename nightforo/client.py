"""NightForo XenForo API Client."""

from __future__ import annotations

from typing import BinaryIO

from .errors import NoApiKeyProvidedError
from .http import HTTPClient
from .types.alert import (
    AlertGetResponse,
    AlertMarkParams,
    AlertMarkResponse,
    AlertSendParams,
    AlertSendResponse,
    AlertsGetParams,
    AlertsGetResponse,
    AlertsMarkAllParams,
    AlertsMarkAllResponse,
)
from .types.attachment import (
    AttachmentDeleteResponse,
    AttachmentGetDataResponse,
    AttachmentGetResponse,
    AttachmentGetThumbnailResponse,
    AttachmentsCreateNewKeyParams,
    AttachmentsCreateNewKeyResponse,
    AttachmentsGetParams,
    AttachmentsGetResponse,
    AttachmentUploadParams,
    AttachmentUploadResponse,
)
from .types.auth import (
    AuthFromSessionParams,
    AuthFromSessionResponse,
    AuthLoginTokenParams,
    AuthLoginTokenResponse,
    AuthTestParams,
    AuthTestResponse,
)
from .types.conversation import (
    ConversationCreateParams,
    ConversationCreateResponse,
    ConversationDeleteParams,
    ConversationDeleteResponse,
    ConversationGetMessagesParams,
    ConversationGetParams,
    ConversationGetResponse,
    ConversationInviteParams,
    ConversationInviteResponse,
    ConversationMarkReadParams,
    ConversationMarkReadResponse,
    ConversationMarkUnreadResponse,
    ConversationMessagesGetResponse,
    ConversationsGetParams,
    ConversationsGetResponse,
    ConversationStarParams,
    ConversationStarResponse,
    ConversationUpdateParams,
    ConversationUpdateResponse,
)
from .types.conversation_message import (
    ConversationMessageGetResponse,
    ConversationMessageReactParams,
    ConversationMessageReactResponse,
    ConversationMessageReplyParams,
    ConversationMessageReplyResponse,
    ConversationMessageUpdateParams,
    ConversationMessageUpdateResponse,
)
from .types.forum import (
    ForumGetParams,
    ForumGetResponse,
    ForumMarkReadParams,
    ForumMarkReadResponse,
    ForumThreadsGetParams,
    ForumThreadsGetResponse,
)
from .types.groups import ArzGuardGroupsIdsEnum
from .types.index import IndexGetResponse
from .types.me import (
    MeAvatarDeleteResponse,
    MeAvatarUpdateResponse,
    MeEmailUpdateResponse,
    MeGetResponse,
    MePasswordUpdateResponse,
    MeUpdateResponse,
)
from .types.me.params import (
    MeEmailUpdateParams,
    MePasswordUpdateParams,
    MeUpdateParams,
)
from .types.node import (
    NodeCreateResponse,
    NodeDeleteParams,
    NodeDeleteResponse,
    NodeGetResponse,
    NodesFlattenedGetResponse,
    NodesGetResponse,
    NodeUpdateParams,
    NodeUpdateResponse,
)
from .types.node.params import AnyNodeCreateParams
from .types.post import (
    PostCreateParams,
    PostCreateResponse,
    PostDeleteParams,
    PostDeleteResponse,
    PostGetResponse,
    PostMarkSolutionResponse,
    PostReactParams,
    PostReactResponse,
    PostUpdateParams,
    PostUpdateResponse,
    PostVoteParams,
    PostVoteResponse,
)
from .types.profile_post import (
    ProfilePostCommentsGetResponse,
    ProfilePostCreateParams,
    ProfilePostCreateResponse,
    ProfilePostDeleteParams,
    ProfilePostDeleteResponse,
    ProfilePostGetParams,
    ProfilePostGetResponse,
    ProfilePostReactParams,
    ProfilePostReactResponse,
    ProfilePostUpdateParams,
    ProfilePostUpdateResponse,
)
from .types.profile_post_comment import (
    ProfilePostCommentCreateParams,
    ProfilePostCommentCreateResponse,
    ProfilePostCommentDeleteParams,
    ProfilePostCommentDeleteResponse,
    ProfilePostCommentGetResponse,
    ProfilePostCommentReactParams,
    ProfilePostCommentReactResponse,
    ProfilePostCommentsGetParams,
    ProfilePostCommentUpdateParams,
    ProfilePostCommentUpdateResponse,
)
from .types.stats import StatsResponse
from .types.thread import (
    ThreadChangeTypeParams,
    ThreadChangeTypeResponse,
    ThreadCreateParams,
    ThreadCreateResponse,
    ThreadDeleteParams,
    ThreadDeleteResponse,
    ThreadGetParams,
    ThreadGetResponse,
    ThreadMarkReadParams,
    ThreadMarkReadResponse,
    ThreadMoveParams,
    ThreadMoveResponse,
    ThreadPostsGetParams,
    ThreadPostsGetResponse,
    ThreadsGetParams,
    ThreadsGetResponse,
    ThreadUpdateParams,
    ThreadUpdateResponse,
    ThreadVoteParams,
    ThreadVoteResponse,
)
from .types.thread_type import ThreadTypeEnum
from .types.user import (
    DemoteUserResponse,
    GetDemoteGroupsResponse,
    GetPromoteGroupsResponse,
    PromoteUserResponse,
    UserAvatarDeleteResponse,
    UserAvatarUpdateResponse,
    UserCreateParams,
    UserCreateResponse,
    UserDeleteParams,
    UserDeleteResponse,
    UserDemoteParams,
    UserFindEmailResponse,
    UserFindNameResponse,
    UserGetParams,
    UserGetResponse,
    UserProfilePostsGetParams,
    UserProfilePostsGetResponse,
    UserPromoteParams,
    UsersFindEmailParams,
    UsersFindNameParams,
    UsersGetParams,
    UsersGetResponse,
    UserUpdateParams,
    UserUpdateResponse,
)
from .types.vote_type import VoteTypeEnum

__all__ = ("Client",)


class Client:
    """XenForo API Client

    Клиент для взаимодействия c ArzGuard (Xenforo) REST API.

    Параметры
    ----------
    api_key : str
        XenForo API key для аутентификации
    is_super_user: bool
        Если вы используете ключ c правами супер пользователя
    xf_user_id: bool
        ID Пользователя, от лица которого будет выполнено действие, если вы используете ключ c правами супер пользователя

    Ошибки:
    ------
    NoApiKeyProvidedError
        Если апи ключ не передан
    """

    def __init__(
        self,
        api_key: str,
        is_super_user: bool = False,
        xf_user_id: int | None = None,
    ) -> None:
        if api_key == "":
            raise NoApiKeyProvidedError()

        if is_super_user and xf_user_id is None:
            raise NoApiKeyProvidedError(
                "Вы должны предоставить параметр xf_user при использовании ключа с правами super user"
            )

        self._is_super_user = is_super_user
        self.xf_user_id = xf_user_id
        self._http = HTTPClient(api_key, is_super_user, xf_user_id)

    # ============================================================================
    # ALERTS
    # ============================================================================

    async def get_alerts(
        self, params: AlertsGetParams | None = None
    ) -> AlertsGetResponse:
        """GET alerts/ - Получить список оповещений API пользователя

        Параметры
        ----------
        page : int, опционален
            Page number of results
        cutoff : int, опционален
            Unix timestamp самого позднего оповещения
        unviewed : bool, опционален
           Получить только непросмотренные оповещения
        unread : bool, опционален
            Получить только непрочитанные оповещения

        Returns AlertsGetResponse:
        -------
        alerts : List[UserAlert]
            Список оповещений пользователя
        pagination : Pagination
            Информация o пагинации
        """

        if params is not None and not isinstance(params, AlertsGetParams):  # type: ignore
            raise TypeError("Ожидался тип AlertsGetParams")

        payload = await self._http.get_alerts(params)
        return AlertsGetResponse.model_validate(payload)

    async def send_alert(self, params: AlertSendParams) -> AlertSendResponse:
        """POST alerts/ - Отправить оповещение определенному пользователю

        Доступно только для ключа c правами super user

        Параметры
        ----------
        to_user_id : int
            ID пользователя которому нужно отправить оповещение
        alert : str
            Текст оповещения
        from_user_id : int, опционален
            Если предоставлен, пользователь, от которого нужно отправить оповещение. Может быть 0 для анонимного оповещения.
        link_url : str, опционален
            При нажатии на оповещение пользователь перейдет по данному URL.
        link_title : str, опционален
            Текст URL-адреса ссылки, который будет отображен. Если в предупреждении нет текста, он будет добавлен автоматически.

        Returns AlertSendResponse:
        -------
        success : bool
            True если оповещение было успешно отправлено
        """

        if not isinstance(params, AlertSendParams):  # type: ignore
            raise TypeError("Ожидался тип AlertSendParams")

        payload = await self._http.send_alert(params)
        return AlertSendResponse.model_validate(payload)

    async def mark_all_alerts(
        self, params: AlertsMarkAllParams
    ) -> AlertsMarkAllResponse:
        """POST alerts/mark-all - Отметить все оповещения API пользователя как read или viewed

        Параметры
        ----------
        read : bool, опционален
            Отметить все оповещения как прочитанные
        viewed : bool, опционален
            If specified, marks all alerts as viewed. This will remove the alert counter but keep unactioned alerts highlighted.

        Returns AlertsMarkAllResponse:
        -------
        success : bool
            True если операция успешна
        """

        if not isinstance(params, AlertsMarkAllParams):  # type: ignore
            raise TypeError(
                "Ожидался тип AlertsMarkAllParams в параметре params"
            )

        payload = await self._http.mark_all_alerts(params)
        return AlertsMarkAllResponse.model_validate(payload)

    async def get_alert(self, alert_id: int) -> AlertGetResponse:
        """GET alerts/{id}/ - Получить информацию o6 определенном оповещении

        Параметры
        ----------
        alert_id : int
            ID оповещения

        Returns AlertGetResponse:
        -------
        alert : UserAlert
            Информация o6 оповещении
        """

        if not isinstance(alert_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре alert_id")

        payload = await self._http.get_alert(alert_id)
        return AlertGetResponse.model_validate(payload)

    async def mark_alert(
        self, alert_id: int, params: AlertMarkParams
    ) -> AlertMarkResponse:
        """POST alerts/{id}/mark - Отметить оповещение как просмотренное или не просмотренное

        Параметры
        ----------
        alert_id : int
            ID оповещения
        read : bool, опционален
            Отметить оповещение как прочитанное
        unread : bool, опционален
            Отметить оповещение как непрочитанное
        viewed : bool, опционален
            Отметить все оповещения как просмотренные

        Returns AlertMarkResponse:
        -------
        success : bool
            True если операция успешна
        """

        if not isinstance(alert_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре alert_id")

        if not isinstance(params, AlertMarkParams):  # type: ignore
            raise TypeError("Ожидался тип AlertMarkParams в параметре params")

        payload = await self._http.mark_alert(alert_id, params)
        return AlertMarkResponse.model_validate(payload)

    # ============================================================================
    # ATTACHMENTS
    # ============================================================================

    async def get_attachments(self, key: str) -> AttachmentsGetResponse:
        """GET attachments/ - Получить вложения связанные c определенным ключом

        Параметры
        ----------
        key : str
            Ключ вложения

        Returns AttachmentsGetResponse:
        -------
        attachments : List[Attachment]
            Список вложений
        """

        if not isinstance(key, str):  # type: ignore
            raise TypeError("Ожидался тип str в параметре key")

        params = AttachmentsGetParams(key=key)

        payload = await self._http.get_attachments(params)
        return AttachmentsGetResponse.model_validate(payload)

    async def upload_attachment(
        self, key: str, attachment: BinaryIO
    ) -> AttachmentUploadResponse:
        """POST attachments/ - Загрузить вложение

        Параметры
        ----------
        key : str
            Существующий ключ вложения
        attachment : BinaryIO
            Вложение

        Returns AttachmentUploadResponse:
        -------
        attachment : Attachment
            Информация o загруженном вложении

        Ошибки:
        ------
            attachment_key_user_wrong:
                Ключ принадлежит не тому, кто выполняет запрос
        """

        if not isinstance(key, str):  # type: ignore
            raise TypeError("Ожидался тип str в параметре key")

        params = AttachmentUploadParams(key=key)

        payload = await self._http.upload_attachment(params, attachment)
        return AttachmentUploadResponse.model_validate(payload)

    async def create_attachment_key(
        self,
        params: AttachmentsCreateNewKeyParams,
        attachment: BinaryIO | None = None,
    ) -> AttachmentsCreateNewKeyResponse:
        """POST attachments/new-key - Создать новый ключ вложения

        Параметры
        ----------
        type : ContentTypeEnum
            Тип конента вложения
        context : Dict[str, Any], опционален
            Пары ключ - значения, отражающие контекст вложения
        attachment : BinaryIO, опционален
            Первое вложение для ассоциации c ключом

        Returns AttachmentsCreateNewKeyResponse:
        -------
        key : str
            Созданный ключ вложения
        attachment : Attachment, опционален
            Информация o вложении, если оно было предоставлено
        """

        if not isinstance(params, AttachmentsCreateNewKeyParams):  # type: ignore
            raise TypeError("Ожидался тип AttachmentsCreateNewKeyParams")

        payload = await self._http.create_attachment_key(params, attachment)
        return AttachmentsCreateNewKeyResponse.model_validate(payload)

    async def get_attachment(
        self, attachment_id: int
    ) -> AttachmentGetResponse:
        """GET attachments/{id}/ - Получить информацию o6 определенном вложении

        Параметры
        ----------
        attachment_id : int
            ID вложения

        Returns AttachmentGetResponse:
        -------
        attachment : Attachment
        """

        if not isinstance(attachment_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре attachment_id")

        payload = await self._http.get_attachment(attachment_id)
        return AttachmentGetResponse.model_validate(payload)

    async def delete_attachment(
        self, attachment_id: int
    ) -> AttachmentDeleteResponse:
        """DELETE attachments/{id}/ - Удалить вложение

        Параметры
        ----------
        attachment_id : int
            ID вложения

        Returns AttachmentDeleteResponse:
        -------
        success : bool
            True если удаление успешно
        """

        if not isinstance(attachment_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре attachment_id")

        payload = await self._http.delete_attachment(attachment_id)
        return AttachmentDeleteResponse.model_validate(payload)

    async def get_attachment_data(
        self, attachment_id: int
    ) -> AttachmentGetDataResponse:
        """GET attachments/{id}/data - Gets the data that makes up the specified attachment

        Параметры
        ----------
        attachment_id : int
            ID вложения

        Returns AttachmentGetData:
        -------
        data : BinaryIO
            The binary data
        """

        if not isinstance(attachment_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре attachment_id")

        payload = await self._http.get_attachment_data(attachment_id)
        return AttachmentGetDataResponse.model_validate(payload)

    async def get_attachment_thumbnail(
        self, attachment_id: int
    ) -> AttachmentGetThumbnailResponse:
        """GET attachments/{id}/thumbnail - Gets the URL to the attachment's thumbnail

        Параметры
        ----------
        attachment_id : int
            ID вложения

        Returns AttachmentGetThumbnail:
        -------
        url : str
            URL редирект на вложение c 301 кодом

        Ошибки:
        ------
            not_found:
                Вложение не имеет thumbnail
        """

        if not isinstance(attachment_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре attachment_id")

        payload = await self._http.get_attachment_thumbnail(attachment_id)
        return AttachmentGetThumbnailResponse.model_validate(payload)

    # ============================================================================
    # AUTH
    # ============================================================================

    async def test_auth(self, params: AuthTestParams) -> AuthTestResponse:
        """POST auth/ - Проверить логин и пароль пользователя

        Доступно только для ключа c правами super user

        Параметры
        ----------
        login : str
            Username или email
        password : str
            Пароль
        limit_ip : str, опционален
            Будет считаться, что запрос на вход отправляется c него и использоваться для защиты от подбора пароля

        Returns AuthTestResponse:
        -------
        user : User
            Информация o пользователе если аутентификация прошла успешно
        """

        if not isinstance(params, AuthTestParams):  # type: ignore
            raise TypeError("Ожидался тип AuthTestParams в параметре params")

        payload = await self._http.test_auth(params)
        return AuthTestResponse.model_validate(payload)

    async def auth_from_session(
        self, params: AuthFromSessionParams
    ) -> AuthFromSessionResponse:
        """POST auth/from-session - Проверить активную сессию пользователя на основе ID сессии или куки

        Параметры
        ----------
        session_id : str, опционален
            Checks for active session
        remember_cookie : str, опционален
            Checks for active "remember me" cookie

        Returns AuthFromSessionResponse:
        -------
        success : bool
                Если false, сессия или куки не найдены
        user : User
            Если успешно - запись соотвествующего пользователя. Может быть гостем.
        """

        if not isinstance(params, AuthFromSessionParams):  # type: ignore
            raise TypeError(
                "Ожидался тип AuthFromSessionParams в параметре params"
            )

        payload = await self._http.auth_from_session(params)
        return AuthFromSessionResponse.model_validate(payload)

    async def create_login_token(
        self, params: AuthLoginTokenParams
    ) -> AuthLoginTokenResponse:
        """POST auth/login-token - Сгенерировать токен для входа, для авторизации от лица определенного пользователя

        Параметры
        ----------
        user_id : int
            ID пользователя
        limit_ip : str, опционален
            Привязать токен к определенному IP
        return_url : str, опционален
            URL для возврата пользователя после входа в систему
        force : bool, опционален
            Если указано, URL-адрес для входа в систему будет принудительно заменен на имя пользователя, вошедшего в систему в данный момент, если пользователь уже вошел в систему и отличается от текущего пользователя, вошедшего в систему в данный момент. Значение по умолчанию равно false.
        remember: bool
            Определяет, будет ли установлен cookie "запомнить меня" при входе пользователя в систему. По умолчанию установлено true.

        Returns AuthLoginTokenResponse:
        -------
        login_token : str
            Сгенерированный токен для входа
        login_url : str
            URL который можно использовать для входач
        expiry_date : int
            Unix timestamp жизни токена
        """

        if not isinstance(params, AuthLoginTokenParams):  # type: ignore
            raise TypeError(
                "Ожидался тип AuthLoginTokenParams в параметре params"
            )

        payload = await self._http.create_login_token(params)
        return AuthLoginTokenResponse.model_validate(payload)

    # ============================================================================
    # CONVERSATION MESSAGES
    # ============================================================================

    async def reply_conversation_message(
        self, params: ConversationMessageReplyParams
    ) -> ConversationMessageReplyResponse:
        """POST conversation-messages/ - Replies to a conversation

        Параметры
        ----------
        conversation_id : int
            ID беседы
        message : str
            Message content
        attachment_key : str, опционален
            API ключ вложения для загрузки вложений. Тип контента y ключа должен быть conversation_message, в поле context - "conversation_id" = ID этой беседы.

        Returns ConversationMessageReplyResponse:
        -------
        success : bool
            True если сообщение было опубликовано
        message : ConversationMessage
            Опубликованное сообщение
        """

        if not isinstance(params, ConversationMessageReplyParams):  # type: ignore
            raise TypeError(
                "Ожидался тип ConversationMessageReplyParams в параметре params"
            )

        payload = await self._http.reply_conversation_message(params)
        return ConversationMessageReplyResponse.model_validate(payload)

    async def get_conversation_message(
        self, message_id: int
    ) -> ConversationMessageGetResponse:
        """GET conversation-messages/{id}/ - Получить сообщение беседы

        Параметры
        ----------
        message_id : int
            ID сообщения

        Returns ConversationMessageGetResponse:
        -------
        message : ConversationMessage
            Информация o сообщении
        """

        payload = await self._http.get_conversation_message(message_id)
        return ConversationMessageGetResponse.model_validate(payload)

    async def update_conversation_message(
        self, message_id: int, params: ConversationMessageUpdateParams
    ) -> ConversationMessageUpdateResponse:
        """POST conversation-messages/{id}/ - Обновить существующее сообщение

        Параметры
        ----------
        message_id : int
            ID сообщения
        message : str
            Новый текст сообщения
        attachment_key : str, опционален
            Новый ключ вложения

        Returns ConversationMessageUpdateResponse:
        -------
        success : bool
            True если операция успешна
        message : ConversationMessage
            Информация o6 обновленном сообщении
        """

        if not isinstance(message_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре message_id")

        if not isinstance(params, ConversationMessageUpdateParams):  # type: ignore
            raise TypeError(
                "Ожидался тип ConversationMessageUpdateParams в параметре params"
            )

        payload = await self._http.update_conversation_message(
            message_id, params
        )
        return ConversationMessageUpdateResponse.model_validate(payload)

    async def react_conversation_message(
        self, message_id: int, reaction_id: int
    ) -> ConversationMessageReactResponse:
        """POST conversation-messages/{id}/react - Отреагировать на сообщение в беседе

        Параметры
        ----------
        message_id : int
            ID сообщения в беседе
        reaction_id : int
            ID реакции для использования. Используйте этот же ID реакции, чтоб убрать её.

        Returns ConversationMessageReactResponse:
        -------
        success : bool
            True если реакция была добавлена / убрана
        action : ConversationMessageReactActionEnum
            "insert" или "delete"
        """

        if not isinstance(message_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре message_id")

        if not isinstance(reaction_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре reaction_id")

        params = ConversationMessageReactParams(reaction_id=reaction_id)

        payload = await self._http.react_conversation_message(
            message_id, params
        )
        return ConversationMessageReactResponse.model_validate(payload)

    # ============================================================================
    # CONVERSATIONS
    # ============================================================================

    async def get_conversations(
        self, params: ConversationsGetParams | None = None
    ) -> ConversationsGetResponse:
        """GET conversations/ - Получить список бесед API пользователя.

        Параметры
        ----------
        page : int, опционален
            Номер страницы
        starter_id : int, опционален
            Отфильтровать по ID пользователя, начавшего беседу
        receiver_id : int, опционален
            Отфильтровать по ID получателя
        starred : bool, опционален
            Only gets starred conversations
        unread : bool, опционален
            Получить только непрочитанные беседы

        Returns ConversationsGetResponse:
        -------
        conversations : List[Conversation]
            List of conversations
        pagination : Pagination
            Инфрормация o пагинации
        """

        if params is not None and not isinstance(
            params, ConversationsGetParams
        ):  # type: ignore
            raise TypeError(
                "Ожидался тип ConversationsGetParams в параметре params"
            )

        payload = await self._http.get_conversations(params)
        return ConversationsGetResponse.model_validate(payload)

    async def create_conversation(
        self, params: ConversationCreateParams
    ) -> ConversationCreateResponse:
        """POST conversations/ - Создать беседу

        Параметры
        ----------
        recipient_ids : List[int]
            Cпиcoк ID участников беседы
        title : str
            Заголовок беседы
        message : str
            Первое сообщение
        attachment_key : str, опционален
            Ключ вложения
        conversation_open : bool, опционален
            Открыта ли беседа
        open_invite : bool, опционален
            Можно ли приглашать пользователей в беседу

        Returns ConversationCreateResponse:
        -------
        success : bool
            True если беседы была создана
        conversation : Conversation
            Информация o созданной беседе
        """

        if not isinstance(params, ConversationCreateParams):  # type: ignore
            raise TypeError(
                "Ожидался тип ConversationCreateParams в параметре params"
            )

        payload = await self._http.create_conversation(params)
        return ConversationCreateResponse.model_validate(payload)

    async def get_conversation(
        self,
        conversation_id: int,
        params: ConversationGetParams | None = None,
    ) -> ConversationGetResponse:
        """### GET conversations/{id}/ - Получить информацию o беседе

        ### Параметры

        `conversation_id` : `int` - ID беседы
        `with_messages` : `bool`, опционален<br>
            Добавлять ли сообщения беседы в ответ API, в поле `messages` (номер страницы указывается в параметре `page`)
        `page` : `int` - Номер страницы, опционален

        ### Ответ API:  `ConversationGetResponse`

        `conversation` : `Conversation` - Информация o беседе
        `messages` : `List[ConversationMessage]`, опционален<br>
            Список сообщений беседы, если в параметре `with_messages` - `True`
        `pagination` : `Pagination`, опционален<br>
            Информация o пагинации, если в параметре `with_messages` - `True`
        """

        if params is not None and not isinstance(
            params, ConversationGetParams
        ):  # type: ignore
            raise TypeError(
                "Ожидался тип ConversationGetParams в параметре params"
            )

        payload = await self._http.get_conversation(conversation_id, params)
        return ConversationGetResponse.model_validate(payload)

    async def update_conversation(
        self, conversation_id: int, params: ConversationUpdateParams
    ) -> ConversationUpdateResponse:
        """POST conversations/{id}/ - Обновить существующую беседу

        Параметры
        ----------
        conversation_id : int
            ID беседы
        title : str, опционален
            Новый заголовок беседы
        open_invite : bool, опционален
            Доступно ли приглашение новых участников
        conversation_open : bool, опционален
            Закрыта ли беседа

        Returns ConversationUpdateResponse:
        -------
        success : bool
            True если действие успешно
        conversation : Conversation
            Обновленная информация o беседе
        """

        if not isinstance(conversation_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре conversation_id")

        if not isinstance(params, ConversationUpdateParams):  # type: ignore
            raise TypeError(
                "Ожидался тип ConversationUpdateParams в параметре params"
            )

        payload = await self._http.update_conversation(conversation_id, params)
        return ConversationUpdateResponse.model_validate(payload)

    async def delete_conversation(
        self,
        conversation_id: int,
        ignore: bool = False,
    ) -> ConversationDeleteResponse:
        """DELETE conversations/{id}/ - Удалить существую беседу из списка API пользователя

        Параметры
        ----------
        conversation_id : int
            ID беседы
        params : ConversationDeleteParams, опционален
            ignore : bool, опционален
                Игнорировать дальнейшие ответы

        Returns:
        -------
        ConversationDeleteResponse
            success : bool
                True if deletion was successful
        """

        if not isinstance(conversation_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре conversation_id")

        if not isinstance(ignore, bool):  # type: ignore
            raise TypeError("Ожидался тип bool в параметре ignore")

        params = ConversationDeleteParams(ignore=ignore)

        payload = await self._http.delete_conversation(conversation_id, params)
        return ConversationDeleteResponse.model_validate(payload)

    async def invite_conversation(
        self, conversation_id: int, params: ConversationInviteParams
    ) -> ConversationInviteResponse:
        """POST conversations/{id}/invite - Пригласить пользователей в беседу

        Параметры
        ----------
        conversation_id : int
            ID беседы
        recipient_ids : List[int]
            Список из ID пользователей для приглашения их в беседу

        Returns ConversationInviteResponse:
        -------
        ConversationInviteResponse
            success : bool
                True если приглашения были отправлены
        """

        if not isinstance(conversation_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре conversation_id")

        if not isinstance(params, ConversationInviteParams):  # type: ignore
            raise TypeError(
                "Ожидался тип ConversationInviteParams в параметре params"
            )

        payload = await self._http.invite_conversation(conversation_id, params)
        return ConversationInviteResponse.model_validate(payload)

    async def mark_conversation_read(
        self,
        conversation_id: int,
        date: int | None = None,
    ) -> ConversationMarkReadResponse:
        """POST conversations/{id}/mark-read - Отметить беседу как прочитанную вплоть до указанного времени date

        Параметры
        ----------
        conversation_id : int
            ID беседы
        date : int, опционален
            Unix timestamp

        Returns ConversationMarkReadResponse:
        -------
        success : bool
            True если действие успешно
        """

        if not isinstance(conversation_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре conversation_id")

        if date is not None and not isinstance(date, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре date")

        params = (
            ConversationMarkReadParams(date=date) if date is not None else None
        )

        payload = await self._http.mark_conversation_read(
            conversation_id, params
        )
        return ConversationMarkReadResponse.model_validate(payload)

    async def mark_conversation_unread(
        self, conversation_id: int
    ) -> ConversationMarkUnreadResponse:
        """POST conversations/{id}/mark-unread - Отметить беседу как непрочитанную

        Параметры
        ----------
        conversation_id : int
            ID беседы

        Returns ConversationMarkUnreadResponse:
        -------
        success : bool
            True если операция успешна
        """

        if not isinstance(conversation_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре conversation_id")

        payload = await self._http.mark_conversation_unread(conversation_id)
        return ConversationMarkUnreadResponse.model_validate(payload)

    async def get_conversation_messages(
        self,
        conversation_id: int,
        page: int | None = None,
    ) -> ConversationMessagesGetResponse:
        """GET conversations/{id}/messages - Получить сообщения на определенной странице в беседе

        Параметры
        ----------
        conversation_id : int
            ID беседы
        page : int, опционален
            Номер страницы

        Returns ConversationMessagesGetResponse:
        -------
        messages : List[ConversationMessage]
            Список сообщений беседы
        pagination : Pagination
            Инфрормация o пагинации
        """

        if not isinstance(conversation_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре conversation_id")

        if page is not None and not isinstance(page, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре page")

        params = (
            ConversationGetMessagesParams(page=page)
            if page is not None
            else None
        )

        payload = await self._http.get_conversation_messages(
            conversation_id, params
        )
        return ConversationMessagesGetResponse.model_validate(payload)

    async def star_conversation(
        self, conversation_id: int, params: ConversationStarParams
    ) -> ConversationStarResponse:
        """POST conversations/{id}/star - Sets the star status of the specified conversation

        Параметры
        ----------
        conversation_id : int
            ID беседы
        star : bool
            Sets the star status

        Returns ConversationStarResponse:
        -------
        success : bool
            True если операция успешна
        """

        if not isinstance(conversation_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре conversation_id")

        if not isinstance(params, ConversationStarParams):  # type: ignore
            raise TypeError(
                "Ожидался тип ConversationStarParams в параметре params"
            )

        payload = await self._http.star_conversation(conversation_id, params)
        return ConversationStarResponse.model_validate(payload)

    # ============================================================================
    # FORUMS
    # ============================================================================

    async def get_forum(
        self, forum_id: int, params: ForumGetParams | None = None
    ) -> ForumGetResponse:
        """GET forums/{id}/ - Получить информацию o6 определенном форуме

        Параметры
        ----------
        forum_id : int
            ID форума
        with_threads : bool, опционален
            Получить ветки, связанные c данным форумом (параметр page для получения веток на странице)
        page : int, опционален
            Номер страницы
        prefix_id : int, опционален
            Отфильтровать по определенному префиксу
        starter_id : int, опционален
            Отфильтровать по пользователю - создателю
        last_days : int, опционален
            Отфильтровать по ответам за X последних дней
        unread : bool, опционален
            Отфильтровать по непрочитанным веткам
        thread_type : ThreadTypeEnum, опционален
            Отфильтровать по типу треда
        order : OrderField, опционален
            Отфильтровать по определенному полю
        direction : DirectionTypeEnum, опционален
            "asc" или "desc"

        Returns ForumGetResponse:
        -------
        forum : Forum
            Информация o форуме
        threads : List[Thread], опционален
            Список веток, если параметр with_thread = True
        pagination : Pagination, опционален
            Информация o пагинации, если параметр with_thread = True
        sticky : List[Thread], опционален
            Список закрепленных веток
        """

        if not isinstance(forum_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре forum_id")

        if params is not None and not isinstance(params, ForumGetParams):  # type: ignore
            raise TypeError("Ожидался тип ForumGetParams в параметре params")

        payload = await self._http.get_forum(forum_id, params)
        return ForumGetResponse.model_validate(payload)

    async def mark_forum_read(
        self, forum_id: int, date: int | None = None
    ) -> ForumMarkReadResponse:
        """POST forums/{id}/mark-read - Отметить форум прочитанным вплоть до определенного времени date

        Параметры
        ----------
        forum_id : int
            ID форума
        date : int, опционален
            Unix timestamp

        Returns ForumMarkReadResponse:
        -------
        success : bool
            True if operation was successful
        """

        if not isinstance(forum_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре forum_id")

        if date is not None and not isinstance(date, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре date")

        params = ForumMarkReadParams(date=date) if date is not None else None

        payload = await self._http.mark_forum_read(forum_id, params)
        return ForumMarkReadResponse.model_validate(payload)

    async def get_forum_threads(
        self, forum_id: int, params: ForumThreadsGetParams | None = None
    ) -> ForumThreadsGetResponse:
        """GET forums/{id}/threads - Получить список (страница) веток определенного форума

        Параметры
        ----------
        forum_id : int
            ID форума
        page : int, опционален
            Номер страницы
        prefix_id : int, опционален
            Отфильтровать по определенному префиксу
        starter_id : int, опционален
            Отфильтровать по пользователю - создателю
        last_days : int, опционален
            Отфильтровать по ответам за X последних дней
        unread : bool, опционален
            Отфильтровать по непрочитанным веткам
        thread_type : ThreadTypeEnum, опционален
            Отфильтровать по типу треда
        order : OrderField, опционален
            Отфильтровать по определенному полю
        direction : DirectionTypeEnum, опционален
            "asc" или "desc"

        Returns ForumThreadsGetResponse:
        -------
        threads : List[Thread]
            Список веток
        pagination : Pagination
            Инфрормация o пагинации
        sticky : List[Thread], опционален
            Закрепленные ветки
        """

        if not isinstance(forum_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре forum_id")

        if params is not None and not isinstance(
            params, ForumThreadsGetParams
        ):  # type: ignore
            raise TypeError(
                "Ожидался тип ForumThreadsGetParams в параметре params"
            )

        payload = await self._http.get_forum_threads(forum_id, params)
        return ForumThreadsGetResponse.model_validate(payload)

    # ============================================================================
    # INDEX
    # ============================================================================

    async def get_index(self) -> IndexGetResponse:
        """GET index/ - Получиь основную информацию o сайте и API

        Returns IndexGetResponse:
        -------
        version_id : int
            Версия форума
        site_title : str
            Заголовок сайта
        base_url : str
            Base URL
        api_url : str
            API URL
        key : ApiKey
            Информация o6 API ключе
        """

        payload = await self._http.get_index()
        return IndexGetResponse.model_validate(payload)

    # ============================================================================
    # ME (Current User)
    # ============================================================================

    async def get_me(self) -> MeGetResponse:
        """GET me/ - Получить информацию o6 API пользователе

        Returns MeGetResponse:
        -------
        me : User
            Информация o6 API пользователе
        """

        payload = await self._http.get_me()
        return MeGetResponse.model_validate(payload)

    async def update_me(self, params: MeUpdateParams) -> MeUpdateResponse:
        """POST me/ - Обновить информацию o6 API пользователе

        Параметры
        ----------
        option : Option
        profile : Profile
        privacy : Privacy
        visible : bool
        activity_visible : bool
        timezone : str
        custom_title : str
        custom_fields : dict

        Returns MeUpdateResponse:
        -------
        success : bool
            True если действие успешно
        """

        if not isinstance(params, MeUpdateParams):  # type: ignore
            raise TypeError("Ожидался тип MeUpdateParams в параметре params")

        payload = await self._http.update_me(params)
        return MeUpdateResponse.model_validate(payload)

    async def update_my_avatar(
        self, avatar: BinaryIO
    ) -> MeAvatarUpdateResponse:
        """POST me/avatar - Обновить аватар API пользователя

        Параметры
        ----------
        avatar : BinaryIO
            Avatar file

        Returns MeAvatarUpdateResponse:
        -------
        success : bool
            True если операция успешна
        """

        payload = await self._http.update_my_avatar(avatar)
        return MeAvatarUpdateResponse.model_validate(payload)

    async def delete_my_avatar(self) -> MeAvatarDeleteResponse:
        """DELETE me/avatar - Удалить аватар API пользователя

        Returns:
        -------
        success : bool
            True если операция успешна
        """

        payload = await self._http.delete_my_avatar()
        return MeAvatarDeleteResponse.model_validate(payload)

    async def update_my_email(
        self, params: MeEmailUpdateParams
    ) -> MeEmailUpdateResponse:
        """POST me/email - Обновить email API пользователя

        Параметры
        ----------
        current_password : str
            Текущий пароль
        email : str
            Новый email

        Returns MeEmailUpdateResponse:
        -------
        success : bool
            True если операция успешна
        confirmation_required : bool
            Если нужно подтверджение почты
        """

        if not isinstance(params, MeEmailUpdateParams):  # type: ignore
            raise TypeError(
                "Ожидался тип MeEmailUpdateParams в параметре params"
            )

        payload = await self._http.update_my_email(params)
        return MeEmailUpdateResponse.model_validate(payload)

    async def update_my_password(
        self, params: MePasswordUpdateParams
    ) -> MePasswordUpdateResponse:
        """POST me/password - Обновить пароль API пользователя

        Параметры
        ----------
        current_password : str
            Текущий пароль
        new_password : str
            Новый пароль

        Returns MePasswordUpdateResponse:
        -------
        success : bool
            True если операция успешна
        """

        if not isinstance(params, MePasswordUpdateParams):  # type: ignore
            raise TypeError(
                "Ожидался тип MePasswordUpdateParams в параметре params"
            )

        payload = await self._http.update_my_password(params)
        return MePasswordUpdateResponse.model_validate(payload)

    # ============================================================================
    # NODES
    # ============================================================================

    async def get_nodes(self) -> NodesGetResponse:
        """GET nodes/ - Получить дерево нод

        Returns NodesGetResponse:
        -------
        tree_map : Dict[int, List[int]]
            Структура нод, значение - ID ноды, ключ - список из вложенных нод
        nodes : List[Node]
            Список нод
        """

        payload = await self._http.get_nodes()
        return NodesGetResponse.model_validate(payload)

    async def create_node(
        self, params: AnyNodeCreateParams
    ) -> NodeCreateResponse:
        """POST nodes/ - Создать новую ноду

        Классы для создания нод:

        - NodeCreateResponse
        - SearchForumNodeCreateParams
        - CategoryNodeCreateParams
        - PageNodeCreateParams
        - LinkForumNodeCreateParams

        Параметры
        ----------
        node : NodeCreateData
        type_data : поля зависят от типа ноды, опционален

        Returns NodeCreateResponse:
        -------
            node : Node
                Информация o созданной ноде
        """

        if not isinstance(params, AnyNodeCreateParams):  # type: ignore
            raise TypeError(
                "Ожидался один из типов AnyNodeCreateParams в параметре params"
            )

        payload = await self._http.create_node(params)
        return NodeCreateResponse.model_validate(payload)

    async def get_nodes_flattened(self) -> NodesFlattenedGetResponse:
        """GET nodes/flattened - Получение списка нод без tree_map

        Returns NodesFlattenedGetResponse:
        -------
            nodes_flat : List[Node]
                Список нод
        """

        payload = await self._http.get_nodes_flattened()
        return NodesFlattenedGetResponse.model_validate(payload)

    async def get_node(self, node_id: int) -> NodeGetResponse:
        """GET nodes/{id}/ - Получить информацию o ноде

        Параметры
        ----------
        node_id : int
            ID ноды

        Returns NodeGetResponse:
        -------
        node : Node
            Информация o ноде
        """

        if not isinstance(node_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре node_id")

        payload = await self._http.get_node(node_id)
        return NodeGetResponse.model_validate(payload)

    async def update_node(
        self, node_id: int, params: NodeUpdateParams
    ) -> NodeUpdateResponse:
        """POST nodes/{id}/ - Обновить существующую ноду

        Параметры
        ----------
        node_id : int
            ID ноды
        node : NodeUpdateData
        type_data : AnyNodeTypeData
            Соответствует типу обновляемой ноды

        Returns NodeUpdateResponse:
        -------
        node : Node
            Информация o6 обновленной ноде
        """

        if not isinstance(node_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре node_id")

        if not isinstance(params, NodeUpdateParams):  # type: ignore
            raise TypeError("Ожидался тип NodeUpdateParams в параметре params")

        payload = await self._http.update_node(node_id, params)
        return NodeUpdateResponse.model_validate(payload)

    async def delete_node(
        self, node_id: int, delete_children: bool = False
    ) -> NodeDeleteResponse:
        """DELETE nodes/{id}/ - Удалить ноду

        Параметры
        ----------
        node_id : int
            ID ноды
        delete_children : bool, опционален
            Удалить ли вложенные ноды

        Returns NodeDeleteResponse:
        -------
        success : bool
            True если операция успешна
        """

        if not isinstance(node_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре node_id")

        if not isinstance(delete_children, bool):  # type: ignore
            raise TypeError("Ожидался тип bool в параметре delete_children")

        params = NodeDeleteParams(delete_children=delete_children)

        payload = await self._http.delete_node(node_id, params)
        return NodeDeleteResponse.model_validate(payload)

    # ============================================================================
    # POSTS
    # ============================================================================

    async def create_post(
        self, params: PostCreateParams
    ) -> PostCreateResponse:
        """POST posts/ - Создать ответ в ветке

        Параметры
        ----------
        thread_id : int
            ID ветки для ответа
        message : str
            Текст сообщения ответа
        attachment_key : str, опционален
            API ключ вложения для загрузки файлов. Контент тип ключа должен быть post, вместе c context.thread_id = ID данной ветки.

        Returns PostCreateResponse:
        -------
        success : bool
            True если пост был создан
        post : Post
            Созданное сообщение
        """

        if not isinstance(params, PostCreateParams):  # type: ignore
            raise TypeError("Ожидался тип PostCreateParams в параметре params")

        payload = await self._http.create_post(params)
        return PostCreateResponse.model_validate(payload)

    async def get_post(self, post_id: int) -> PostGetResponse:
        """GET posts/{id}/ - Получить информацию o посте

        Параметры
        ----------
        post_id : int
            ID поста

        Returns PostGetResponse:
        -------
        post : Post
            Информация o сообщении
        """

        if not isinstance(post_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре post_id")

        payload = await self._http.get_post(post_id)
        return PostGetResponse.model_validate(payload)

    async def update_post(
        self, post_id: int, params: PostUpdateParams
    ) -> PostUpdateResponse:
        """POST posts/{id}/ - Обновить существующий пост

        Параметры
        ----------
        post_id : int
            ID поста
        message : str
            Новый текст сообщения
        silent : bool, опционален
            Тихое изменение
        clear_edit : bool, опционален
            Очистить историю изменений
        author_alert : bool, опционален
            Отправить уведомление автору
        author_alert_reason : str, опционален
            Причина уведомления
        attachment_key : str, опционален
            Attachment key if including attachments

        Returns PostUpdateResponse:
        -------
        success : bool
            True если операция успешна
        post : Post
            Обновленная информация o посте
        """

        if not isinstance(post_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре post_id")

        if not isinstance(params, PostUpdateParams):  # type: ignore
            raise TypeError("Ожидался тип PostUpdateParams в параметре params")

        payload = await self._http.update_post(post_id, params)
        return PostUpdateResponse.model_validate(payload)

    async def delete_post(
        self, post_id: int, params: PostDeleteParams | None = None
    ) -> PostDeleteResponse:
        """DELETE posts/{id}/ - Удалить пост

        Параметры
        ----------
        post_id : int
            ID поста
        hard_delete : bool, опционален
            Whether to hard delete
        reason : str, опционален
            Причина удаления
        author_alert : bool, опционален
            Отправить уведомление автору
        author_alert_reason : str, опционален
            Причина уведомления

        Returns PostDeleteResponse:
        -------
        success : bool
            True если операция успешна
        """

        if not isinstance(post_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре post_id")

        if params is not None and not isinstance(params, PostDeleteParams):  # type: ignore
            raise TypeError("Ожидался тип PostDeleteParams в параметре params")

        payload = await self._http.delete_post(post_id, params)
        return PostDeleteResponse.model_validate(payload)

    async def mark_post_solution(
        self, post_id: int
    ) -> PostMarkSolutionResponse:
        """POST posts/{id}/mark-solution - Toggle the specified post as the solution to its containing thread

        Параметры
        ----------
        post_id : int
            ID поста

        Returns PostMarkSolutionResponse:
        -------
        true : Any
            Success indicator
        new_solution_post : Post, опционален
            New solution post if set
        old_solution_post : Post, опционален
            Old solution post if changed
        """

        if not isinstance(post_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре post_id")

        payload = await self._http.mark_post_solution(post_id)
        return PostMarkSolutionResponse.model_validate(payload)

    async def react_post(
        self, post_id: int, reaction_id: int
    ) -> PostReactResponse:
        """POST posts/{id}/react - Отреагировать на пост

        Параметры
        ----------
        post_id : int
            ID поста
        reaction_id : int
            ID реакции

        Returns PostReactResponse:
        -------
        success : bool
            True если реакция была добавлена или удалена
        action : PostReactStateEnum
            "insert" или "delete"
        """

        if not isinstance(post_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре post_id")

        if not isinstance(reaction_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре reaction_id")

        params = PostReactParams(reaction_id=reaction_id)

        payload = await self._http.react_post(post_id, params)
        return PostReactResponse.model_validate(payload)

    async def vote_post(
        self, post_id: int, vote_type: VoteTypeEnum
    ) -> PostVoteResponse:
        """POST posts/{id}/vote - Проголосовать в посте

        Параметры
        ----------
        post_id : int
            ID поста
        type : VoteTypeEnum
            "up" или "down"

        Returns PostVoteResponse:
        -------
        success : bool
            True if vote was cast/removed
        action : PostReactStateEnum
            "insert" or "delete"
        """

        if not isinstance(post_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре post_id")

        if not isinstance(vote_type, VoteTypeEnum):  # type: ignore
            raise TypeError("Ожидался тип VoteTypeEnum в параметре vote_type")

        params = PostVoteParams(type=vote_type)

        payload = await self._http.vote_post(post_id, params)
        return PostVoteResponse.model_validate(payload)

    # ============================================================================
    # PROFILE POST COMMENTS
    # ============================================================================

    async def create_profile_post_comment(
        self, params: ProfilePostCommentCreateParams
    ) -> ProfilePostCommentCreateResponse:
        """POST profile-post-comments/ - Отправить комментарий под постом

        Параметры
        ----------
        profile_post_id : int
            ID поста
        message : str
            Текст комментария
        attachment_key : str, опционален
            Attachment key if including attachments

        Returns ProfilePostCommentCreateResponse:
        -------
        success : bool
            True если действие успешно
        comment : ProfilePostComment
            Информация o комментарие
        """

        if not isinstance(params, ProfilePostCommentCreateParams):  # type: ignore
            raise TypeError(
                "Ожидался тип ProfilePostCommentCreateParams в параметре params"
            )

        payload = await self._http.create_profile_post_comment(params)
        return ProfilePostCommentCreateResponse.model_validate(payload)

    async def get_profile_post_comment(
        self, comment_id: int
    ) -> ProfilePostCommentGetResponse:
        """GET profile-post-comments/{id}/ - Получить информацию o комментарие

        Параметры
        ----------
        comment_id : int
            ID комментария

        Returns ProfilePostCommentGetResponse:
        -------
        comment : ProfilePostComment
            Информация o комментарие
        """

        if not isinstance(comment_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре comment_id")

        payload = await self._http.get_profile_post_comment(comment_id)
        return ProfilePostCommentGetResponse.model_validate(payload)

    async def update_profile_post_comment(
        self, comment_id: int, params: ProfilePostCommentUpdateParams
    ) -> ProfilePostCommentUpdateResponse:
        """POST profile-post-comments/{id}/ - Изменить комментарий к посту

        Параметры
        ----------
        comment_id : int
            ID комментария
        message : str, опционален
            Новый текст сообщения
        author_alert : bool, опционален
            Отправить оповещение автору
        author_alert_reason : str, опционален
            Причина оповещения
        attachment_key : str, опционален
            Attachment key if including attachments

        Returns ProfilePostCommentUpdateResponse:
        -------
        success : bool
            True если операция успешна
        comment : ProfilePostComment
            Обновленная информация o комментарие
        """

        if not isinstance(comment_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре comment_id")

        if not isinstance(params, ProfilePostCommentUpdateParams):  # type: ignore
            raise TypeError(
                "Ожидался тип ProfilePostCommentUpdateParams в параметре params"
            )

        payload = await self._http.update_profile_post_comment(
            comment_id, params
        )
        return ProfilePostCommentUpdateResponse.model_validate(payload)

    async def delete_profile_post_comment(
        self,
        comment_id: int,
        params: ProfilePostCommentDeleteParams | None = None,
    ) -> ProfilePostCommentDeleteResponse:
        """DELETE profile-post-comments/{id}/ - Удалить комментарий

        Параметры
        ----------
        comment_id : int
            ID комментария
        hard_delete : bool, опционален
            Whether to hard delete
        reason : str, опционален
            Deletion reason
        author_alert : bool, опционален
            Отправить уведомление автору
        author_alert_reason : str, опционален
            Причина оповещения

        Returns ProfilePostCommentDeleteResponse:
        -------
        success : bool
            True если операция успешна
        """

        if not isinstance(comment_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре comment_id")

        if params is not None and not isinstance(
            params, ProfilePostCommentDeleteParams
        ):  # type: ignore
            raise TypeError(
                "Ожидался тип ProfilePostCommentDeleteParams в параметре params"
            )

        payload = await self._http.delete_profile_post_comment(
            comment_id, params
        )
        return ProfilePostCommentDeleteResponse.model_validate(payload)

    async def react_profile_post_comment(
        self, comment_id: int, reaction_id: int
    ) -> ProfilePostCommentReactResponse:
        """POST profile-post-comments/{id}/react - Отреагировать на комментарий к посту

        Параметры
        ----------
        comment_id : int
            ID комментария
        reaction_id : int
            ID реакции

        Returns ProfilePostCommentReactResponse:
        -------
        success : bool
            True если реакция была добавлена или удалена
        action : PostReactStateEnum
            "insert" or "delete"
        """

        if not isinstance(comment_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре comment_id")

        if not isinstance(reaction_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре reaction_id")

        params = ProfilePostCommentReactParams(reaction_id=reaction_id)

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
        """POST profile-posts/ - Создать новый пост в профиле

        Параметры
        ----------
        user_id : int
            ID пользователя
        message : str
            Post message content
        attachment_key : str, опционален
            Attachment key if including attachments

        Returns ProfilePostCreateResponse:
        -------
        success : bool
            True если действие успешно
        profile_post : ProfilePost
            Информация o созданном посте
        """

        if not isinstance(params, ProfilePostCreateParams):  # type: ignore
            raise TypeError(
                "Ожидался тип ProfilePostCreateParams в параметре params"
            )

        payload = await self._http.create_profile_post(params)
        return ProfilePostCreateResponse.model_validate(payload)

    async def get_profile_post(
        self,
        profile_post_id: int,
        params: ProfilePostGetParams | None = None,
    ) -> ProfilePostGetResponse:
        """GET profile-posts/{id}/ - Получить информацию o посте в профиле пользователя

        Параметры
        ----------
        profile_post_id : int
            ID поста
        with_comments : bool, опционален
            Добавлять ли комментарии к посту в ответ API
        page : int, опционален
            Номер страницы
        direction : DirectionTypeEnum, опционален
            "desc" or "asc"

        Returns ProfilePostGetResponse:
        -------
        profile_post : ProfilePost
            Profile post information
        comments : List[ProfilePostComment], опционален
            Список комментариев, если параметр with_comments = True
        pagination : Pagination, опционален
            Пагинация, если параметр with_comments = True
        """

        if not isinstance(profile_post_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре profile_post_id")

        if params is not None and not isinstance(params, ProfilePostGetParams):  # type: ignore
            raise TypeError(
                "Ожидался тип ProfilePostGetParams в параметре params"
            )

        payload = await self._http.get_profile_post(profile_post_id, params)
        return ProfilePostGetResponse.model_validate(payload)

    async def update_profile_post(
        self, profile_post_id: int, params: ProfilePostUpdateParams
    ) -> ProfilePostUpdateResponse:
        """POST profile-posts/{id}/ - Обновить существующий пост в профиле

        Параметры
        ----------
        profile_post_id : int
            ID поста
        message : str
            Новый текст сообщения
        author_alert : bool, опционален
            Отправить оповещение автору
        author_alert_reason : str, опционален
            Причина оповещения
        attachment_key : str, опционален
            Attachment key if including attachments

        Returns ProfilePostUpdateResponse:
        -------
        success : bool
            True если операция успешна
        profile_post : ProfilePost
            Обновленная информация o посте
        """

        if not isinstance(profile_post_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре profile_post_id")

        if not isinstance(params, ProfilePostUpdateParams):  # type: ignore
            raise TypeError(
                "Ожидался тип ProfilePostUpdateParams в параметре params"
            )

        payload = await self._http.update_profile_post(profile_post_id, params)
        return ProfilePostUpdateResponse.model_validate(payload)

    async def delete_profile_post(
        self,
        profile_post_id: int,
        params: ProfilePostDeleteParams | None = None,
    ) -> ProfilePostDeleteResponse:
        """DELETE profile-posts/{id}/ - Удалить пост из профиля пользователя

        Параметры
        ----------
        profile_post_id : int
            ID поста
        hard_delete : bool, опционален
            Whether to hard delete
        reason : str, опционален
            Причина удаления
        author_alert : bool, опционален
            Отправить оповещение автору
        author_alert_reason : str, опционален
            Причина отправки оповещения

        Returns ProfilePostDeleteResponse:
        -------
        success : bool
            True если действие успешно
        """

        if not isinstance(profile_post_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре profile_post_id")

        if params is not None and not isinstance(
            params, ProfilePostDeleteParams
        ):  # type: ignore
            raise TypeError(
                "Ожидался тип ProfilePostDeleteParams в параметре params"
            )

        payload = await self._http.delete_profile_post(profile_post_id, params)
        return ProfilePostDeleteResponse.model_validate(payload)

    async def get_profile_post_comments(
        self,
        profile_post_id: int,
        params: ProfilePostCommentsGetParams | None = None,
    ) -> ProfilePostCommentsGetResponse:
        """GET profile-posts/{id}/comments - Получить комментарии поста из профиля юзера

        Параметры
        ----------
        profile_post_id : int
            ID поста
        page : int, опционален
            Номер страницы
        direction : DirectionTypeEnum, опционален
            "desc" или "asc"

        Returns ProfilePostCommentsGetResponse:
        -------
        comments : List[ProfilePostComment]
            Список комментариев
        pagination : Pagination
            Инфрормация o пагинации
        """

        if not isinstance(profile_post_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре profile_post_id")

        if params is not None and not isinstance(
            params, ProfilePostCommentsGetParams
        ):  # type: ignore
            raise TypeError(
                "Ожидался тип ProfilePostCommentsGetParams в параметре params"
            )

        payload = await self._http.get_profile_post_comments(
            profile_post_id, params
        )
        return ProfilePostCommentsGetResponse.model_validate(payload)

    async def react_profile_post(
        self, profile_post_id: int, reaction_id: int
    ) -> ProfilePostReactResponse:
        """POST profile-posts/{id}/react - Отреагировать на пост в профиле пользователя

        Параметры
        ----------
        profile_post_id : int
            ID поста
        reaction_id : int
            ID реакции

        Returns ProfilePostReactResponse:
        -------
        success : bool
            True если реакция была добавлена или удалена
        action : PostReactStateEnum
            "insert" или "delete"
        """

        if not isinstance(profile_post_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре profile_post_id")

        if not isinstance(reaction_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре reaction_id")

        params = ProfilePostReactParams(reaction_id=reaction_id)

        payload = await self._http.react_profile_post(profile_post_id, params)
        return ProfilePostReactResponse.model_validate(payload)

    # ============================================================================
    # STATS
    # ============================================================================

    async def get_stats(self) -> StatsResponse:
        """GET stats/ - Получить статистику сайта и основную информацию o6 активности

        Returns StatsResponse:
        -------
        totals : Totals
            Total counts for threads, messages, users
        latest_user : LatestUser
            Latest registered user information
        online : Online
            Online user counts
        """

        payload = await self._http.get_stats()
        return StatsResponse.model_validate(payload)

    # ============================================================================
    # THREADS
    # ============================================================================

    async def get_threads(
        self, params: ThreadsGetParams | None = None
    ) -> ThreadsGetResponse:
        """GET threads/ - Получить список веток

        Параметры
        ----------
        page : int, опционален
            Номер страницы
        prefix_id : int, опционален
            Отфильтровать по префиксу
        starter_id : int, опционален
            Отфильтровать по пользователю, начавшему ветку
        last_days : int, опционален
            Отфильтровать по ответам за последние X дней
        unread : bool, опционален
            Отфильтровать по непрочитанным веткам
        thread_type : ThreadTypeEnum, опционален
            Отфильтровать по типу ветки
        order : OrderField, опционален
            Отфильтровать по определенному полю
        direction : DirectionTypeEnum, опционален
            "asc" или "desc"

        Returns ThreadsGetResponse:
        -------
        threads : List[Thread]
            Список веток
        pagination : Pagination
            Инфрормация o пагинации
        """

        if params is not None and not isinstance(params, ThreadsGetParams):  # type: ignore
            raise TypeError("Ожидался тип ThreadsGetParams в параметре params")

        payload = await self._http.get_threads(params)
        return ThreadsGetResponse.model_validate(payload)

    async def create_thread(
        self, params: ThreadCreateParams
    ) -> ThreadCreateResponse:
        """POST threads/ - Создать ветку

        Параметры
        ----------
        node_id : int
            ID форума для создания ветки в нем
        title : str
            Заголовок ветки
        message : str
            Текст первого сообщения в ветке
        discussion_type : str, опционален
            Discussion type
        prefix_id : int, опционален
            Префикс ветки
        tags : List[str], опционален
            Список тегов
        custom_fields : dict, опционален
            Custom field values
        discussion_open : bool, опционален
            Открыта ли ветка
        sticky : bool, опционален
            Закреплена ли ветка
        attachment_key : str, опционален
            Ключ вложения если ветка включает в себя вложения

        Returns ThreadCreateResponse:
        -------
        success : bool
            True если действие успешно
        thread : Thread
            Информация o созданной ветке

        Ошибки:
        ------
            no_permission:
                Нет прав для создания ветки.
        """

        if not isinstance(params, ThreadCreateParams):  # type: ignore
            raise TypeError(
                "Ожидался тип ThreadCreateParams в параметре params"
            )

        payload = await self._http.create_thread(params)
        return ThreadCreateResponse.model_validate(payload)

    async def get_thread(
        self, thread_id: int, params: ThreadGetParams | None = None
    ) -> ThreadGetResponse:
        """GET threads/{id}/ - Получить информацию o ветке

        Параметры
        ----------
        thread_id : int
            ID ветки
        params : ThreadGetParams, опционален
            with_posts : bool, опционален
                Включая посты в ветке в ответ от API
            with_first_post : bool, опционален
                Включить ли первый пост
            page : int, опционален
                Номер страницы

        Returns ThreadGetResponse:
        -------
        thread : Thread
            Информация o ветке
        posts : List[Post], опционален
            Список постов, если параметр with_posts = True
        pagination : Pagination, опционален
            Пагинация, если параметр with_posts = True
        """

        if not isinstance(thread_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре thread_id")

        if params is not None and not isinstance(params, ThreadGetParams):  # type: ignore
            raise TypeError("Ожидался тип ThreadGetParams в параметре params")

        payload = await self._http.get_thread(thread_id, params)
        return ThreadGetResponse.model_validate(payload)

    async def update_thread(
        self, thread_id: int, params: ThreadUpdateParams
    ) -> ThreadUpdateResponse:
        """POST threads/{id}/ - Обновить существующую ветку

        Параметры
        ----------
        thread_id : int
            ID ветки
        title : str, опционален
            Новый заголовок ветки
        prefix_id : int, опционален
            Новый префикс
        tags : List[str], опционален
            Список тегов
        custom_fields : dict, опционален
            Custom field values
        discussion_open : bool, опционален
            Открыта ли ветка
        sticky : bool, опционален
            Закреплена ли ветка

        Returns ThreadUpdateResponse:
        -------
        success : bool
            True если действие успешно
        thread : Thread
            Обновленная информация o ветке
        """

        if not isinstance(thread_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре thread_id")

        if not isinstance(params, ThreadUpdateParams):  # type: ignore
            raise TypeError(
                "Ожидался тип ThreadUpdateParams в параметре params"
            )

        payload = await self._http.update_thread(thread_id, params)
        return ThreadUpdateResponse.model_validate(payload)

    async def delete_thread(
        self, thread_id: int, params: ThreadDeleteParams | None = None
    ) -> ThreadDeleteResponse:
        """DELETE threads/{id}/ - Удалить ветку

        Параметры
        ----------
        thread_id : int
            ID ветки
        hard_delete : bool, опционален
            Whether to hard delete
        reason : str, опционален
            Причина удаления
        author_alert : bool, опционален
            Отправить оповещение автору
        author_alert_reason : str, опционален
            Текст оповещения
        starter_alert : bool, опционален
            Отправить оповещения пользователю, начавшему ветку
        starter_alert_reason : str, опционален
            Текст оповещения

        Returns ThreadDeleteResponse:
        -------
        success : bool
            True если действие успешно
        """

        if not isinstance(thread_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре thread_id")

        if params is not None and not isinstance(params, ThreadDeleteParams):  # type: ignore
            raise TypeError(
                "Ожидался тип ThreadDeleteParams в параметре params"
            )

        payload = await self._http.delete_thread(thread_id, params)
        return ThreadDeleteResponse.model_validate(payload)

    async def change_thread_type(
        self, thread_id: int, new_thread_type: ThreadTypeEnum
    ) -> ThreadChangeTypeResponse:
        """POST threads/{id}/change-type - Сменить тип ветки

        Параметры
        ----------
        thread_id : int
            ID of the thread
        new_thread_type : ThreadTypeEnum
            Новый тип ветки

        Returns ThreadChangeTypeResponse:
        -------
        success : bool
            True если действие успешно
        thread : Thread
            Обновленная информация o ветке
        """

        if not isinstance(thread_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре thread_id")

        if not isinstance(new_thread_type, ThreadTypeEnum):  # type: ignore
            raise TypeError(
                "Ожидался тип ThreadTypeEnum в параметре new_thread_type"
            )

        params = ThreadChangeTypeParams(new_thread_type_id=new_thread_type)

        payload = await self._http.change_thread_type(thread_id, params)
        return ThreadChangeTypeResponse.model_validate(payload)

    async def mark_thread_read(
        self, thread_id: int, date: int
    ) -> ThreadMarkReadResponse:
        """POST threads/{id}/mark-read - Отметить ветку как прочитанную вплоть до времени date

        Параметры
        ----------
        thread_id : int
            ID ветки
        date : int
            Unix timestamp

        Returns ThreadMarkReadResponse:
        -------
        success : bool
            True если операция успешна
        """

        if not isinstance(thread_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре thread_id")

        if not isinstance(date, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре date")

        params = ThreadMarkReadParams(date=date)

        payload = await self._http.mark_thread_read(thread_id, params)
        return ThreadMarkReadResponse.model_validate(payload)

    async def move_thread(
        self, thread_id: int, params: ThreadMoveParams
    ) -> ThreadMoveResponse:
        """POST threads/{id}/move - Переместить ветку на другой форум

        Параметры
        ----------
        thread_id : int
            ID ветки
        node_id : int
            ID целевого форума
        notify_watchers : bool, опционален
            Notify watchers of move
        starter_alert : bool, опционален
            Send alert to thread starter
        starter_alert_reason : str, опционален
            Reason for starter alert
        prefix_id : int, опционален
            ID нового префикса

        Returns ThreadMoveResponse:
        -------
        success : bool
            True если операция успешна
        thread : Thread
            Обновленная информация o ветке
        """

        if not isinstance(thread_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре thread_id")

        if not isinstance(params, ThreadMoveParams):  # type: ignore
            raise TypeError("Ожидался тип ThreadMoveParams в параметре params")

        payload = await self._http.move_thread(thread_id, params)
        return ThreadMoveResponse.model_validate(payload)

    async def get_thread_posts(
        self, thread_id: int, params: ThreadPostsGetParams | None = None
    ) -> ThreadPostsGetResponse:
        """GET threads/{id}/posts - Получить посты из ветки

        Параметры
        ----------
        thread_id : int
            ID ветки
        page : int, опционален
            Номер страницы

        Returns ThreadPostsGetResponse:
        -------
        posts : List[Post]
            Список постов ветки
        pagination : Pagination
            Инфрормация o пагинации
        """

        if not isinstance(thread_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре thread_id")

        if params is not None and not isinstance(params, ThreadPostsGetParams):  # type: ignore
            raise TypeError(
                "Ожидался тип ThreadPostsGetParams в параметре params"
            )

        payload = await self._http.get_thread_posts(thread_id, params)
        return ThreadPostsGetResponse.model_validate(payload)

    async def vote_thread(
        self, thread_id: int, vote_type: VoteTypeEnum
    ) -> ThreadVoteResponse:
        """POST threads/{id}/vote - Проголосовать в ветке

        Параметры
        ----------
        thread_id : int
            ID ветки
        type : VoteTypeEnum
            "up" или "down"

        Returns ThreadVoteResponse:
        -------
        success : bool
            True if vote was cast/removed
        action : PostReactStateEnum
            "insert" или "delete"
        """

        if not isinstance(thread_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре thread_id")

        if not isinstance(vote_type, VoteTypeEnum):  # type: ignore
            raise TypeError("Ожидался тип VoteTypeEnum в параметре vote_type")

        params = ThreadVoteParams(type=vote_type)

        payload = await self._http.vote_thread(thread_id, params)
        return ThreadVoteResponse.model_validate(payload)

    # ============================================================================
    # USERS
    # ============================================================================

    async def get_users(
        self, params: UsersGetParams | None = None
    ) -> UsersGetResponse:
        """GET users/ - Получить список пользователей

        Параметры
        ----------
        page : int, опционален
            Номер страницы

        Returns UsersGetResponse:
        -------
        users : List[User]
            Список пользователей
        pagination : Pagination
            Инфрормация o пагинации
        """

        if params is not None and not isinstance(params, UsersGetParams):  # type: ignore
            raise TypeError("Ожидался тип UsersGetParams в параметре params")

        payload = await self._http.get_users(params)
        return UsersGetResponse.model_validate(payload)

    async def create_user(
        self, params: UserCreateParams
    ) -> UserCreateResponse:
        """POST users/ - Создать нового пользователя

        Параметры
        ----------
        username : str
            Username
        email : str
            Email address
        password : str
            Пароль

        Returns UserCreateResponse:
        -------
        success : bool
            True если операция успешна
        user : User
            Информация o созданном пользователе
        """

        if not isinstance(params, UserCreateParams):  # type: ignore
            raise TypeError("Ожидался тип UserCreateParams в параметре params")

        payload = await self._http.create_user(params)
        return UserCreateResponse.model_validate(payload)

    async def find_user_by_email(self, email: str) -> UserFindEmailResponse:
        """GET users/find-email - Найти пользователя по email

        Параметры
        ----------
        email : str
            Email для поиска по нему пользователя

        Returns UserFindEmailResponse:
        -------
        user : User, опционален
            Пользователь, если найден
        """

        if not isinstance(email, str):  # type: ignore
            raise TypeError("Ожидался тип str в параметре email")

        params = UsersFindEmailParams(email=email)

        payload = await self._http.find_user_by_email(params)
        return UserFindEmailResponse.model_validate(payload)

    async def find_user_by_name(self, username: str) -> UserFindNameResponse:
        """GET users/find-name - Найти пользователей по username

        Параметры
        ----------
        username : str
            Username для поиска по нему пользователей

        Returns UserFindNameResponse:
        -------
        exact : User, опционален
            Пользователь, если найден
        recommendations : List[User], опционален
            Пользователи c похожими usernames
        """

        if not isinstance(username, str):  # type: ignore
            raise TypeError("Ожидался тип str в параметре username")

        params = UsersFindNameParams(username=username)

        payload = await self._http.find_user_by_name(params)
        return UserFindNameResponse.model_validate(payload)

    async def get_user(
        self, user_id: int, params: UserGetParams | None = None
    ) -> UserGetResponse:
        """GET users/{id}/ - Получить информацию o6 определенном пользователе

        Параметры
        ----------
        user_id : int
            ID пользователя
        with_posts : bool, опционален
            Для предоставления информации o постах в профиле пользователя (страница зависит от параметра page)
        page : int
            Номер страницы

        Returns UserGetResponse:
        -------
        user : User
            Информация o пользователе
        """

        if not isinstance(user_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре user_id")

        if params is not None and not isinstance(params, UserGetParams):  # type: ignore
            raise TypeError("Ожидался тип UserGetParams в параметре params")

        payload = await self._http.get_user(user_id, params)
        return UserGetResponse.model_validate(payload)

    async def update_user(
        self, user_id: int, params: UserUpdateParams
    ) -> UserUpdateResponse:
        """POST users/{id}/ - Обновить существующего пользователя

        Параметры
        ----------
        user_id : int
            ID пользователя
        username : str, опционален
            New username
        email : str, опционален
            New email
        user_group_id : int, опционален
            Primary user group
        secondary_group_ids : List[int], опционален
            Secondary groups
        custom_title : str, опционален
            Custom title
        is_staff : bool, опционален
            Staff status
        visible : bool, опционален
            Видимость

        Returns UserUpdateResponse:
        -------
        success : bool
            True если операция успешна
        user : User
            Updated user information
        """

        if not isinstance(user_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре user_id")

        if not isinstance(params, UserUpdateParams):  # type: ignore
            raise TypeError("Ожидался тип UserUpdateParams в параметре params")

        payload = await self._http.update_user(user_id, params)
        return UserUpdateResponse.model_validate(payload)

    async def delete_user(
        self, user_id: int, rename_to: str | None = None
    ) -> UserDeleteResponse:
        """DELETE users/{id}/ - Удалить пользователя

        Параметры
        ----------
        user_id : int
            ID пользователя
        rename_to : str, опционален
            Новый ник для указания авторства контента удаленного пользователя

        Returns UserDeleteResponse:
        -------
        success : bool
            True если операция успешна
        """

        if not isinstance(user_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре user_id")

        if rename_to is not None and not isinstance(rename_to, str):  # type: ignore
            raise TypeError("Ожидался тип str в параметре rename_to")

        params = (
            UserDeleteParams(rename_to=rename_to)
            if rename_to is not None
            else None
        )

        payload = await self._http.delete_user(user_id, params)
        return UserDeleteResponse.model_validate(payload)

    async def update_user_avatar(
        self, user_id: int, avatar: BinaryIO
    ) -> UserAvatarUpdateResponse:
        """POST users/{id}/avatar - Обновить аватар пользователя

        Параметры
        ----------
        user_id : int
            ID пользователя
        avatar : BinaryIO
            Avatar file

        Returns UserAvatarUpdateResponse:
        -------
        success : bool
            True если операция успешна
        """

        if not isinstance(user_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре user_id")

        payload = await self._http.update_user_avatar(user_id, avatar)
        return UserAvatarUpdateResponse.model_validate(payload)

    async def delete_user_avatar(
        self, user_id: int
    ) -> UserAvatarDeleteResponse:
        """DELETE users/{id}/avatar - Удалить аватар пользователя

        Параметры
        ----------
        user_id : int
            ID пользователя

        Returns UserAvatarDeleteResponse:
        -------
        success : bool
            True если операция успешна
        """

        if not isinstance(user_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре user_id")

        payload = await self._http.delete_user_avatar(user_id)
        return UserAvatarDeleteResponse.model_validate(payload)

    async def get_user_profile_posts(
        self, user_id: int, page: int | None
    ) -> UserProfilePostsGetResponse:
        """GET users/{id}/profile-posts - Получить список постов в профиле пользователя

        Параметры
        ----------
        user_id : int
            ID пользователя
        page : int, опционален
            Номер страницы

        Returns UserProfilePostsGetResponse:
        -------
        profile_posts : List[ProfilePost]
            Список постов профиля
        pagination : Pagination
            Инфрормация o пагинации
        """

        if not isinstance(user_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре user_id")

        if page is not None and not isinstance(page, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре page")

        params = (
            UserProfilePostsGetParams(page=page) if page is not None else None
        )
        payload = await self._http.get_user_profile_posts(user_id, params)
        return UserProfilePostsGetResponse.model_validate(payload)

    # ============================================================================
    # ACTIONS
    # ============================================================================

    async def get_demote_groups(self) -> GetDemoteGroupsResponse:
        """GET demote/ - Получить список групп, которые API пользователь может удалять

        Returns GetDemoteGroupsResponse:
        -------
        success : bool
            True, если операция успешна
        groups : Dict[ArzGuardGroupsIdsEnum, ArzGuardGroupsNamesEnum]
            Пары ключ - значение, ключ - ID, значение - название

        """

        payload = await self._http.get_demote_groups()
        return GetDemoteGroupsResponse.model_validate(payload)

    async def demote_user(
        self, user_id: int, group_id: ArzGuardGroupsIdsEnum
    ) -> DemoteUserResponse:
        """POST demote/{user_id}/ - удалить y юзера определенную группу

        Параметры
        ----------
        user_id : int
            ID пользователя
        group_id : ArzGuardGroupsIdsEnum
            ID группы для удаления y пользователя

        Returns DemoteUserResponse:
        -------
        success : bool
            Operation status
        groups : List[ArzGuardGroupsNamesEnum]
            Список названий групп y пользователя
        user : User, опционален
            Информация o пользователе (включен только при наличии права user:read y API ключа)

        Ошибки
        ------
            user_id_not_valid:
                Неверный ID пользователя
            user_cannot_promote:
                Пользователь не может быть изменен
            group_not_allowed:
                Нет прав для снятия группы
        """

        if not isinstance(user_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре user_id")

        if not isinstance(group_id, ArzGuardGroupsIdsEnum):  # type: ignore
            raise TypeError(
                "Ожидался тип ArzGuardGroupsIdsEnum в параметре group_id"
            )

        params = UserDemoteParams(group=group_id)
        payload = await self._http.demote_user(user_id, params)
        return DemoteUserResponse.model_validate(payload)

    async def get_promote_groups(self) -> GetPromoteGroupsResponse:
        """GET promote/ - Получить список групп, которые API пользователь может выдавать

        Returns GetPromoteGroupsResponse:
        -------
        success : bool
            True, если операция успешна
        groups : Dict[ArzGuardGroupsIdsEnum, ArzGuardGroupsNamesEnum]
            Пары ключ - значение, ключ - ID, значение - название
        """

        payload = await self._http.get_promote_groups()
        return GetPromoteGroupsResponse.model_validate(payload)

    async def promote_user(
        self, user_id: int, group_id: ArzGuardGroupsIdsEnum
    ) -> PromoteUserResponse:
        """POST promote/{user_id}/ - выдать пользователю определенную группу

        Параметры
        ----------
        user_id : int
            ID пользователя
        group_id : ArzGuardGroupsIdsEnum
            ID группы, которую нужно выдать

        Returns PromoteUserResponse:
        -------
        success : bool
            True, если операция успешна
        groups : List[ArzGuardGroupsNamesEnum]
            Список названий групп y пользователя
        user : User, опционален
            Информация o пользователе (включен только при наличии права user:read y API ключа)

        Ошибки:
        ------
            user_id_not_valid:
                Неизвестный ID пользователя
            user_cannot_promote:
                Пользователь не может быть изменен
            group_not_allowed:
                Y вас нет прав для выдачи данной группы
        """

        if not isinstance(user_id, int):  # type: ignore
            raise TypeError("Ожидался тип int в параметре user_id")

        if not isinstance(group_id, ArzGuardGroupsIdsEnum):  # type: ignore
            raise TypeError(
                "Ожидался тип ArzGuardGroupsIdsEnum в параметре group_id"
            )

        params = UserPromoteParams(group=group_id)
        payload = await self._http.promote_user(user_id, params)
        return PromoteUserResponse.model_validate(payload)
