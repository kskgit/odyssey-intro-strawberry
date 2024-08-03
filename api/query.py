import strawberry
from .types.playlist import Playlist


@strawberry.type(description="Playlist hand-picked to be featured to all users.")
class Query:
    @strawberry.field
    def featured_playlists(self) -> list[Playlist]:
        return [
            Playlist(id="1", name="GraphQL Groovin", description=None),
            Playlist(id="2", name="GraphQL Explorer Jams", description=None),
            Playlist(id="3", name="Interpretive GraphQL Dance", description=None),
        ]
