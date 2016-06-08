from glob import glob

files = glob('LR-data/w=0.*')

def readLine(line):
    splitLine = line.split()
    w = float(splitLine[0])
    rh = float(splitLine[1])
    LR = [float(lr) for lr in splitLine[2:5]]
    M = float(splitLine[-1])
    return w,rh,LR,M

def checkFile(file):
    prevLine=open(file).readline()
    oldw,oldrh,oldLR,oldM=readLine(prevLine)
    print('w='+str(oldw))
    for line in open(file):
        w,rh,LR,M=readLine(line)
        LRzeros = LR.count(0)
        oldLRzeros = oldLR.count(0)
        if oldLRzeros > LRzeros:
            print('1LR to 3LR at rh='+str(oldrh)+' to rh='+str(rh))
            lrTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# 1LR to 3LR\n')
        elif oldLRzeros < LRzeros:
            print('3LR to 1LR at rh='+str(oldrh)+' to rh='+str(rh))
            lrTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# 3LR to 1LR\n')
        prevLine=line
        oldw,oldrh,oldLR,oldM=readLine(prevLine)

lrTransitions=open('3LR.dat','w')
for file in files:
    checkFile(file)
