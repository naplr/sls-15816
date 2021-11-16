cat algos.txt | while read line
do
  name=${line//[[:blank:]]/};

  for file in ../xor6cut/*;
  do
    echo Running -alg $line on $file;

    #filename=logs7/$name-${file:19:2}.log
    #./ubcsat -alg $line -cutoff 1000000 -runs 10 -i $file > $filename;

    filename=logs8/$name-${file:19:2}.log
    ./ubcsat -alg $line -cutoff 10000000 -runs 10 -i $file > $filename;
  done
done
