import strawberry

from api.types.playlist import Playlist


@strawberry.type
class AddItemsToPlaylistPayload:
    code: int = strawberry.field(
        description="Similar to HTTP status code, represents the status of the mutation."
    )
    success: bool = strawberry.field(
        description="Indicates whether the mutaion was successful."
    )
    message: str = strawberry.field(description="Human-readable message for the UI.")
    playlist: Playlist | None = strawberry.field(
        description="The playlist that contains the newy added items."
    )
