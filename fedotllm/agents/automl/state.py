from typing import List
from typing import TypedDict, Optional
from agents.automl.structured import ProblemReflection, FedotConfig
from agents.automl.eval.local_exec import ExecutionResult
from agents.state import FedotLLMAgentState


class Solution(TypedDict):
    code: str
    exec_result: ExecutionResult
    fix_tries: int = 0


class AutoMLAgentState(FedotLLMAgentState):
    description: str
    reflection: Optional[ProblemReflection] = None
    fedot_config: Optional[FedotConfig] = None
    skeleton: Optional[str] = None
    codegen_sol: Solution
    solutions: List[Solution] = []
    exec_result: Optional[ExecutionResult] = None
    metrics: Optional[dict] = None
    pipeline: Optional[dict] = None