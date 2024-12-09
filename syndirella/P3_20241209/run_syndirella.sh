#!/bin/bash

export MANIFOLD_API_KEY="v1:IEgBrU-Vi4r1bBTGidyEnA"

syndirella \
	--input *_syndirella_input.csv \
	--hits_path *_syndirella_inspiration_hits.sdf \
	--output . \
	--just_retro

# sb.sh --job-name syndirella $HOME2/slurm/run_bash_with_conda.sh ./run_syndirella.sh