#!/bin/bash
# find prime factors of a number
# expects the number in question as an argument
# this isridiculously slow when numbers get big... even when there aren't many factors


declare answer_array
declare unique_answers


euler3(){
  numerator=$1
  local notfound=0
  for denom in $(eval echo {2..$numerator})
  do
    if [ $(( $numerator % $denom )) -eq 0 ] && [ $denom -lt $numerator ]
    then
      notfound=1
      answer_array+=("$denom")
      new_num=$(( $numerator/$denom ))
      euler3 $new_num
      break
    fi
  done

  #deal with primes as numerator
  if [ "$notfound" ]
  then
    answer_array+=("$numerator")
  fi
}

euler3 $1


# now arrange them nicely, useful for using against numbers like 64.

unique_answers+=($(for num in "${answer_array[@]}"; do echo $num; done | sort -n | uniq | xargs))
echo"${unique_answers[@]}"
