#!/bin/bash

for KEY in *"_syndirella_input.csv"; do
	KEY=${KEY:0:6}
	echo $KEY

	sb.sh --job-name syndirella_$KEY --ntasks=1 --cpus-per-task=1 --mem=3GB $HOME2/slurm/run_bash_with_conda.sh run_syndirella.sh $KEY

done
