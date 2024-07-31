import strawberry
from strawberry.types.base import StrawberryType


@strawberry.type
class Query:
    hello: str = strawberry.field(resolver=get_hello)


def get_hello():
    return "Hello world"
