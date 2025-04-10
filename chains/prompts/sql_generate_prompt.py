from langchain.prompts import PromptTemplate

sql_generate_prompt = PromptTemplate(
    input_variables=['query', 'table_name', 'table_def_sql', 'table_head', 'table_field_info'],
    template='''
    <system>
        你是一个数据库专家，你的任务是生成SQL查询语句。
    </system>

    <table name="{table_name}">
        表的定义为：
        {table_def_sql}
        表部分内容如下:
        {table_head}
        其中部分名词解释如下：
        {table_field_info}
    </table>

    <user>
        用户的查询语句为：{query}
        请根据用户的查询语句生成SQL查询语句。
    </user>

    <important>
        1. 括号中带订单的数据是指订单数据，默认选择订单数据，订单数据和非订单数据只需要选择一个
        2. 无论如何都要保证选择直播间名称和日期两个字段
        3. 根据用户查询的需求，选择对应的字段，尽可能选取相关的字段，但是不要选取无关的字段，对于大多数查询，只需要选择一个最相关的字段即可
        4. 一般来说一个查询只会用到不多于5个字段，所以不要选择太多的字段
        5. 请注意避免重复选择相同的字段
        6. 请只生成SQL语句，不要添加其他的内容，也不要添加注释，也不需要markdown的格式标记
        7. 使用as关键字来给字段添加中文名，每个字段都需要
        8. sql语句尽量换行，保持格式整齐
    </important>
    '''
)