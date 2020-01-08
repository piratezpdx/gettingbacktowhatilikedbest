#!/bin/bash
# https://projecteuler.net/problem=4
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


# expects largest number of x number of digits as argument. eg: 999 for 3 digits
# this is slow, I wouldn't do it with 4 digits...

product=0
palindrome=0
m1=0
m2=0

is_palin() {
  # just look at largest ten percent or so of numbers...
  # our answer should lie in that range

  let "a = $1 * 9 / 10"
  for i in $(eval echo {$1..$a})
  do
    for j in $(eval echo {$i..$a})
    do
      let "product = $i * $j"
      if [[ "$(echo $product | rev)" == "$product" ]]
      then
        if [[ $product -gt $palindrome ]]
        then
          palindrome=$product
          m1=$i
          m2=$j
        fi
      fi
    done
  done

  echo "palindrome : $palindrome from $m1 * $m2"
}

is_palin $1
