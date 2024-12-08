from typing import List, Union

from langchain_core.documents import Document

from agents.state import FedotLLMAgentState
from agents.researcher.structured import GenerateWithCitations


class ResearcherAgentState(FedotLLMAgentState):
    """
    Represents the state of our graph.

    Attributes:
        messages: list of messages
        question: question
        generation: LLM generation
        documents: list of documents
    """
    question: str
    generation: GenerateWithCitations
    documents: List[Union[str, Document]]
    answer: str
    attempt: int = 0