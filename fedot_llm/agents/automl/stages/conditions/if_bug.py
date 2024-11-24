
from fedot_llm.agents.automl.state import AutoMLAgentState
from fedot_llm.agents.automl.eval.local_exec import ProgramStatus
from fedot_llm.log import get_logger
from settings.config_loader import get_settings

logger = get_logger()


def if_bug(state: AutoMLAgentState):
    solution = state['solutions'][-1]
    codegen = state['codegen_sol']
    if solution['exec_result'].program_status == ProgramStatus.kSuccess or solution['exec_result'].program_status == ProgramStatus.kTimeout:
        return False
    elif codegen['fix_tries'] > get_settings().config.fix_tries:
        logger.error("Too many fix tries")
        return False
    else:
        return True
