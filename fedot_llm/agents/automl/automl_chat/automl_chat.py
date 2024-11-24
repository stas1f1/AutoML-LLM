from fedot_llm.agents.automl.automl import AutoMLAgent
from fedot_llm.agents.automl.llm.inference import AIInference
from fedot_llm.agents.automl.data.data import Dataset
from fedot_llm.agents.automl.state import AutoMLAgentState
from fedot_llm.agents.automl.automl_chat.stages.run_accept_task import run_accept_task
from fedot_llm.agents.automl.automl_chat.stages.run_send_message import run_send_message
from langgraph.graph import START, END, StateGraph
from functools import partial

class AutoMLAgentChat:
    def __init__(self, inference: AIInference, dataset: Dataset):
        self.inference = inference
        self.dataset = dataset
        self.automl = AutoMLAgent(inference=self.inference, dataset=self.dataset)

    def create_graph(self):
        workflow = StateGraph(AutoMLAgentState)
        workflow.add_node("accept_task", run_accept_task)
        workflow.add_node("AutoMLAgent", self.automl.create_graph())
        workflow.add_node("send_message", partial(run_send_message, inference=self.inference))

        workflow.add_edge(START, "accept_task")
        workflow.add_edge("accept_task", "AutoMLAgent")
        workflow.add_edge("AutoMLAgent", "send_message")
        workflow.add_edge("send_message", END)
        return workflow.compile().with_config(config={"run_name": "AutoMLAgentChat"})
