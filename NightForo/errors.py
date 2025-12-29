class BaseException(Exception):
    pass


class XenForoError(Exception):
    def __init__(self, msg: object) -> None:
        super().__init__(msg)


class UnsupportedEndpointMethod(XenForoError):
    pass


class NoApiKeyProvided(BaseException):
    pass
