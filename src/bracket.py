"""
Team and Bracket Holder and Rules
"""
from itertools import chain


class Team:
    """Team

    A team is a set of players
    >>> a = Team({0,1,2,3})
    """

    def __init__(self, players):
        self._players = frozenset(players)

    @property
    def players(self):
        return self._players

    def __hash__(self):
        return hash(self.players)

    def __eq__(self, other):
        # Equaility is based upon the players, not the order
        if isinstance(other, self.__class__):
            return self.players == other.players
        return False


class Matchup:
    """Matchup between two teams"""

    def __init__(self, a: Team, b: Team):
        # Check that the teams are not the same
        if a == b:
            raise ValueError("Teams must be unique")
        self._teams = frozenset({a, b})

    @property
    def teams(self):
        return self._teams

    def __eq__(self, other):
        # Equaility is based upon the teams, not the order
        if isinstance(other, self.__class__):
            return self.teams == other.teams
        return False

    def __hash__(self):
        return hash(self.teams)

    def get_players(self) -> set:
        """Gets the players of the teams in a matchup

        Returns:
            set: a set (no order) of the players
        """
        players = map(lambda x: x.players, self.teams)
        return set(chain.from_iterable(players))


class Round:
    """Matchups of a given round"""

    def __init__(self, matchups: set[Matchup]):
        # All Matchups must be unique
        self._matchups = frozenset(matchups)

    @property
    def matchups(self):
        return self._matchups

    def get_teams(self) -> set[Team]:
        teams = map(lambda x: x.teams, self.matchups)
        return set(chain.from_iterable(teams))

    def get_players(self) -> set:
        players = map(lambda x: x.players, self.get_teams())
        return set(chain.from_iterable(players))
