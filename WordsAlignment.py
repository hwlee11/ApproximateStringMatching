from Levenshtein import distance as lev

import copy
import argparse


korean = False
noPredictionToken = "null"

def dfs(matrix, startX,startY):
    stack = list()
    scoreStack = list()
    scoreList = list()
    pathStack = list()
    stack.append((startX,startY))
    pathList = list()
    path = list()
    scoreHistory = 0
    while True:
        if len(stack) == 0:
            break

        #visit
        nowX,nowY = stack.pop()

        #visit check
        if nowX == 0 and nowY == 0:
            pathList.append(path)
            scoreList.append(scoreHistory)
            if len(pathStack) > 0:
                path = pathStack.pop()
                scoreHistory = scoreStack.pop()
            continue
        else:
            path.insert(0,(nowX,nowY))
            scoreHistory += matrix[nowX][nowY]

        #search
        #path.append((nowX,nowY))
        tempScoreList = list()   # del, in, sub
        if nowY > 0:
            tempScoreList.append(matrix[nowX][nowY-1]) # del
        if nowX > 0:
            tempScoreList.append(matrix[nowX-1][nowY]) # in
        if nowX > 0 and nowY > 0:
            tempScoreList.append(matrix[nowX-1][nowY-1]) # sub

        minScore = min(tempScoreList)

        temp = list()
        if tempScoreList[0] == minScore:
            temp.append((nowX,nowY-1))
        if tempScoreList[1] == minScore:
            temp.append((nowX-1,nowY))
        if tempScoreList[2] == minScore:
            temp.append((nowX-1,nowY-1))
        
        if len(temp)>1:         # if branch, stacking path
            for i in temp:
                stack.append(i)
                pathStack.append(copy.deepcopy(path))
                scoreStack.append(copy.deepcopy(scoreHistory))
        else:
            stack.append(temp.pop())

    return pathList,scoreList

def wordLevenshteinDistance(wordA,wordB):
    
    if wordA == wordB:
        value = -(len(wordA))
        return value

    if korean:
        from jamo import h2j,j2hcj
        from g2pk import G2p
        wordA = g2p(wordA)
        wordB = g2p(wordB)
        wordA = j2hcj(h2j(wordA))
        wordB = j2hcj(h2j(wordB))
        levDistance = lev()
    else:
        levDistance = lev(wordA,wordB)

    return levDistance

def optimalWordStringAlignment(strB,strA):

    scoreMatrix = list()
    lengthA = len(strA) 
    lengthB = len(strB) 


    # make score matirx
    for i in range(lengthA+1):
        temp = list()
        for j in range(lengthB+1):
            temp.append(0)
        scoreMatrix.append(temp)

    # init matrix
    for i in range(lengthA+1):
        scoreMatrix[i][0] = wordLevenshteinDistance(strA[0],"") + i
    for i in range(lengthB+1):
        scoreMatrix[0][i] = wordLevenshteinDistance("",strB[0]) + i

    # scoring
    # base on Smith-Waterman algorithm
    gapPenalty = 0
    for i in range(1,lengthA+1):
        for j in range(1,lengthB+1):
            scoreMatrix[i][j] = min([
                scoreMatrix[i-1][j-1] + wordLevenshteinDistance(strA[i-1],strB[j-1]),               # substitution
                scoreMatrix[i-1][j] + wordLevenshteinDistance(strA[i-1],"") +  (i-1)*gapPenalty,    # deletion
                scoreMatrix[i][j-1] + wordLevenshteinDistance("",strB[j-1]) + (j-1)*gapPenalty      # insertion
            ])
    
    # Tracback
    matchingPaths,matchingScore = dfs(scoreMatrix,lengthA,lengthB)
    minPath = matchingPaths[matchingScore.index(min(matchingScore))]

    # matching
    newA=list()
    newB=list()
    for i in range(len(minPath)):
        newA.append('-')
        newB.append('-')
    i=0
    j=0
    for k in range(len(minPath)):
        if minPath[k][0] == minPath[k-1][0]:
            newA[k] = "-"#.append('-')
        else:
            newA[k] = strA[i]
            i+=1
        if minPath[k][1] == minPath[k-1][1]:
            newB[k] = strB[j]
            j+=1
        else:
            newB[k] = strB[j]
            j=j+1
    wordPairs = list
    for i,j in zip(newA,newB):
        wordParis.append((i,j))

    return wordPairs



def main(args):

    strA = args.strA.split()
    strB = args.strB.split()
    paris = optimalWordStringAlignment(strA,strB)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="word lavel string alignment\n --strA '' --strB ''")
    parser.add_argument("--strA",default="s a t u r d a y c b d",type=str)
    parser.add_argument("--strB",default="s u n d a y a b",type=str)
    parser.add_argument("--korean",default=False,type=bool)

    args = parser.parse_args()
    main(args)
