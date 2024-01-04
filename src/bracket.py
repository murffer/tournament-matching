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
        self._teams = [a, b]

    @property
    def teams(self):
        return self._teams

    def __eq__(self, other):
        # Equaility is based upon the teams, not the order
        if isinstance(other, self.__class__):
            return self.teams == other.teams
        return False

    def get_players(self) -> list:
        """Gets the players of the teams in a matchup

        Returns:
            list: a list (no order) of the players
        """
        players = map(lambda x: x.players, self.teams)
        return list(chain.from_iterable(players))

    def unique_players(self) -> bool:
        """Determines if the players are unique in the matchup

        Returns:
            bool: true if the players are unique
        """
        players = self.get_players()
        return len(players) == len(set(players))


class Round:
    """Matchups of a given round"""

    def __init__(self, matchups: list[Matchup]):
        self._matchups = matchups

    @property
    def matchups(self):
        return self._matchups

    def get_teams(self) -> list[Team]:
        teams = map(lambda x: x.teams, self.matchups)
        return list(chain.from_iterable(teams))


def get_teams(round_i):
    """ """
    # All of the teams in a round
    teams_i = [team_i for team in round_i for team_i in team]
    return teams_i


def get_players(matchup_i):
    # Player can't play themselves in a matchup
    players_i = [player_i for team in matchup_i for player_i in team]
    return players_i


def unique_teams(round_i) -> bool:
    # Cannot have the same team playing twice in a round
    teams_i = get_teams(round_i)
    return len(teams_i) == len(set(teams_i))


def unique_matchup(matchup_i) -> bool:
    # Player can't play themselves in a matchup
    players_i = [player_i for team in matchup_i for player_i in team]
    return len(players_i) == len(set(players_i))
