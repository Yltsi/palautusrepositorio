from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or, QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)
    query = QueryBuilder()


    matcher = And(
    HasFewerThan(2, "goals"),
    PlaysIn("NYR")
)
    for player in stats.matches(matcher):
        print(player)

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    print("-----")
    print("Or eka")
    matcher = Or(
    HasAtLeast(45, "goals"),
    HasAtLeast(70, "assists")
)
    for player in stats.matches(matcher):
        print(player)

    print("-----")
    print("Or toka")
    matcher = And(
    HasAtLeast(70, "points"),
    Or(
        PlaysIn("NYR"),
        PlaysIn("FLA"),
        PlaysIn("BOS")
    )
)
    for player in stats.matches(matcher):
        print(player)

    print("-----")
    print("Query builder")
    matcher = (
        query
        .plays_in("NYR")
        .has_at_least(10, "goals")
        .has_fewer_than(20, "goals")
        .build()
    )

    for player in stats.matches(matcher):
        print(player)
    
    print("-----")
    print("Query builder Osa 2")

    matcher = (
        query
        .one_of(
            query.plays_in("PHI")
                .has_at_least(10, "assists")
                .has_fewer_than(10, "goals")
                .build(),
            query.plays_in("EDM")
                .has_at_least(50, "points")
                .build()
        )
        .build()
    )

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
