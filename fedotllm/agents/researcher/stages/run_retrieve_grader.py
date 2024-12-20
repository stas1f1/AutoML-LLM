from langchain.schema import Document

from fedotllm.agents.researcher.state import ResearcherAgentState
from fedotllm.agents.researcher.structured import GradeDocuments, BoolAnswer
from fedotllm.agents.utils import render
from fedotllm.llm.inference import AIInference
from fedotllm.settings.config_loader import get_settings


def run_retrieve_grader(state: ResearcherAgentState, inference: AIInference) -> ResearcherAgentState:
    question = state["question"]
    documents = state["documents"]

    # Score each doc
    filtered_docs = []
    for d in documents:
        if not isinstance(d, Document):
            raise ValueError("Document must be an instance of Document")
        score = GradeDocuments.model_validate(
            inference.chat_completion(*render(get_settings().get("prompts.researcher.retrieve_grader"),
                                              question=question, document=d.page_content),
                                      structured=GradeDocuments))

        grade = score.score
        if grade == BoolAnswer.YES:
            filtered_docs.append(d)
        else:
            continue
    state["documents"] = filtered_docs
    return state
