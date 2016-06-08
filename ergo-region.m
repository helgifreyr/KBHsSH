(* ::Package:: *)

Remove["Global`*"];
Unprotect[In,Out];
Clear[In,Out];
Off[General::spell1]


data=ReadList["functf.dat",Number,RecordLists->True];
nOfFs=5;
radialCoord=ReadList["gridx.dat",Number];
angularCoord=ReadList["gridy.dat",Number];
nx=Length[radialCoord];
ny=Length[angularCoord];


dat=ArrayReshape[data,{nx ny,nOfFs}];


(* 1  2   3   4  5  6   7*)
(* nr,w,alpha,c1,c2,c3,rh*)
conf=ReadList["res.txt",{Number,Number ,Number ,Number ,Number,Number,Number }];

 
nr=conf[[1]][[1]];
rh= conf[[1]][[7]];
alfa= conf[[1]][[3]];
c1= conf[[1]][[4]];
c2= conf[[1]][[5]];
c3= conf[[1]][[6]]; 
w= conf[[1]][[2]];

Xtor[X_]:=If[X!=1,Sqrt[(X/(1-X))^2],1000]
f1=Table[{radialCoord[[j]],angularCoord[[i]],dat[[j+(i-1)*nx,1]]},{i,1,ny},{j,1,nx}];
f2=Table[{radialCoord[[j]],angularCoord[[i]],dat[[j+(i-1)*nx,2]]},{i,1,ny},{j,1,nx}];
f0=Table[{radialCoord[[j]],angularCoord[[i]],dat[[j+(i-1)*nx,3]]},{i,1,ny},{j,1,nx}];
Z=Table[{radialCoord[[j]],angularCoord[[i]],dat[[j+(i-1)*nx,4]]},{i,1,ny},{j,1,nx}];
W=Table[{radialCoord[[j]],angularCoord[[i]],dat[[j+(i-1)*nx,5]]},{i,1,ny},{j,1,nx}];
if1=Interpolation[Flatten[f1,1],InterpolationOrder->4];
if2=Interpolation[Flatten[f2,1],InterpolationOrder->4];
if0=Interpolation[Flatten[f0,1],InterpolationOrder->4];
iZ=Interpolation[Flatten[Z,1],InterpolationOrder->4];
iW=Interpolation[Flatten[W,1],InterpolationOrder->4];
f1=if1;
f2=if2;
f0=if0;
Z=iZ;
W=iW;

dat=ReadList["fx-inf.txt",{Number,Number ,Number ,Number,Number ,Number  }];
lung1=Length[dat] ;
unghi0=ReadList["gridy.dat",{Number}];
ny=Length[unghi0];


infF0=Table[dat[[i]][[4]],{i,1,lung1}]

constINF=Sum[infF0[[i]],{i,1,ny}]/ny

Mc=constINF;

MSch=rh/2 ;
Mass=MSch+Mc; 

H[r_] := 1 - rh/r;
gtt[r_,t_]:=-E^(2 f0[r,t]) H[r]+E^(2 f2[r,t]) r^2 W[r,t]^2

gttEquatorial[r_] = gtt[r,Pi/2];

findRoots[f_,xMax_]:=Block[{zeros,soln,y,x},
reaping=Reap[soln=y[x]/.First[NDSolve[{y'[x]==Evaluate[D[f[x],x]],y[xMax]==(f[xMax])},y[x],{x,xMax,10^-16},Method->{"EventLocator","Event"->y[x],"EventAction":>Sow[{x,y[x]}]}]]][[2]];
zeros = If[Length[reaping]>0,reaping[[1]],{{0,0}}];
zeros[[All,1]]]
findExtrema[f_,xMax_]:=Block[{zeros,soln,y,x},
reaping=Reap[soln=y[x]/.First[NDSolve[{y'[x]==Evaluate[D[f[x],x]],y[xMax]==(f[xMax])},y[x],{x,xMax,10^-16},Method->{"EventLocator","Event"->y'[x],"EventAction":>Sow[{x,y[x]}]}]]][[2]];
zeros = If[Length[reaping]>0,reaping[[1]],{{0,0}}];
zeros[[All,1]]]

ergoRoots=findRoots[gttEquatorial,5]
ergoExtrema=findExtrema[gttEquatorial,5]

dgttEquatorial[r_] = D[gttEquatorial[r],{r,1}];

dgttExtrema=findExtrema[dgttEquatorial,5]

output={Flatten[{{w,rh,PadRight[ergoRoots,3],PadRight[ergoExtrema,2],PadRight[dgttExtrema,4],Mass}},2]};
Print[output]
file = OpenAppend["/home/h/usb/work/scalar-HBHs-data-ER/ER-data/w="<>ToString[w]<>".dat"]

Export[file, output, "Table"];
WriteString[file, "\n"];

Close[file]

