from dijkstra_github import shortest_path
from parseDot import getAdjMatrix


if __name__ == "__main__":
    start = [0, 1]
    end = [0, 0]
    matrix = getAdjMatrix("graphA.dot", start, end)

    print(shortest_path(matrix, start='start', end='end'))
