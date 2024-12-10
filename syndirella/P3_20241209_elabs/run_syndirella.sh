#!/bin/bash

KEY=$1

cp -v $HOME2/2A_HIPPO/A71EV2A_P3only_20241209/aligned_files/$KEY/*_apo-desolv.pdb templates/

echo --input $(pwd)/$KEY"_syndirella_input.csv"
echo --hits_path $(pwd)/$KEY"_syndirella_inspiration_hits.sdf"
echo --output $(pwd)/$KEY"_elabs"
echo --metadata "/opt/xchem-fragalysis-2/maxwin/2A_HIPPO/A71EV2A_P3only_20241209/metadata.csv"
echo --templates "$(pwd)/templates"

syndirella \
	--input $(pwd)/$KEY"_syndirella_input.csv" \
	--hits_path $(pwd)/$KEY"_syndirella_inspiration_hits.sdf" \
	--output $(pwd)/$KEY"_elabs" \
	--metadata "/opt/xchem-fragalysis-2/maxwin/2A_HIPPO/A71EV2A_P3only_20241209/metadata.csv" \
	--templates "$(pwd)/templates"

# sb.sh --job-name syndirella $HOME2/slurm/run_bash_with_conda.sh ./run_syndirella.sh
