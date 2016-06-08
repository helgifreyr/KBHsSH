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


def plotTransitions(type,line,c,style,size):
    dat= genfromtxt(type)
    w = dat[:,0]
    M = (dat[:,1]+dat[:,2])/2.0
    plot(w,M,linestyle=line,color=c,marker=style,ms=size)

datBS = genfromtxt('BS.txt')
wBS = datBS[:,0]
MBS = datBS[:,1]
plot(wBS,MBS,'r-',ms=2.5)

datExtremal = genfromtxt('eHBH.dat')
wExtremal = datExtremal[:,0]
MExtremal = datExtremal[:,1]
plot(wExtremal,MExtremal,'g-',ms=2.5)

plotTransitions('ET.dat','-','b','None',2.5)
plotTransitions('ES.dat','None','y','.',2.5)
plotTransitions('3LR.dat','-','m','None',2.5)
plotTransitions('gtt-no-maxima.dat','-','c','None',2.5)

# # i=0
# styles=[r'$0\rightarrow 1$',r'$0\rightarrow 2$',r'$1\rightarrow2$',r'$2\rightarrow 4$']
# # colors=['r','g','b','k']
# for file in glob('inflection*dat'):
#     plotTransitions(file,'None','b','.',2.5)
#     # i+=1

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
savefig('w-M.pdf')
