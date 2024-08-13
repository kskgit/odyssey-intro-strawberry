import strawberry

from api.types.track import Track


@strawberry.type(
    description="A curated collection of tracks designed for a specific activity or mood."
)
class Playlist:
    id: strawberry.ID = strawberry.field(description="The ID for the playlist.")
    name: str = strawberry.field(description="The name of the playlist")
    description: str | None = strawberry.field(
        description="Describes the playlist, what to expect and entices the user to listen."
    )
    _tracks: strawberry.Private[list[Track] | None] = None
    _test: strawberry.Private[str] = None

    @strawberry.field(description="The tracks in the playlist.")
    def tracks(self) -> list[Track]:
        return self._tracks
