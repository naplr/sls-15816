
for ((x=23;x<28;x++));
do
    for ((i=1;i<=10;i++));
    do
        filename=logs/yal-$x-$i.log;
        echo Running $filename;
        R=$RANDOM; ./yalsat -v ../xor6cut/xor6cut-$x.cnf $R 10000000 > $filename;
    done
done

#R=$RANDOM; echo $R; ./yalsat -v ../xor6cut/xor6cut-27.cnf $R

