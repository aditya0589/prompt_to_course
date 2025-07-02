from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def get_chat_response(subject: str, timeframe: str) -> str:
    template = template = """
    I want to learn {subject} in {timeframe}.
    Give me a detailed course structure including:
    1. Weekly breakdown of topics
    2. Tools/technologies to use
    3. Project ideas
    4. Free resources (with YouTube channel names and their links)
    make sure the youtube channels are valid and are the LATEST AVAILABLE ONES.
    5. Final capstone project
    Also give some daily and weekly targets if possible.

    Respond in clean, readable markdown or bullet-point format (not JSON).
    """


    prompt_template = PromptTemplate(template=template, input_variables=["subject", "timeframe"])
    llm = ChatGroq(model='llama3-70b-8192')
    chain = prompt_template | llm

    res = chain.invoke({"subject": subject, "timeframe": timeframe})

    # Convert to plain string (content of AI message)
    response_text = res.content if hasattr(res, "content") else str(res)

    return response_text
