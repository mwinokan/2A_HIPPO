import hippo

from sqlite3 import DatabaseError

import mrich

animal = hippo.HIPPO("A71EV2A_7", "A71EV2A_7.sqlite") #, copy_from="A71EV2A_6.sqlite", overwrite_existing=True)

gen = hippo.RandomRecipeGenerator.from_json(animal.db, "A71EV2A_6_rgen.json")

poses = gen.route_pool.products.poses

mrich.var("poses", poses)

for pose in mrich.track(poses, prefix="Interactions"):
    try:
        pose.calculate_interactions()
    except NotImplementedError as e:
        mrich.error("Failed interaction calculation", str(e))

animal.db.close()

# sb.sh --job-name 2A_HIPPO_7 $HOME2/slurm/run_python.sh 7_interactions.py
