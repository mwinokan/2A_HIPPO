import hippo

from sqlite3 import DatabaseError

import mrich as logger

animal = hippo.HIPPO("A71EV2A_5_batch_flat", "A71EV2A_5_flat.sqlite", copy_from="A71EV2A_4.sqlite", overwrite_existing=True)

bases = animal.compounds(tag="Syndirella scaffold")
elabs = bases.elabs
products = bases + elabs

# animal.reactions.set_product_yields(type="Buchwald-Hartwig_amination", product_yield=0.1)
# animal.reactions.set_product_yields(type="Buchwald-Hartwig_amidation_with_amide-like_nucleophile", product_yield=0.1)
# animal.reactions.set_product_yields(type="Steglich_esterification", product_yield=0.1)

animal.db.execute('DROP TABLE route')
animal.db.execute('DROP TABLE component')

animal.db.create_table_route()
animal.db.create_table_component()

logger.var("products", products)

for i, c in logger.track(enumerate(products), total=len(products)):

    try:
        reactions = c.reactions
    except DatabaseError:
        logger.error(f"Error getting {c}'s reactions")
        continue

    for reaction in reactions:

        try:
            recipes = reaction.get_recipes()
        except DatabaseError:
            logger.error(f"Error getting {reaction}'s ({c}) recipes")
            continue

        for recipe in recipes:

            route = animal.register_route(recipe=recipe)

            logger.print(f"registered {route=}")

    if i % 100 == 99:
        logger.success("Committing...")
        animal.db.commit()

animal.db.close()

# sb.sh --job-name 2A_HIPPO_5 -pgpu --exclusive $HOME2/slurm/run_python.sh 5_routes.py