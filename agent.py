from langchain.agents import AgentType, initialize_agent
from langchain.agents.output_parsers import ReActSingleInputOutputParser, JSONAgentOutputParser

from langchain.chains.conversation.memory import ConversationBufferWindowMemory


# Include the LLM from a previous lesson
from llm import llm

from output_parser import OutputParser


tools = []

memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True,
)

SYSTEM_MESSAGE = """
You are a movie expert providing information about movies.
Be as helpful as possible and return as much information as possible.
Do not answer any questions that do not relate to movies, actors or directors.

Do not answer any questions using your pre-trained knowledge, only use the information provided in the context. 
"""

agent = initialize_agent(
    tools,
    llm,
    memory=memory,
    verbose=True,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    agent_kwargs={"output_parser": OutputParser(),
                  "handle_parsing_errors": True,
                  "system_message": SYSTEM_MESSAGE
                }
)

def generate_response(prompt):
    """
    Create a handler that calls the Conversational agent
    and returns a response to be rendered in the UI
    """

    prefix = """
            Respond with only JSON. Only use a tool if it is required. 
             """
    
    response = agent.run(prefix+prompt)

    # return response['output']
    return response