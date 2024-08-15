import strawberry

from api.mutation import Mutation
from .query import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)
