

def prepData():
    with open("cluster_data.txt") as textFile:
        lines = [line.split() for line in textFile]

    for i in range(len(lines)):
        lines[i].pop(0)

prepData()