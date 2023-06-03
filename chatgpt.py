from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


openai_api_key = 'xxxxxxx'
chat = ChatOpenAI(temperature=0.7,openai_api_key=openai_api_key,verbose=True)


template="Your name is Raj. Your are build by Raj Krishna Mondal, a Data Scientist. The following is a friendly conversation between a human and an Raj. The Raj is talkative and provides lots of specific details from its context. If the Raj does not know the answer to a question, it truthfully says it does not know."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template="{input}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])



def gptchat(query):
    # get a chat completion from the formatted messages
    prompt=chat_prompt.format_prompt(input=query).to_messages()
    return chat(prompt).content


