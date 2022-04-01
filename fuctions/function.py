def countingWordsFromFile():
    fileName=input("Enter the file name")
    numberOfWords=0

    files=open(fileName, "r")
    for line in files:
        words=line.split()
        numberOfWords=numberOfWords+len(words)

    print("Number of words")
    print(numberOfWords)

countingWordsFromFile()