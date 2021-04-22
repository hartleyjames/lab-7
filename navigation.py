import argparse
from parseDot import getAdjMatrix
from dijkstra import dijkstras

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("graph_filename",
                        help="Filename for graph .dot file. must be in same directory as code.",
                        type=int)
    parser.add_argument("end",
                        help="Coordinates of the desired end position: [3, 4]",
                        type=tuple)
    parser.add_argument("-s", "--start",
                        help="Coordinates of the desired start position: [3, 4]",
                        type=tuple)

    # get args
    args = parser.parse_args()

    # get either current location of bot or start coordinate from input
    startpos = None
    if args.start:
        # pull from here
        pass
    else:
        # find from bot localizer
        pass

    # parse the graph from the file
    filename = args.graph_filename
    matrix = getAdjMatrix(filename, startpos, args.end)

    # find shortest path from start node to end node

    # execute the path using drive code from previous project
