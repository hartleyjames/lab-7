import argparse
from turtleAPI import robot
from parseDot import getAdjMatrix
from dijkstra import dijkstras, getLocations

if __name__ == "__main__":

	
    #rbt = robot()

    parser = argparse.ArgumentParser()
    parser.add_argument("graph_filename",
                        help="Filename for graph .dot file. must be in same directory as code.",
                        type=str)
    parser.add_argument("end",
                        help="Coordinates of the desired end position: [3, 4]",
                        type=list)
    parser.add_argument("-s", "--start",
                        help="Coordinates of the desired start position: [3, 4]",
                        type=list)

    # get args
    args = parser.parse_args()

    # get either current location of bot or start coordinate from input
    startpos = [0,1]
    endpos = args.end

    endpos[0] = float(endpos[0])
    endpos[1] = float(endpos[2])
    endpos.pop()
    print endpos

    if args.start:
        # pull from here
        startpos = args.start
        startpos[0] = float(startpos[0])
        startpos[1] = float(startpos[2])
	startpos.pop()
    else:
        # find from bot localizer
        #startpos = list(rbt.getPositionTup())
	pass

    print startpos

    # parse the graph from the file
    filename = args.graph_filename
    matrix = getAdjMatrix(filename, startpos, endpos)
    loc = getLocations(filename, startpos, endpos)
    path = dijkstras(matrix, "start", "end", loc)

    print(path) 

    # find shortest path from start node to end node

    # execute the path using drive code from previous project
