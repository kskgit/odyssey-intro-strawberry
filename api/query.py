import strawberry

from .types.playlist import Playlist
from mock_spotify_rest_api_client.api.playlists import get_featured_playlists


@strawberry.type(description="Playlist hand-picked to be featured to all users.")
class Query:
    @strawberry.field
    async def featured_playlists(self, info: strawberry.Info) -> list[Playlist]:
        spotify_client = info.context["spotify_client"]
        data = await get_featured_playlists.asyncio(client=spotify_client)
        return [
            Playlist(
                id=strawberry.ID(playlist.id),
                name=playlist.name,
                description=playlist.description,
            )
            for playlist in data.playlists.items
        ]
