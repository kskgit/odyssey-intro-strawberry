import strawberry


@strawberry.type
class Playlist:
    id: strawberry.ID
    name: str
    description: str | None
