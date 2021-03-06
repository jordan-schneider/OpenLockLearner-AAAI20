import logging
import time

from openlockagents.OpenLockLearner.causal_classes.SchemaStructureSpace import (
    AbstractSchemaStructureSpace,
)
from openlockagents.OpenLockLearner.generator.chain_generator import (
    generate_chain_structure_space,
)
from openlockagents.OpenLockLearner.io.causal_structure_io import (
    write_causal_structure_space,
    write_schema_structure_space,
)
from openlockagents.OpenLockLearner.util.common import ACTIONS, FLUENT_STATES, FLUENTS


def generate_hypothesis_space(
    env,
    structure,
    causal_chain_structure_space_path,
    two_solution_schemas_structure_space_path,
    three_solution_schemas_structure_space_path,
    attributes,
    actions=ACTIONS,
    fluents=FLUENTS,
    fluent_states=FLUENT_STATES,
    perceptually_causal_relations=None,
    max_delay: int = 0,
):
    t = time.time()
    causal_chain_structure_space = generate_chain_structure_space(
        env=env,
        actions=actions,
        attributes=attributes,
        fluents=fluents,
        fluent_states=fluent_states,
        perceptually_causal_relations=perceptually_causal_relations,
        structure=structure,
        max_delay=max_delay,
    )
    write_causal_structure_space(
        causal_chain_structure_space=causal_chain_structure_space,
        causal_chain_structure_space_path=causal_chain_structure_space_path,
    )

    logging.info(
        "Chains saved to {}. Chain generation time: {}s".format(
            causal_chain_structure_space_path, time.time() - t
        )
    )

    t = time.time()

    two_solution_schemas = AbstractSchemaStructureSpace(
        causal_chain_structure_space.structure, 2, draw_chains=False
    )
    write_schema_structure_space(
        schema_structure_space=two_solution_schemas,
        schema_structure_space_path=two_solution_schemas_structure_space_path,
    )

    logging.info(
        "Two solution schemas saved to {}. Schema generation time: {}s".format(
            two_solution_schemas_structure_space_path, time.time() - t
        )
    )

    t = time.time()
    three_solution_schemas = AbstractSchemaStructureSpace(
        causal_chain_structure_space.structure, 3, draw_chains=False
    )
    write_schema_structure_space(
        schema_structure_space=three_solution_schemas,
        schema_structure_space_path=three_solution_schemas_structure_space_path,
    )

    logging.info(
        "Three solution schemas saved to {}. Schema generation time: {}s".format(
            three_solution_schemas_structure_space_path, time.time() - t
        )
    )
