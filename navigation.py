import argparse
from turtleAPI import robot
from PIDController import AngularSpeedPIDController
from parseDot import getAdjMatrix
from dijkstra import dijkstras, getLocations


def distance(goal, curr):
    return np.sqrt((curr[0] - goal[0]) ** 2 + (curr[1] - goal[1]) ** 2)


# calculate angle between two points
def newyaw(goal, curr):
    return np.arctan2(goal[1] - curr[1], goal[0] - curr[0])


# fixes yaw error value
def yawdif(goal, curr):
    yaw = goal[2] - curr[2]
    if yaw > np.pi / 2 or yaw < -np.pi / 2:
        yaw = 1
    return yaw


if __name__ == "__main__":
    # create robot
    # rbt = robot()

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
    startpos = [0, 1]
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
        # startpos = list(rbt.getPositionTup())
        pass

    print startpos

    # parse the graph from the file
    filename = args.graph_filename
    matrix = getAdjMatrix(filename, startpos, endpos)
    loc = getLocations(filename, startpos, endpos)
    path = dijkstras(matrix, "start", "end", loc)

    print(path)

    # find shortest path from start node to end node
    # pull start and end from the matrix
    path = dijkstras(matrix, "start", "end")

    # execute the path using drive code from previous project
    apid = AngularSpeedPIDController(0.5, 0.1, 0.1, num_time_steps=5)
    for index in range(len(path) - 2):  # len-2 because the last item is None for some reason
        goal = path[index][1]  # goal is a list of x, y coordinates: [x, y]
        # get current odometer position from bot
        # cur_pos = rbt.getPositionTup()
        # find distance to goal
        dist_to_goal = distance(goal, cur_pos)
        while dist_to_goal > 0.1:
            # get robot position
            # cur_pos = rbt.getPositionTup()
            # find distance and angle to goal
            dist_to_goal = distance(goal, cur_pos)
            angle_to_goal = newyaw(goal, cur_pos)
            yaw_error = yawdif(goal, cur_pos)
            # get new angular speed to drive
            angular_speed = apid.updateInputValue(yaw_error)
            # call drive with new speed
            # rbt.drive(.5, angular_speed)
            # if distance is less than .1 meters, stop
            # update angle error
    # rbt.stop()
