file=../xor6cut/xor6cut-26.cnf

for ((i=1;i<100;i++));
do
  if [[ $i -gt 9 ]]
  then
    wp=0.$i
  else
    wp=0.0$i
  fi
  echo Running wp=$wp;

  filename=wp-sweep/wp-$wp.log
  ./ubcsat -alg walksat -cutoff 10000000 -wp $wp -runs 10 -i $file > $filename;
done
