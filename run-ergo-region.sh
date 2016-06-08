for dir in w=0,9{5,6,7,8,9}
do
  for rh in $dir/1st/0,*
  do
    echo $rh
    cp ergo-region.m $rh
    cd $rh
    math -script ergo-region.m > ergo-region-output.txt
    rm ergo-region.m
    cd ../../../
  done
  for rh in $dir/2nd/0,*(On)
  do
    echo $rh
    cp ergo-region.m $rh
    cd $rh
    math -script ergo-region.m > ergo-region-output.txt
    rm ergo-region.m
    cd ../../../
  done
done
