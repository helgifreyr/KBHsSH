import sys
from glob import glob

files = glob('ER-data/w=0.*')

def readLine(line):
    splitLine = line.split()
    w = float(splitLine[0])
    rh = float(splitLine[1])
    ER = [float(er) for er in splitLine[2:5]]
    M = float(splitLine[-1])
    return w,rh,ER,M


def checkFile(file):
    prevLine=open(file).readline()
    oldw,oldrh,oldER,oldM=readLine(prevLine)
    print('w='+str(oldw))
    for line in open(file):
        w,rh,ER,M=readLine(line)
        ERzeros = ER.count(0)
        oldERzeros = oldER.count(0)
        if oldERzeros > ERzeros:
            print('ER to ET at rh='+str(oldrh)+' to rh='+str(rh))
            erTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# ER to ET\n')
        elif oldERzeros < ERzeros:
            print('ET to ER at rh='+str(oldrh)+' to rh='+str(rh))
            erTransitions.write(str(w)+'\t'+str(oldM)+'\t'+str(M)+'\t# ET to ER\n')
        prevLine=line
        oldw,oldrh,oldER,oldM=readLine(prevLine)

erTransitions=open('ET.dat','w')
for file in files:
    checkFile(file)
