for dir in w=0,7/2nd/0,*
do 
  echo $dir
  cp light-rings.m $dir
  cd $dir
  math -script light-rings.m > light-ring-output.txt
  rm light-rings.m
  cd ../../../
done

mv LR-ER-w=0.7.dat LR-ER-w=0.7-2nd.dat
