import jamo
#import Levenshtein
from Levenshtein import distance as lev

import argparse


korean = False
noPredictionToken = "null"

def wordLevenshteinDistance(wordA,wordB):
    
    if wordA == wordB:
        return -1

    if korean:
        pass
    else:
        levDistance = lev(wordA,wordB)

    return levDistance

def optimalWordStringAlignment(strA,strB):

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
    gapPenalty = 3
    for i in range(1,lengthA+1):
        for j in range(1,lengthB+1):
            scoreMatrix[i][j] = min([
                scoreMatrix[i-1][j-1] + wordLevenshteinDistance(strA[i-1],strB[j-1]),
                scoreMatrix[i-1][j] + wordLevenshteinDistance(strA[i-1],"") +  (i-1)*gapPenalty,
                scoreMatrix[i][j-1] + wordLevenshteinDistance("",strB[j-1]) + (j-1)*gapPenalty
            ])

    for i in range(lengthA+1):
        print(i,j,scoreMatrix[i])
    # Tracback
    mathcingPath = list()

    # matching
    i=1
    j=1
    newA=list()
    newB=list()
    #for k in range(1,):
    #    if matchingPath[k]

    #return (newA,newB)



def main(args):

    strA = args.strA.split()
    strB = args.strB.split()
    paris = optimalWordStringAlignment(strA,strB)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="word lavel string alignment")
    #parser.add_argument("--strA",default="hello world bro a",type=str)
    #parser.add_argument("--strB",default="hello my friend a",type=str)
    parser.add_argument("--strA",default="a c b d",type=str)
    parser.add_argument("--strB",default="a c d",type=str)

    args = parser.parse_args()
    main(args)
