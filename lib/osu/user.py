class User:
    """
    Represents osu player as class.
    """

    def __init__(
            self,
            user_id: int,
            data: dict
    ):
        """

        :type user_id: osu user id
        :type data: JSON like data from osu!api v1 /get_user
        """
        self._user_id = user_id
        self._data = data

    @property
    def user_id(self) -> int:
        return self._user_id

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
        return f"http://s.ppy.sh/a/{self._user_id}"
