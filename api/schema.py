import strawberry
from strawberry.federation import schema
from .query import Query

schema = strawberry.Schema(query=Query)
