#!/bin/bash

while true;
do
	read -rsn1 input
	declare -u input
	if [[ $input == [A-G] ]]; then
		play -qn synth 2 pluck $input & 
	fi
done
