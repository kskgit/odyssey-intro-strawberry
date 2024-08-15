import strawberry
from api.types.AddItemsToPlaylistPayload import AddItemsToPlaylistPayload
from api.types.playlist import Playlist


@strawberry.type
class Mutation:
    @strawberry.mutation(description="Add one or more items to a user's playlist.")
    def add_items_to_playlist(self) -> AddItemsToPlaylistPayload:
        return AddItemsToPlaylistPayload(
            code=200,
            success=True,
            message="Successfully added items to playlist.",
            playlist=Playlist(
                id="6Fl8d6KF0O4V5kFdbzalfW",
                name="Sweet Beats & Eats",
                description=None,
            ),
        )
