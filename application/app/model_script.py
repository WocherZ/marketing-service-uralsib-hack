from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI
from .local_settings import OPENAI_API_KEY

PROMPT_NAME = "Продукт является [функционал, характеристика, качество и т.д.] и предназначен для [целевая аудитория, использование и т.д.]. Пожалуйста, сгенерируйте креативное название для этого продукта."

PROMPT_ADVERTISMENT = "Мы разработали уникальный продукт, который [описание преимущества или проблемы, которую он решает]. Наш продукт обладает [характеристики или функции продукта]. Он идеально подходит для [целевая аудитория] и поможет вам [достижение цели или решение проблемы]. Доверьтесь нашему продукту и получите [выгода или результат от использования продукта]"

def get_answer_by_model(prompt, input):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.3, openai_api_key=OPENAI_API_KEY)
    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=input)
    ]

    response=chat(messages)
    return response.content
def get_name_by_model(product_describtion):
    product_name = get_answer_by_model(PROMPT_NAME, product_describtion)
    return product_name

def get_advertisment(product_describtion):
    product_adbertisment = get_answer_by_model(PROMPT_ADVERTISMENT, product_describtion)
    return product_adbertisment