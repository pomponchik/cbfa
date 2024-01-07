from typing import Callable, Type, Optional, Any

from fastapi import FastAPI


class ClassBased:
    methods = (
        'get',
        'post',
        'put',
        'delete',
        'trace',
        'head',
        'options',
        'connect',
        'patch',
    )

    def __init__(self, app: FastAPI) -> None:
        self.app = app

    def __call__(self, *args: Any, **kwargs: Any) -> Callable[[Type[Any]], Type[Any]]:
        def decorator(Class: Type[Any]) -> Type[Any]:
            for method_name in self.methods:
                if hasattr(Class, method_name):
                    fastapi_decorator_fabrique = self.get_fastapi_decorator_fabrique(method_name)
                    if fastapi_decorator_fabrique is not None:
                        fast_api_decorator = fastapi_decorator_fabrique(*args, **kwargs)
                        new_method = getattr(Class, method_name)
                        new_method.__name__ = f'{Class.__name__.lower()}_{method_name}'
                        new_method = fast_api_decorator(new_method)
                        setattr(Class, method_name, new_method)
            return Class
        return decorator

    def get_fastapi_decorator_fabrique(self, method_name: str) -> Optional[Callable[..., Any]]:
        return getattr(self.app, method_name, None)
