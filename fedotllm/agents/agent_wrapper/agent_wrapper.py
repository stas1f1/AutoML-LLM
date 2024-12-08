from functools import partial

from langgraph.graph import END, START, StateGraph

from agents.agent_wrapper.stages.run_entry_state_connector import \
    run_entry_state_connector
from agents.agent_wrapper.stages.run_exit_state_connector import \
    run_exit_state_connector
from agents.automl.automl import AutoMLAgent
from agents.automl.state import AutoMLAgentState
from agents.base import Agent
from agents.researcher.researcher import ResearcherAgent
from agents.researcher.state import ResearcherAgentState


class AgentWrapper(Agent):
    def __init__(self, agent: Agent):
        self.agent = agent

    def create_graph(self):
        if isinstance(self.agent, ResearcherAgent):
            workflow = StateGraph(ResearcherAgentState)
        elif isinstance(self.agent, AutoMLAgent):
            workflow = StateGraph(AutoMLAgentState)

        workflow.add_node('run_entry_state_connector', partial(
            run_entry_state_connector, agent=self.agent))
        workflow.add_node('agent', self.agent.create_graph())
        workflow.add_node('run_exit_state_connector', partial(
            run_exit_state_connector, agent=self.agent))

        workflow.add_edge(START, 'run_entry_state_connector')
        workflow.add_edge('run_entry_state_connector', 'agent')
        workflow.add_edge('agent', 'run_exit_state_connector')
        workflow.add_edge('run_exit_state_connector', END)

        return workflow.compile()