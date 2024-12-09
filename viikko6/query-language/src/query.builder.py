from matchers import And, Or, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self):
        self.matchers = []

    def plays_in(self, team):
        self.matchers.append(PlaysIn(team))
        return self

    def has_at_least(self, value, attr):
        self.matchers.append(HasAtLeast(value, attr))
        return self

    def has_fewer_than(self, value, attr):
        self.matchers.append(HasFewerThan(value, attr))
        return self

    def build(self):
        return And(*self.matchers)