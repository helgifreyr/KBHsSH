import sys

file=sys.argv[1]

def readLine(line):
    splitLine = line.split()
    w = float(splitLine[0])
    rh = float(splitLine[1])
    ER = [float(er) for er in splitLine[2:5]]
    LR = [float(lr) for lr in splitLine[8:11]]
    M = float(splitLine[-1])
    return w,rh,ER,LR,M

prevLine=open(file).readline()
oldw,oldrh,oldER,oldLR,oldM=readLine(prevLine)
erTransitions=open('ET.dat','a')
lrTransitions=open('3LR.dat','a')
print('w='+str(oldw))
for line in open(file):
    w,rh,ER,LR,M=readLine(line)
    ERzeros = ER.count(0)
    oldERzeros = oldER.count(0)
    if oldERzeros > ERzeros:
        print('ER to ET at rh='+str(oldrh)+' to rh='+str(rh))
        erTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# ER to ET\n')
    elif oldERzeros < ERzeros:
        print('ET to ER at rh='+str(oldrh)+' to rh='+str(rh))
        erTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# ET to ER\n')
    LRzeros = LR.count(0)
    oldLRzeros = oldLR.count(0)
    if oldLRzeros > LRzeros:
        print('1LR to 3LR at rh='+str(oldrh)+' to rh='+str(rh))
        lrTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# 1LR to 3LR\n')
    elif oldLRzeros < LRzeros:
        print('3LR to 1LR at rh='+str(oldrh)+' to rh='+str(rh))
        lrTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# 3LR to 1LR\n')
    prevLine=line
    oldw,oldrh,oldER,oldLR,oldM=readLine(prevLine)
