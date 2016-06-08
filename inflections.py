import sys
from glob import glob
import os

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


def checkFile(file,n,m):
    prevLine=open(file).readline()
    oldw,oldrh,oldRoots,oldExtremas,oldInflections,oldM=readLine(prevLine)
    oldRootCount = len(oldRoots)-oldRoots.count(0)
    oldExtremaCount = len(oldExtremas)-oldExtremas.count(0)
    oldInflectionCount = len(oldInflections)-oldInflections.count(0)
    print('w='+str(oldw))
    for line in open(file):
        w,rh,roots,extremas,inflections,M=readLine(line)
        rootCount = len(roots)-roots.count(0)
        extremaCount = len(extremas)-extremas.count(0)
        inflectionCount = len(inflections)-inflections.count(0)
        if rootCount == 1:
            if inflectionCount == n and oldInflectionCount == m:
                print(str(m)+' inflection points to '+str(n)+' at rh='+str(oldrh)+' to rh='+str(rh))
                erTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# '+str(m)+'inflection to '+str(n)+'inflection\n')
            if inflectionCount == m and oldInflectionCount == n:
                print(str(n)+' inflection points to '+str(m)+' at rh='+str(oldrh)+' to rh='+str(rh))
                erTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# '+str(n)+'inflection to '+str(m)+'inflection\n')
        prevLine=line
        oldw,oldrh,oldRoots,oldExtremas,oldInflections,oldM=readLine(prevLine)
        oldRootCount = len(oldRoots)-oldRoots.count(0)
        oldExtremaCount = len(oldExtremas)-oldExtremas.count(0)
        oldInflectionCount = len(oldInflections)-oldInflections.count(0)

n = [0,1,2,3,4]
m = [0,1,2,3,4]
for i in n:
    m.remove(i)
    for j in m:
        if i!=j:
            erTransitions=open('inflection-'+str(i)+'-'+str(j)+'.dat','w')
            for file in files:
                checkFile(file,i,j)
            erTransitions.close()
os.system('find inflection*dat -size  0 -print0 |xargs -0 rm')
