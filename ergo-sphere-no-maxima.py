import sys
from glob import glob

files = glob('ER-data/w=0.*')

def readLine(line):
    splitLine = line.split()
    w = float(splitLine[0])
    rh = float(splitLine[1])
    roots = [float(er) for er in splitLine[2:5]]
    extremas = [float(er) for er in splitLine[5:7]]
    inflections = [float(er) for er in splitLine[7:9]]
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
        if extremaCount == len(extremas) and rootCount == 2 and oldExtremaCount == 0:
            print('Two maxima to no maxima at rh='+str(oldrh)+' to rh='+str(rh))
            erTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# 2max to 0max\n')
        if extremaCount == 0 and rootCount == 2 and oldExtremaCount == len(extremas):
            print('No maxima to two maxima at rh='+str(oldrh)+' to rh='+str(rh))
            erTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# 0max to 2max\n')
        prevLine=line
        oldw,oldrh,oldRoots,oldExtremas,oldInflections,oldM=readLine(prevLine)
        oldRootCount = oldRoots.count(0)
        oldExtremaCount = oldExtremas.count(0)
        oldInflectionCount = oldInflections.count(0)

erTransitions=open('gtt-no-maxima.dat','w')
for file in files:
    checkFile(file)
