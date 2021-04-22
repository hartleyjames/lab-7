import argparse
from parseDot import getAdjMatrix
from dijkstra import dijkstras


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("graph filename", type=int)
    parser.add_argument("end", help="Coordinates of the desired end position: (3, 4)", type=tuple)

    # get args
    parser.parse_args()

    # parse the graph from the file

    # find shortest path from start node to end node

    # execute the path using drive code from previous project
