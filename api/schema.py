import strawberry
from strawberry.federation import schema
from .query import Query
from .types.playlist import Playlist

schema = strawberry.Schema(query=Query, types=[Playlist])
