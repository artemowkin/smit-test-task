from fastapi import HTTPException, status
from tortoise.exceptions import DoesNotExist


def handle_doesnt_exist(detail_message: str):
    """Decorator that handles DoesNotExist exception"""

    def decorator(func):

        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except DoesNotExist:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail_message.format(*args, **kwargs))

        return wrapper

    return decorator
