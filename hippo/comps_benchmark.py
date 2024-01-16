from pathlib import Path
import molparse as mp
import hippo2 as hippo
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from pprint import pprint
import json

animal = hippo.HIPPO.from_pickle('pickles/2A_hits_v2p1.pickle')

animal.summary()

syndirella_root = Path('/data/xchem-fragalysis/kfieseler/A71EV2A')

animal.add_elabs(
    syndirella_root, 
    test=100, 
    reference_hit='x0310_0A', 
    overwrite=True, 
    pickle_dump='pickles/2A_comps_bench_v2p1.pickle', 
    restart_j=0,
    debug=False
)

animal.summary()
