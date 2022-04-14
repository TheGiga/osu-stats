from lib import UserNotFound
from lib.osu import get_data
from .user_score import UserBestScore


class User:
    """
    Represents osu player as class.
    """

    def __init__(
            self,
            data: dict,
            game_mode: str,
            api_key: str
    ):
        """
        :param data: data from api
        :param game_mode: osu! game mode
        :param api_key: osu!api key
        """
        self._game_mode = game_mode
        self._data = data
        self._api_key = api_key

    @property
    def game_mode(self) -> str:
        return self._game_mode

    @property
    def user_id(self) -> int:
        return self._data.get('user_id')

    @property
    def username(self) -> str:
        return self._data.get('username')

    @property
    def accuracy(self) -> float:
        try:
            x = round(float(self._data.get('accuracy')))
        except TypeError:
            x = 0

        return x

    @property
    def count_300(self) -> int:
        try:
            x = int(self._data.get('count_300'))
        except TypeError:
            x = 0

        return x

    @property
    def play_count(self) -> int:
        try:
            x = int(self._data.get('playcount'))
        except TypeError:
            x = 0

        return x

    @property
    def rank(self) -> int:
        try:
            x = int(self._data.get('pp_rank'))
        except TypeError:
            x = 0

        return x

    @property
    def country_rank(self) -> int:
        try:
            x = int(self._data.get('pp_country_rank'))
        except TypeError:
            x = 0

        return x

    @property
    def level(self) -> int:
        try:
            x = int(round(float(self._data.get('level'))))
        except TypeError:
            x = 0

        return x

    @property
    def pp(self) -> int:
        try:
            x = int(round(float(self._data.get('pp_raw'))))
        except TypeError:
            x = 0

        return x

    @property
    def total_ss(self) -> int:
        try:
            x = int(self._data.get('count_rank_ss')) + int(self._data.get('count_rank_ssh'))
        except TypeError:
            x = 0

        return x

    @property
    def total_s(self) -> int:
        try:
            x = int(self._data.get('count_rank_s')) + int(self._data.get('count_rank_sh'))
        except TypeError:
            x = 0

        return x

    @property
    def country(self) -> str:
        x = self._data.get('country')
        if x is None:
            return 'aq'
        return x

    @property
    def profile_image_url(self) -> str:
        return f"http://s.ppy.sh/a/{self.user_id}"

    @property
    async def best_score(self) -> UserBestScore:
        obj = await UserBestScore.form_object(user_id=self.user_id, mode=self.game_mode, api_key=self._api_key)

        return obj

    @classmethod
    async def form_object(cls, username: str, mode: str, api_key: str):
        """
        :param username: User name to get data from
        :param mode: osu! game mode (osu!, Taiko etc.)
        :param api_key: osu!api key

        :return: osu.UserScore
        """

        modes = {
            "osu!": 0,
            "Taiko": 1,
            "CtB": 2,
            "osu!mania": 3
        }

        params = {
            'k': api_key,
            'u': username,
            'm': modes.get(mode),
            'type': 'string'
        }
        data = await get_data(f'https://osu.ppy.sh/api/get_user', params=params)

        try:
            obj = cls(
                data=data[0],
                game_mode=mode,
                api_key=api_key
            )
        except IndexError:
            raise UserNotFound

        return obj
