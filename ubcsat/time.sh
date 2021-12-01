file=../xor6cut/xor6cut-$1.cnf

#for ((i=1;i<10000000000;i*10));
for i in 1 10 100 1000 10000 100000 1000000 10000000 100000000 1000000000 10000000000;
do
  echo $i;
  for ((x=23;x<28;x++));
  do
    file=../xor6cut/xor6cut-$x.cnf;
    echo $file;

    filename=time-logs/wp-$x-$i.log;
    ./ubcsat -alg walksat -cutoff $i -wp 0.68 -runs 10 -i $file > $filename;

    filename=time-logs/jack-$x-$i.log;
    ./ubcsat -alg jack -cutoff $i -runs 10 -i $file > $filename;

  done
done
