import pytest
from dijkstra import Dijkstra

@pytest.mark.parametrize("edges, n, src, expected", [
    (
        [
            [0, 1, 10],
            [0, 2, 3],
            [1, 3, 2],
            [2, 1, 4],
            [2, 3, 8],
            [2, 4, 2],
            [3, 4, 5],
        ],
        5,
        0,
        {0: 0, 1: 7, 2: 3, 3: 9, 4: 5},
    ),
    ([[0, 1, 5]], 2, 0, {0: 0, 1: 5}),
    ([[0, 1, 3], [1, 2, 1], [2, 0, 4]], 3, 0, {0: 0, 1: 3, 2: 4}),
    (
        [[0, 1, 5], [0, 2, 7], [1, 2, 2], [1, 3, 6], [2, 3, 4]],
        4,
        1,
        {0: -1, 1: 0, 2: 2, 3: 6},
    ),
])

def test_shortest_path(edges, n, src, expected):
    assert Dijkstra.shortest_path(edges, n, src) == expected

