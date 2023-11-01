from abc import ABC, abstractmethod


class Request:
    def __init__(self):
        self.user = "dummy_user"
        self.resource = "dummy_resource"


class Response:
    ...


class ErrorResponse(Response):
    ...


class RequestHandlerInterface(ABC):
    @abstractmethod
    def handle(self, request: Request) -> Response:
        raise NotImplementedError


class AbstractCheckedHandler(RequestHandlerInterface):
    def handle(self, request: Request) -> Response:
        if self.__check_commonly(request) and self.check_externally(request):
            request = self.__preprocess_request(request)
            response = self.request_to_response(request)
            return self.__postprocess_response(response)
        else:
            return ErrorResponse()

    def __check_commonly(self, request: Request) -> bool:
        return True  # dummy

    @abstractmethod
    def check_externally(self, request: Request) -> bool:
        raise NotImplementedError

    def __preprocess_request(self, request: Request) -> Request:
        return Request()  # dummy

    @abstractmethod
    def request_to_response(self, request: Request) -> Response:
        raise NotImplementedError

    def __postprocess_response(self, response: Response) -> Response:
        return Response()  # dummy


class UserAccessCheckerInterface(ABC):
    @abstractmethod
    def is_allowed(self, user) -> bool:
        raise NotImplementedError


class UserAccessCheckedHandler(AbstractCheckedHandler):
    def __init__(
        self, user_access_checker: UserAccessCheckerInterface
    ) -> None:
        self.user_access_checker = user_access_checker

    def check_externally(self, request: Request) -> bool:
        print(self.__class__.__name__, "check_externally")
        return self.user_access_checker.is_allowed(request.user)

    def request_to_response(self, request: Request) -> Response:
        print(self.__class__.__name__, "request_to_response")
        return Response()


class ResourceCheckerInterface(ABC):
    @abstractmethod
    def is_allowed(self, resource) -> bool:
        raise NotImplementedError


class ResourceCheckedHandler(AbstractCheckedHandler):
    def __init__(self, resource_checker: ResourceCheckerInterface) -> None:
        self.resource_checker = resource_checker

    def check_externally(self, request: Request) -> bool:
        print(self.__class__.__name__, "check_externally")
        return self.resource_checker.is_allowed(request.resource)

    def request_to_response(self, request: Request) -> Response:
        print(self.__class__.__name__, "request_to_response")
        return Response()


class AwesomeUserAccessChecker(UserAccessCheckerInterface):
    def is_allowed(self, user) -> bool:
        return True


class FabulousResourceChecker(ResourceCheckerInterface):
    def is_allowed(self, resource) -> bool:
        return True


if __name__ == "__main__":
    UserAccessCheckedHandler(AwesomeUserAccessChecker()).handle(Request())
    print()
    ResourceCheckedHandler(FabulousResourceChecker()).handle(Request())

"""
UserAccessCheckedHandler check_externally
UserAccessCheckedHandler request_to_response

ResourceCheckedHandler check_externally
ResourceCheckedHandler request_to_response
"""
