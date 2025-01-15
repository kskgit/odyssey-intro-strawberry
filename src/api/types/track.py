import strawberry


@strawberry.type(description="A single audio file, usually a song.")
class Track:
    id: strawberry.ID = strawberry.field(description="The ID for the track.")
    name: str = strawberry.field(description="The name of the track.")
    duration_ms: int = strawberry.field(
        description="The track length in milliseconds.")
    explicit: bool = strawberry.field(
        description="Whether or not the track has explict lyrics (true = yes it does; false = no it does not or unknown)"
    )
    uri: str = strawberry.field(
        description="The URI for the track, useally a Spotify link."
    )

    @strawberry.field(description="The type name of this object")
    def __typename(self) -> str:
        return "Track"
