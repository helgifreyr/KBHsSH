import sys

file=sys.argv[1]

def readLine(line):
    splitLine = line.split()
    w = float(splitLine[0])
    rh = float(splitLine[1])
    roots = [float(root) for root in splitLine[2:5]]
    extremas = [float(extrema) for extrema in splitLine[5:7]]
    M = float(splitLine[-1])
    return w,rh,roots,extremas,M

prevLine=open(file).readline()
oldw,oldrh,oldRoots,oldExtremas,oldM=readLine(prevLine)
oldrh=0
oldMaxRoot=0;oldMaxExtrema=0
oldRootCount=oldRoots.count(0)
oldExtremaCount=oldExtremas.count(0)
erTransitions=open('ER.dat','a')
print('w='+str(oldw))
for line in open(file):
    w,rh,roots,extremas,M=readLine(line)
    maxRoot = max(roots)
    maxExtrema = max(extremas)
    rootCount = roots.count(0)
    extremaCount = extremas.count(0)
    # need to write something clever to account for all scenarios
    # use extremaCount and maxRoot vs maxExtrema to figure it out
    if rh!=oldrh:
        derivative = abs((maxRoot-oldMaxRoot)/(rh-oldrh))
        if derivative>10 and oldDerivative<10 and rootCount == 2:
            print('ER to ET at rh='+str(oldrh)+' to rh='+str(rh))
            erTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# ER to ET at rh='+str(oldrh)+' to rh='+str(rh)+'\n')
    # if maxRoot > maxExtrema and maxRoot > 1.10*oldMaxRoot:
    #     print('ER to ET at rh='+str(oldrh)+' to rh='+str(rh))
    #     erTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# ER to ET at rh='+str(oldrh)+' to rh='+str(rh)+'\n')
    # if maxRoot < maxExtrema and oldMaxRoot > oldMaxExtrema:
    #     print('ET to ER at rh='+str(oldrh)+' to rh='+str(rh))
    #     erTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# ET to ER at rh='+str(oldrh)+' to rh='+str(rh)+'\n')
    prevLine=line
    oldDerivative=derivative
    oldw,oldrh,oldRoots,oldExtremas,oldM=readLine(prevLine)
    oldMaxRoot=maxRoot
    oldMaxExtrema=maxExtrema
    oldRootCount = oldRoots.count(0)
    oldExtremaCount = oldExtremas.count(0)
