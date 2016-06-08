from scipy import genfromtxt,linspace
from pylab import *
import sys
from glob import glob

datZM = genfromtxt('ZM-kerr.dat')
rhZM = datZM[:,0]
MZM = datZM[:,1]
wZM = datZM[:,-1]
plot(wZM,MZM,'b--',ms=2.5)
V=0
extremalLine = lambda w: sqrt((1.0 - 4.0*V*V + sqrt(1.0+8.0*V*V))/w)/(2.0*sqrt(2.0*w))
ws = linspace(0.64,1,100)
plot(ws,extremalLine(ws),'k-',ms=2.5)

def readLine(line):
    splitLine = line.split()
    w = float(splitLine[0])
    rh = float(splitLine[1])
    roots = [float(er) for er in splitLine[2:5]]
    extremas = [float(er) for er in splitLine[5:7]]
    inflections = [float(er) for er in splitLine[7:11]]
    M = float(splitLine[-1])
    return w,rh,roots,extremas,inflections,M


datBS = genfromtxt('BS.txt')
wBS = datBS[:,0]
MBS = datBS[:,1]
plot(wBS,MBS,'r-',ms=2.5)

datExtremal = genfromtxt('eHBH.dat')
wExtremal = datExtremal[:,0]
MExtremal = datExtremal[:,1]
plot(wExtremal,MExtremal,'g-',ms=2.5)


for file in glob('ER-data/w=0*'):
    for line in open(file):
        w,rh,roots,extremas,inflections,M=readLine(line)
        inflectionCount = len(inflections)-inflections.count(0)
        cs = { 0:'r' , 1:'g' , 2:'b' , 3:'c' , 4:'m' }
        plot([w],[M],cs[inflectionCount]+'.',ms=2.5)
        

datRBS = genfromtxt('RBS.dat')
wRBS = datRBS[:,0]
MRBS = datRBS[:,1]
plot(wRBS,MRBS,'kD',ms=3.5)
datHBH = genfromtxt('KBHsSH.dat')
wHBH = datHBH[:,0]
MHBH = datHBH[:,1]
plot(wHBH,MHBH,'ks',ms=3.5)


xlim(0.64,1)
ylim(0,1.4)

xlabel(r'$w$')
ylabel(r'$M$')
savefig('w-M-inflections.pdf')
