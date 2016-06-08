import sys
from glob import glob

files = glob('ER-data/w=0.*')

def readLine(line):
    splitLine = line.split()
    w = float(splitLine[0])
    rh = float(splitLine[1])
    roots = [float(er) for er in splitLine[2:5]]
    extremas = [float(er) for er in splitLine[5:7]]
    inflections = [float(er) for er in splitLine[7:11]]
    M = float(splitLine[-1])
    return w,rh,roots,extremas,inflections,M


def checkFile(file):
    prevLine=open(file).readline()
    oldw,oldrh,oldRoots,oldExtremas,oldInflections,oldM=readLine(prevLine)
    oldRootCount = oldRoots.count(0)
    oldExtremaCount = oldExtremas.count(0)
    oldInflectionCount = oldInflections.count(0)
    print('w='+str(oldw))
    for line in open(file):
        w,rh,roots,extremas,inflections,M=readLine(line)
        rootCount = roots.count(0)
        extremaCount = extremas.count(0)
        inflectionCount = inflections.count(0)
        if rootCount == 2:
            if inflectionCount == 2 and oldInflectionCount == 0:
                print('2 inflection points to 4 at rh='+str(oldrh)+' to rh='+str(rh))
                erTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# 2inflection to 4inflection\n')
            if inflectionCount == 0 and oldInflectionCount == 2:
                print('4 inflection points to 2 at rh='+str(oldrh)+' to rh='+str(rh))
                erTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# 4inflection to 2inflection\n')
        prevLine=line
        oldw,oldrh,oldRoots,oldExtremas,oldInflections,oldM=readLine(prevLine)
        oldRootCount = oldRoots.count(0)
        oldExtremaCount = oldExtremas.count(0)
        oldInflectionCount = oldInflections.count(0)

erTransitions=open('ES.dat','w')
for file in files:
    checkFile(file)
