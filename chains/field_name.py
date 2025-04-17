from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

from .documents import database_document
from .llms.deepseek import llm
import json


prompt = PromptTemplate(
    input_variables=['query' ,'name' ,'text', 'important', 'knowledge'],
    template='''
    <system>
        你是一个语义搜索引擎，你的任务是提取用户查询语句中的涉及的字段名。
    </system>

    <user>
        用户的要求查询的表名为{name}, 这张表的基本定义如下：
        {text}
        冒号前的数据为字段名，格式为<中文字段名>(英文字段名): <字段解释> | <字段类型> | <是否为主键>

        其中部分名词解释如下：
        {knowledge}

        有一下几点需要注意：
        {important}

        请提取用户查询语句中的字段名，要求严格按照一下格式输出为json格式的数组,不要有多余的输出：
            field_name_zh: <中文字段名>,
            field_name_en: <英文字段名>,
            field_type: <字段类型>,
            field_explain: <字段解释>
        
        !!!!输出时不需要保留mrakdown的json标记!!!!
    </user>
    '''
)

field_name_chain = prompt | llm

# # test
# response = field_name_chain.invoke({
#     'query': '查询数据日表每天直播时长和带货金额的联系',
#     'name': database_document['summary_data_day']['name'],
#     'text': database_document['summary_data_day']['text'],
#     'important': database_document['summary_data_day']['important'],
#     'knowledge': database_document['summary_data_day']['knowledge']
# })
# print(response['text'])

# data = json.loads(response['text'])
# print(data)
