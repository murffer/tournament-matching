import unittest
from src.bracket import Team, Matchup, Round


class TestTeam(unittest.TestCase):
    def test_team_construct(self):
        t = Team({0, 1, 2, 3})
        self.assertSetEqual(t.players, {0, 1, 2, 3})

    def test_team_equality(self):
        self.assertTrue(Team({1, 2}) == Team({2, 1}))
        self.assertFalse(Team({1, 2}) == Team({2, 3}))

    def test_team_hash(self):
        self.assertTrue(hash(Team({1, 2})) == hash(Team({2, 1})))
        self.assertFalse(hash(Team({1, 2})) == hash(Team({2, 3})))


class TestMatchup(unittest.TestCase):
    def test_matchup_construct(self):
        a = {0, 1, 2}
        b = {3, 4, 5}
        m = Matchup(Team(a), Team(b))
        self.assertSetEqual(m.get_players(), a | b)

    def test_unique_teams(self):
        t = Team({0, 1})
        with self.assertRaises(ValueError):
            Matchup(t, t)

    def test_matchup_equality(self):
        a = {0, 1}
        b = {2, 3}
        c = {4, 5}
        d = {6, 7}
        m1 = Matchup(Team(a), Team(b))
        m2 = Matchup(Team(c), Team(d))
        self.assertEqual(m1, m1)
        self.assertNotEqual(m1, m2)

    def test_matchup_hash(self):
        a = {0, 1}
        b = {2, 3}
        c = {4, 5}
        d = {6, 7}
        m1 = Matchup(Team(a), Team(b))
        m2 = Matchup(Team(c), Team(d))
        self.assertEqual(hash(m1), hash(m1))
        self.assertNotEqual(hash(m1), hash(m2))


class TestRound(unittest.TestCase):
    a = {0, 1}
    b = {2, 3}
    c = {4, 5}
    d = {6, 7}
    m1 = Matchup(Team(a), Team(b))
    m2 = Matchup(Team(c), Team(d))

    def test_round_construct(self):
        r = Round([self.m1, self.m2])
        self.assertEqual(r.matchups, frozenset([self.m1, self.m2]))

    def test_get_teams(self):
        r = Round([self.m1, self.m2])
        self.assertSetEqual(
            r.get_teams(), {Team(self.a), Team(self.b), Team(self.c), Team(self.d)}
        )

    def test_get_players(self):
        r = Round([self.m1, self.m2])
        players = self.a | self.b | self.c | self.d
        self.assertSetEqual(r.get_players(), players)


if __name__ == "__main__":
    unittest.main()
