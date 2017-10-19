#!/bin/bash
brackets=(0 9276 37651 91151 190150 413350 415050)
percent=(10 15 25 28 33 35 39)
total=0
ndx=0
if [[ $# -eq 0 ]] ; then
    echo 'Please enter a salary'
    exit 0
fi

while [ $ndx -lt 6 ]; do
    rate=$(echo "${percent[$ndx]} / 100" | bc -l )
    if [ $1 -ge ${brackets[$ndx + 1]} ]; then
	total=$(echo "$total + (${brackets[$ndx + 1]} * $rate)" | bc -l )
    else
	remainder=$(echo "$1 - ${brackets[$ndx]}" | bc -l )
	total=$(echo "$total + ($remainder * $rate)" | bc -l )
	break
    fi
    
    let ndx+=1
done

printf "%.2f\n" $total
