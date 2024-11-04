#simplified version
if __name__ == '__main__':
    matches = []        # blank list to store valid matches
    line = ""
    try:
        f = open("matches.txt")
    except FileNotFoundError:
        print("file not found")
        exit(-1)                    # exit program passing an error code
    print("Reading file.")
    for line in f:      # loop for every line in  the file
        splitList = line.split(" ")  # split into 4 element list
        if len(splitList) != 4:
            print("error with match data :", line, end="")
            continue    # if an invalid line just go on and get the next line

        matches.append(splitList)

    # now we have a list called "matches" which has valid matches
    # <home team : string> <awayTeam : string> <homeScore: string> <awayScore : string>

    print()
    print("R E S U L T S")
    for match in matches:
        homeTeam = match[0]
        awayTeam = match[1]
        homeScore = match[2]
        awayScore = match[3]
        print(homeTeam, " ", homeScore, " : ", awayScore, " ", awayTeam)