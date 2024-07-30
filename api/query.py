import strawberry
from strawberry.types.base import StrawberryType


@strawberry.type
class Query:
    hello: str
