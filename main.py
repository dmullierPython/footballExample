# Football Example
# uses concepts needed for tasks 2 and 3
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
        try:            # see if we can convert the third and fourth items into numbers
            splitList[2] = int(splitList[2])
            splitList[3] = int(splitList[3])
        except ValueError:  # if we can convert into numbers then it is an invalid ficture
            print("invalid score ", line, end="")
            continue    # if an invalid line just go on and get the next line
        matches.append(splitList)

    # now we have a list called "matches" which has valid matches
    # <home team : string> <awayTeam : string> <homeScore: int> <awayScore : int>
    highestScore = 0
    highestScoreTeam = ""
    print()
    print("R E S U L T S")
    for match in matches:
        homeTeam = match[0]
        awayTeam = match[1]
        homeScore = match[2]
        awayScore = match[3]
        print(homeTeam, " ", homeScore, " : ", awayScore, " ", awayTeam)
        if homeScore > highestScore:
            highestScoreTeam = homeTeam
            highestScore = homeScore
        if awayScore > highestScore:
            highestScoreTeam = awayTeam
            highestScore = awayScore
    print("Highest score was ", highestScore, " by ", highestScoreTeam)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
