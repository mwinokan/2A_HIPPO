
import hippo
import mrich

# share a database
animal = hippo.HIPPO("A71EV2A_8", "A71EV2A_7.sqlite")

gen = hippo.RandomRecipeGenerator.from_json(db=animal.db, path="A71EV2A_6_rgen.json")

for i in range(500):
    mrich.header("i=", i)
    r = gen.generate(
            shuffle=True,  
            budget=10000, 
            max_products=1200, 
            max_reactions=3000, 
            max_iter=5000, 
            currency='EUR', 
            debug=False,
            balance_clusters=True,
        )

for j in range(500):
    mrich.header("j=", j)
    r = gen.generate(
            shuffle=True,  
            budget=15000, 
            max_products=1200, 
            max_reactions=3000, 
            max_iter=5000, 
            currency='EUR', 
            debug=False,
            balance_clusters=True,
        )
    
animal.db.close()

# sb.sh --job-name 2A_HIPPO_8_rgen $HOME2/slurm/run_python.sh 8_rgen.py
