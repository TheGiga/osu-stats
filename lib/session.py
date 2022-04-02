from .errors import UserNotFound
from .osu import get, User


class Api:
    def __init__(
            self,
            api_key: str
    ):
        """
        :type api_key: String-like api key
        """
        self._api_key = api_key
        self._api_endpoint = "https://osu.ppy.sh/api"

    async def get_osu_player(self, name: str, mode: str = 'osu!') -> User:
        """
        :type name: Player's name
        :type mode: osu! game mode e.g osu!, osu!mania etc

        :rtype: osu.User
        """

        modes = {
            "osu!": 0,
            "Taiko": 1,
            "CtB": 2,
            "osu!mania": 3
        }

        params = {
            'k': self._api_key,
            'u': name,
            'm': modes[mode],
            'type': 'string'
        }
        data = await get(f'{self._api_endpoint}/get_user', params=params)

        try:
            obj = User(
                user_id=int(data[0].get('user_id')),
                data=data[0]
            )
        except IndexError:
            raise UserNotFound

        return obj
