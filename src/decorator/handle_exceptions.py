from functools import wraps
from src.errors.types import NotFoundConfig, NotFoundError, DateError, ExistingRegistry, ValueError


class Exceptions:
    def __init__(self, func):
        self.func = func
        wraps(func)(self.func)

    def __get__(self, instance, owner):
        return lambda *args, **kwargs: self.__call__(instance, *args, **kwargs)

    def __call__(self, instance, *args, **kwargs):
        try:
            return self.func(instance, *args, **kwargs)
        except (ValueError, DateError, ExistingRegistry, NotFoundConfig, NotFoundError) as exception:
            return {"status": exception.code, "data": {'error':str(exception)}}
        except Exception as e:
            return {"status": 500, "data": f'{e}'}
