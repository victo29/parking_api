from functools import wraps
from src.errors.types.not_found_error import NotFoundError
from src.errors.types.existing_registry import ExistingRegistry
from src.errors.types.date_error import DateError


class Exceptions:
    def __init__(self, func):
        self.func = func
        wraps(func)(self.func)

    def __get__(self, instance, owner):
        return lambda *args, **kwargs: self.__call__(instance, *args, **kwargs)

    def __call__(self, instance, *args, **kwargs):
        try:
            return self.func(instance, *args, **kwargs)
        except NotFoundError as exception:
            return {"status": 404, "data": {'error':str(exception)}}
        except (ValueError, DateError, ExistingRegistry) as exception:
            return {"status": 400, "data": {'error':str(exception)}}
        except Exception as e:
            return {"status": 500, "data": f'{e}'}
