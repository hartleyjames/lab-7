from math import sqrt
import heapq


def dist(x1, y1, x2, y2):
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

def contains(pq, s):
	val = False
	for x in pq:
		if x[2] == s:
			val = True
	return val

def dijkstras(matrix, startPoint, endPoint):

	i = 0
	s = [0, i, startPoint]
	pq = []
	while s[2] != endPoint:
		print(s[2])
		for key, value in matrix[s[2]].items():
			if value > 0:
				if not contains(pq, key):
					gs1 = s[0] + value
					pq.append([gs1, i, key])
					i += 1
				else:	
					gs1 = 0
					s1 = None
					for x in pq:
						if x[2] == s:
							gs1 = x[0]
							s1 = x
					if gs1 > s[0] + value:
						gs1 = s[0] + value
						s1[0] = gs1
		heapq.heapify(pq)
		s = heapq.heappop(pq)
	print(s[2])

def getAdjMatrix(filename, ss, ee):
    f = open(filename, "r")
    contents = f.read()

    contents = contents.split("\n")
    contents.pop(0)
    while contents[len(contents) - 1] == "" or contents[len(contents) - 1] == "}":
        contents.pop()
    # print(contents)

    i = 0
    for x in contents:
        if "=" in x:
            i += 1
        else:
            break
    # print(contents[i])

    j = 0
    locations = {}
    for s in contents:
        if j == i:
            break

        name = s.split(" ")
        while name[0] == "":
            name.pop(0)
        name = name[0]

        start = s.index("(")
        end = s.index(")")
        val = s[start + 1:end - 1]

        # print val
        val = val.split(", ")

        coor = [float(val[0]), float(val[1])]

        locations[name] = coor

        j += 1

    '''print locations'''

    j = 0
    combos = []
    for s in contents:
        if j >= i:
            points = s.strip()
            points = points.replace(";", "")
            points = points.split(" -- ")
            combos.append(points)
        j += 1

    startPoint = "start"
    endPoint = "end"
    closestStart = 100000000000000000
    closestEnd = 100000000000000000

    for key in locations:
        startDist = dist(ss[0], ss[1], locations[key][0], locations[key][1])
        endDist = dist(ee[0], ee[1], locations[key][0], locations[key][1])

        if startDist < closestStart:
            closestStart = startDist
            startPoint = key

        if endDist < closestEnd:
            closestEnd = endDist
            endPoint = key

    combos.append(["start", startPoint])
    combos.append(["end", endPoint])

    locations["start"] = ss
    locations["end"] = ee

    '''print("combos:")
    print(combos)'''

    adjMax = {}
    for key in locations:
        adjMax[key] = {}
        for key2 in locations:
            connect = False
            for x in combos:
                if (x[0] == key and x[1] == key2) or (x[1] == key and x[0] == key2):
                    connect = True
            if key == key2:
                adjMax[key][key2] = 0
            elif connect:
                adjMax[key][key2] = dist(locations[key][0], locations[key][1], locations[key2][0], locations[key2][1])
            else:
                adjMax[key][key2] = -1

    '''print("matrix:\n")
    print(adjMax)'''

    '''print ss
    print ee
    print locations'''

    return adjMax


start = [0, 1]
end = [0, 0]
mat = getAdjMatrix("graphA.dot", start, end)
dijkstras(mat, start, end)
