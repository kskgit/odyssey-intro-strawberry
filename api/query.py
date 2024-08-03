import strawberry
from strawberry.types.base import StrawberryType


def get_hello():
    return "Hello world"


@strawberry.type
class Query:
    hello: str = strawberry.field(resolver=get_hello)
