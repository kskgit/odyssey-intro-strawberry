from strawberry import schema
from stawberry.fastapi import GraphQLRouter
from fastapi import FastAPI

app = FastAPI()
graphql_router = GraphQLRouter(schema, path="/", graphql_ide="appllo-sandbox")
app.include_router(graphql_router)
