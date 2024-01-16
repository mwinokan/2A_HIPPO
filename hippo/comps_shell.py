#!/usr/bin/env python3

import hippo2 as hippo
import sys
import time
import mout
import argparse
from pathlib import Path

def main():
	
	parser = argparse.ArgumentParser(description="collator")
	parser.add_argument("-s", "--syndirella", help="Syndirella elaborations root path")
	parser.add_argument("-i", "--input", help="Pickle input containing a HIPPO animal")
	parser.add_argument("-o", "--output", help="Pickle output of the HIPPO animal")
	parser.add_argument("-r", "--restart", help="Restart add_elabs at this j_value (CSV index)")
	parser.add_argument("-f", "--filter", help="Require substring in elab subdirectories")
	parser.add_argument("-c", "--rmsd-cut", help="Maximum Fragmenstein mRMSD value")

	args = parser.parse_args()

	assert args.input
	assert args.output
	assert args.syndirella

	if args.rmsd_cut:
		rmsd_cut = float(args.rmsd_cut)
	else:
		rmsd_cut = None

	if args.filter:
		elabs_csv_pattern = f'elabs/*/*/*{args.filter}*/*.csv'
		placements_pattern = f'elabs/*/*/*/success/*{args.filter}*/*.minimised.mol'
	else:
		elabs_csv_pattern='elabs/*/*/*/*.csv'
		placements_pattern='elabs/*/*/*/success/*/*.minimised.mol'

	start = time.perf_counter()
	
	animal = hippo.HIPPO.from_pickle(args.input)
	
	syndirella_root = Path(args.syndirella)

	restart_j = args.restart or 0
	restart_j = int(restart_j)

	animal.add_elabs(
	    syndirella_root, 
	    reference_hit='x0310_0A', 
	    overwrite=True, 
		restart_j=restart_j,
	    pickle_dump=f'pickles/{animal.name}_comps_shell_restart.pickle', 
        elabs_csv_pattern=elabs_csv_pattern, 
		placements_pattern=placements_pattern,
		rmsd_cut=rmsd_cut,
	)

	animal.write_pickle(args.output)

	animal.summary()

	end = time.perf_counter()

	mout.var('HIPPO execution time', f'{(end-start)/60:.1f}', unit='minutes')

if __name__ == '__main__':
	main()