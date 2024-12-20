import hippo
import pandas as pd
from pathlib import Path
import os
import numpy as np

import mrich as logger

logger.var("hippo", hippo.__file__)

animal = hippo.HIPPO("2A_HIPPO_3_batch", "A71EV2A_3.sqlite")
# animal = hippo.HIPPO("2A_HIPPO_3_batch", "A71EV2A_3.sqlite", copy_from="A71EV2A.sqlite")

inspiration_map = {
  "A71EV2A-x0152_A_147_1_A71EV2A-x0525+A+246+1": 41,
  "A71EV2A-x0152_A_201_1_A71EV2A-x0395+A+148+1": 40,
  "A71EV2A-x0188_A_147_1_A71EV2A-x0541+A+147+1": 1,
  "A71EV2A-x0194_A_147_1_A71EV2A-x0395+A+148+1": 42,
  "A71EV2A-x0202_A_147_1_A71EV2A-x0395+A+148+1": 43,
  "A71EV2A-x0202_A_201_1_A71EV2A-x0488+A+147+1": 44,
  "A71EV2A-x0207_A_151_1_A71EV2A-x0526+A+147+1": 2,
  "A71EV2A-x0228_A_147_1_A71EV2A-x0525+A+246+1": 45,
  "A71EV2A-x0229_A_147_1_A71EV2A-x0525+A+246+1": 46,
  "A71EV2A-x0229_A_201_1_A71EV2A-x0541+A+147+1": 47,
  "A71EV2A-x0237_A_151_1_A71EV2A-x0526+A+147+1": 48,
  "A71EV2A-x0239_A_147_1_A71EV2A-x0486+A+147+1": 49,
  "A71EV2A-x0269_A_147_1_A71EV2A-x0395+A+148+1": 32,
  "A71EV2A-x0278_A_147_1_A71EV2A-x0541+A+147+1": 34,
  "A71EV2A-x0278_A_201_1_A71EV2A-x0525+A+246+1": 33,
  "A71EV2A-x0305_A_147_1_A71EV2A-x0541+A+147+1": 35,
  "A71EV2A-x0309_A_147_1_A71EV2A-x0486+A+147+1": 36,
  "A71EV2A-x0310_A_147_1_A71EV2A-x0526+A+147+1": 37,
  "A71EV2A-x0332_A_147_1_A71EV2A-x0541+A+147+1": 50,
  "A71EV2A-x0333_A_201_1_A71EV2A-x3181+A+202+1": 51,
  "A71EV2A-x0341_A_147_1_A71EV2A-x0395+A+148+1": 52,
  "A71EV2A-x0351_A_201_1_A71EV2A-x0432+A+147+1": 53,
  "A71EV2A-x0351_A_301_1_A71EV2A-x0526+A+147+1": 54,
  "A71EV2A-x0351_A_302_1_A71EV2A-x3181+A+202+1": 55,
  "A71EV2A-x0354_A_147_1_A71EV2A-x0541+A+147+1": 56,
  "A71EV2A-x0359_A_147_1_A71EV2A-x0525+A+246+1": 57,
  "A71EV2A-x0365_A_201_1_A71EV2A-x0526+A+147+1": 58,
  "A71EV2A-x0375_A_147_1_A71EV2A-x0395+A+148+1": 59,
  "A71EV2A-x0375_A_201_1_A71EV2A-x0526+A+147+1": 60,
  "A71EV2A-x0375_A_301_1_A71EV2A-x0526+A+147+1": 61,
  "A71EV2A-x0379_A_147_1_A71EV2A-x0379+A+147+1": 62,
  "A71EV2A-x0387_A_151_1_A71EV2A-x0526+A+147+1": 63,
  "A71EV2A-x0395_A_147_1_A71EV2A-x0395+A+148+1": 64,
  "A71EV2A-x0395_A_148_1_A71EV2A-x0395+A+148+1": 65,
  "A71EV2A-x0396_A_147_1_A71EV2A-x0396+A+147+1": 66,
  "A71EV2A-x0412_A_147_1_A71EV2A-x0412+A+147+1": 67,
  "A71EV2A-x0416_A_147_1_A71EV2A-x0526+A+147+1": 68,
  "A71EV2A-x0428_A_147_1_A71EV2A-x0541+A+147+1": 69,
  "A71EV2A-x0432_A_147_1_A71EV2A-x0432+A+147+1": 70,
  "A71EV2A-x0437_A_250_1_A71EV2A-x0526+A+147+1": 71,
  "A71EV2A-x0443_A_250_1_A71EV2A-x0526+A+147+1": 72,
  "A71EV2A-x0450_A_201_1_A71EV2A-x0526+A+147+1": 5,
  "A71EV2A-x0451_A_201_1_A71EV2A-x0526+A+147+1": 6,
  "A71EV2A-x0469_A_147_1_A71EV2A-x0525+A+246+1": 7,
  "A71EV2A-x0473_A_147_1_A71EV2A-x0526+A+147+1": 8,
  "A71EV2A-x0486_A_147_1_A71EV2A-x0486+A+147+1": 9,
  "A71EV2A-x0487_A_250_1_A71EV2A-x0526+A+147+1": 10,
  "A71EV2A-x0488_A_147_1_A71EV2A-x0488+A+147+1": 11,
  "A71EV2A-x0497_A_147_1_A71EV2A-x0395+A+148+1": 12,
  "A71EV2A-x0501_A_151_1_A71EV2A-x0526+A+147+1": 13,
  "A71EV2A-x0501_A_152_1_A71EV2A-x0526+A+147+1": 14,
  "A71EV2A-x0514_A_250_1_A71EV2A-x3181+A+202+1": 16,
  "A71EV2A-x0514_B_151_1_A71EV2A-x0526+A+147+1": 15,
  "A71EV2A-x0515_A_147_1_A71EV2A-x0395+A+148+1": 17,
  "A71EV2A-x0515_A_201_1_A71EV2A-x0526+A+147+1": 18,
  "A71EV2A-x0517_A_147_1_A71EV2A-x0517+A+147+1": 19,
  "A71EV2A-x0525_A_246_1_A71EV2A-x0525+A+246+1": 20,
  "A71EV2A-x0526_A_147_1_A71EV2A-x0526+A+147+1": 21,
  "A71EV2A-x0528_A_147_1_A71EV2A-x0526+A+147+1": 22,
  "A71EV2A-x0528_A_201_1_A71EV2A-x3181+A+202+1": 23,
  "A71EV2A-x0540_A_147_1_A71EV2A-x0525+A+246+1": 24,
  "A71EV2A-x0541_A_147_1_A71EV2A-x0541+A+147+1": 25,
  "A71EV2A-x0554_A_147_1_A71EV2A-x0554+A+147+1": 27,
  "A71EV2A-x0554_A_201_1_A71EV2A-x0526+A+147+1": 26,
  "A71EV2A-x0556_A_147_1_A71EV2A-x0526+A+147+1": 28,
  "A71EV2A-x0566_A_147_1_A71EV2A-x0526+A+147+1": 29,
  "A71EV2A-x0571_A_147_1_A71EV2A-x0517+A+147+1": 30,
  "A71EV2A-x0586_A_147_1_A71EV2A-x0541+A+147+1": 31,
  "A71EV2A-x0608_A_147_1_A71EV2A-x0486+A+147+1": 38,
  "A71EV2A-x0691_A_201_1_A71EV2A-x0541+A+147+1": 39,
  "A71EV2A-x0717_A_147_1_A71EV2A-x0541+A+147+1": 74,
  "A71EV2A-x0719_A_201_1_A71EV2A-x3181+A+202+1": 76,
  "A71EV2A-x0719_A_301_1_A71EV2A-x0526+A+147+1": 75,
  "A71EV2A-x0732_A_201_1_A71EV2A-x0526+A+147+1": 77,
  "A71EV2A-x0739_A_147_1_A71EV2A-x0526+A+147+1": 78,
  "A71EV2A-x0812_A_147_1_A71EV2A-x0526+A+147+1": 79,
  "A71EV2A-x0831_A_147_1_A71EV2A-x0395+A+148+1": 80,
  "A71EV2A-x0836_A_301_1_A71EV2A-x0526+A+147+1": 81,
  "A71EV2A-x0836_A_302_1_A71EV2A-x0526+A+147+1": 82,
  "A71EV2A-x0853_A_147_1_A71EV2A-x0526+A+147+1": 83,
  "A71EV2A-x0863_A_147_1_A71EV2A-x3181+A+202+1": 84,
  "A71EV2A-x0875_A_147_1_A71EV2A-x0395+A+148+1": 85,
  "A71EV2A-x0875_A_201_1_A71EV2A-x0526+A+147+1": 86,
  "A71EV2A-x0884_A_147_1_A71EV2A-x0526+A+147+1": 87,
  "A71EV2A-x0900_A_147_1_A71EV2A-x0900+A+147+1": 88,
  "A71EV2A-x0911_A_147_1_A71EV2A-x0526+A+147+1": 89,
  "A71EV2A-x0922_A_147_1_A71EV2A-x0526+A+147+1": 90,
  "A71EV2A-x1080_A_201_1_A71EV2A-x0526+A+147+1": 3,
  "A71EV2A-x1105_A_148_1_A71EV2A-x0395+A+148+1": 97,
  "A71EV2A-x1109_A_147_1_A71EV2A-x0395+A+148+1": 98,
  "A71EV2A-x1128_A_147_1_A71EV2A-x0900+A+147+1": 99,
  "A71EV2A-x1140_A_147_1_A71EV2A-x0526+A+147+1": 100,
  "A71EV2A-x1145_A_147_1_A71EV2A-x3181+A+202+1": 102,
  "A71EV2A-x1145_A_201_1_A71EV2A-x0395+A+148+1": 101,
  "A71EV2A-x1146_A_147_1_A71EV2A-x3181+A+202+1": 103,
  "A71EV2A-x1148_A_147_1_A71EV2A-x0395+A+148+1": 104,
  "A71EV2A-x1148_A_201_1_A71EV2A-x0526+A+147+1": 105,
  "A71EV2A-x1169_A_151_1_A71EV2A-x0526+A+147+1": 106,
  "A71EV2A-x1180_A_151_1_A71EV2A-x0526+A+147+1": 108,
  "A71EV2A-x1180_B_151_1_A71EV2A-x0526+A+147+1": 109,
  "A71EV2A-x1209_A_151_1_A71EV2A-x0526+A+147+1": 110,
  "A71EV2A-x1247_A_246_1_A71EV2A-x0526+A+147+1": 111,
  "A71EV2A-x1255_B_201_1_A71EV2A-x0526+A+147+1": 112,
  "A71EV2A-x1292_A_151_1_A71EV2A-x0526+A+147+1": 113,
  "A71EV2A-x1293_A_151_1_A71EV2A-x0395+A+148+1": 114,
  "A71EV2A-x1346_A_250_1_A71EV2A-x0526+A+147+1": 115,
  "A71EV2A-x1445_B_201_1_A71EV2A-x0526+A+147+1": 116,
  "A71EV2A-x1445_B_301_1_A71EV2A-x0526+A+147+1": 117,
  "A71EV2A-x1775_A_201_1_A71EV2A-x0526+A+147+1": 118,
  "A71EV2A-x1776_A_201_1_A71EV2A-x0526+A+147+1": 119,
  "A71EV2A-x1778_A_201_1_A71EV2A-x0526+A+147+1": 120,
  "A71EV2A-x1779_A_201_1_A71EV2A-x0526+A+147+1": 121,
  "A71EV2A-x2290_A_301_1_A71EV2A-x0526+A+147+1": 122,
  "A71EV2A-x2293_A_201_1_A71EV2A-x0526+A+147+1": 123,
  "A71EV2A-x2304_A_246_1_A71EV2A-x0526+A+147+1": 124,
  "A71EV2A-x2339_A_246_1_A71EV2A-x0526+A+147+1": 125,
  "A71EV2A-x2351_A_246_1_A71EV2A-x0526+A+147+1": 126,
  "A71EV2A-x2448_A_246_1_A71EV2A-x0541+A+147+1": 127,
  "A71EV2A-x2454_A_246_1_A71EV2A-x0526+A+147+1": 128,
  "A71EV2A-x2458_A_246_1_A71EV2A-x0541+A+147+1": 129,
  "A71EV2A-x2513_A_301_1_A71EV2A-x0526+A+147+1": 130,
  "A71EV2A-x2629_A_246_1_A71EV2A-x0526+A+147+1": 131,
  "A71EV2A-x2846_A_301_1_A71EV2A-x0526+A+147+1": 132,
  "A71EV2A-x3066_A_301_1_A71EV2A-x0526+A+147+1": 107,
  "A71EV2A-x3286_A_201_1_A71EV2A-x0526+A+147+1": 4,
  "A71EV2A-x0926_A_250_1_A71EV2A-x0526+A+147+1": 91,
}

output_root = Path("/opt/xchem-fragalysis-2/kfieseler/A71EV2A_run5")

for file in output_root.glob("*-*-?/*to_hippo*"):

    inchikey=file.name[:27]

    base = animal.compounds[inchikey]

    ref = [animal.poses[t.removeprefix("template: ")] for t in base.tags if t.startswith("template: ")][0]
    
    animal.add_syndirella_elabs(file, reference=ref, inspiration_map=inspiration_map)
    

animal.db.close()

# sb.sh --job-name 2A_HIPPO_3 --exclusive --no-requeue $HOME2/slurm/run_python.sh 3_load_elabs.py
