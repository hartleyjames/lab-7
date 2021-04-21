# Lab 7

### [Link to Course Page](https://www.usna.edu/Users/cs/taylor/courses/si475/hw/navProj.html)

##### Navigation Project

The basic project description: after initializing your particle cloud in MCL, and reading in some graph information, your program should accept an (x,y) coordinate in the map, and drive there, without running into any walls.

##### Building the graph

To accomplish this, we need a graph of coordinates at different points along our map. We saw some ways in class to build such graphs automatically, but we’re going to do it manually to save some effort in our specific space. As a class, you will work together to construct a DOT file which describes our graph. DOT files are just text files that describe graphs - they’re commonly used by programs to draw or analyze graphs. Here’s an example of the text in a DOT file that would work for us:

```
graph G {
  A [label = "(5.2,3.4)"];
  infrontofHP114 [label = "(-3.5,2.1)"];
  C [label = "(0,5.2)"];

  A -- C;
  infrontofHP114 -- C;
}
```

This dot file begins by listing its three nodes, A, infrontofHP114, and C. You’ll note I’ve listed their locations as labels, and that their names can be whatever you like and as descriptive as you like. After a blank space, I’ve listed the edges of the graph. A and C have an edge between them, and infrontofHP114 and C has an edge between them. Of course the length of those edges can be easily calculated using their locations in the label.

I will want to see a picture of your graph, written on top of the map, so I can understand what your robot is navigating.

##### Parsing the graph

Your program should accept a path to your DOT file as a command line argument. You’ll read in a DOT file and turn it into an adjacency matrix, where each entry is the distance between the two nodes. Add two more nodes - one which is where your robot is now, and one which is where your robot is supposed to stop. Each should be adjacent to only the closest node in the existing graph.

##### Finding the shortest path

Perform Dijkstra’s algorithm from where you are to where you want to end up. Print out the intended path.

##### Execute the path

Of course, you’ve already written code with PID controllers that can drive to an (x,y) location when there are no walls in the way (each pair of connected nodes in your graph, for example, have no walls in the way). Driving from node to node should allow you to execute your path.

##### I/O

Your program should accept two or three command-line arguments (consider using argparse). The first should be the path to a DOT file. The second should be the x,y coordinates of the goal. If there is a third, this should be considered a theoretical starting location. If there is not a third, the starting location should be the robot’s position.

If there was a third argument, your program should just print out the sequence of (x, y) coordinates it intends to visit. If there was not a third argument, your program should print out that sequence, then execute the path.

I will test by giving you a new DOT file and start and ending points, as well as by separately asking you to drive somewhere in Hopper.
