#!/bin/bash
# expects limit as argument to execution: ./euler2.bash limit
# By considering the terms in the Fibonacci sequence, find the sum of the even-valued terms.

a=1
b=2
c=3     # could also leave this as 0 ... results are same because line 19 the first time through makes proper adjustment
        # just depends how you want to kludge it all together to get rolling
total=2 # account for b term start
declare -a euler_array
euler_array=(1 2)


while [ "$c" -le "$1" ]
do
  if [[ $(( $c % 2 )) -eq 0 ]]
  then
    let "total += $c"
  fi
  let "c = $a + $b" 
  euler_array+=("$c")
  let "a = $b"
  let "b = $c"
done

# echo "${euler_array[@]}" # recall extra term in array at end.
echo $total
