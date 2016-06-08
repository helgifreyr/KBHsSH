for dir in w=0,8*
do
  for rh in $dir/1st/0,*
  do
    echo $rh
    cp light-rings.m $rh
    cd $rh
    math -script light-rings.m > light-ring-output.txt
    rm light-rings.m
    cd ../../../
  done
  for rh in $dir/2nd/0,*(On)
  do
    echo $rh
    cp light-rings.m $rh
    cd $rh
    math -script light-rings.m > light-ring-output.txt
    rm light-rings.m
    cd ../../../
  done
done
