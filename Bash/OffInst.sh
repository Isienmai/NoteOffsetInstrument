#!/bin/bash

#range is A0 -> C8, incrementing between B and C
#create new scales and swap in as necessary to include sharp/flat notes, or limit note availability

#scale=(C D E F G A B)
scale=(C Db Eb F G Ab Bb)
scaleSize=7

key=4
keyMax=7
keyMin=1

currentNote=0

#function for checking two specified inputs and incrementing/decrementing the currentNote by a given amount
#args: 1 = increment input, 2 = decrement input, 3 = increment/decrement value
function CondIncNote
{
	if [ "$input" == "$1" ]
	then
		#INCREMENT by the specified value
		((currentNote+=$3))
		
		#If this goes over the upper limit then either undo the change or update the key
		if (( currentNote >= scaleSize ))
		then
			if ((key < keyMax))
			then 
				((currentNote = currentNote % scaleSize))
				((key++))
			else
				((currentNote -= $3))
			fi
		fi
	fi

	if [ "$input" == "$2" ]
	then
		((currentNote-=$3))
		
		if (( currentNote < 0 ))
		then
			if ((key > keyMin))
			then
				((currentNote += scaleSize))
				((key--))
			else
				((currentNote += $3))
			fi
		fi
	fi
}

function CheckInput
{
	#increment the note by one
	CondIncNote w s 1	

	#increment the note by two
	CondIncNote e d 2

	#increment the note by three
	CondIncNote r f 3

	#increment the note by four
	CondIncNote t g 4

	#increment the note by five
	CondIncNote y h 5
}

while true;
do
	read -rsn1 input

	CheckInput
	
	echo ${scale[$currentNote]}$key
	play -qn synth 2 pluck ${scale[$currentNote]}$key & 
done
