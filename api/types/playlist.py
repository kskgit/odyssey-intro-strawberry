import strawberry

from api.types.track import Track
from mock_spotify_rest_api_client.api.playlists import get_playlists_tracks
from mock_spotify_rest_api_client.models.spotify_object_paginated_spotify_object_playlist_track import (
    SpotifyObjectPaginatedSpotifyObjectPlaylistTrack,
)


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
    def tracks(self, info: strawberry.Info) -> list[Track] | None:
        if self._tracks is None:
            spotify_client = info.context["spotify_client"]

            data = get_playlists_tracks.asyncio(
                client=spotify_client, playlist_id=self.id
            )

            if data is None:
                return None
            if not isinstance(data, SpotifyObjectPaginatedSpotifyObjectPlaylistTrack):
                return None

            self._tracks = [
                Track(
                    id=strawberry.ID(item.track.id),
                    name=item.track.name,
                    duration_ms=item.track.duration_ms,
                    explicit=item.track.explicit,
                    uri=item.track.uri,
                )
                for item in data.items
            ]

        return self._tracks
