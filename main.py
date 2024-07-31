from strawberry import schema
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI
from api.schema import schema

app = FastAPI()
graphql_router = GraphQLRouter(schema, path="/", graphql_ide="appllo-sandbox")
app.include_router(graphql_router)
