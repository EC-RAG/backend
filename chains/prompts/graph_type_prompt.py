from langchain.prompts import PromptTemplate 

graph_type_prompt = PromptTemplate(
    input_variables=["query", "data_schema"],
    template="""
    <system>
    你是一个数据可视化助手。根据下面的数据结构和用户的意图，推荐一个最合适的图表类型（使用 Plotly Express）并给出字段对应关系。
    </system>

    <user>
    用户查询如下：
    {query}
    </user>
    
    <table>
    数据结构如下：
    {data_schema}
    </table>

    <assistant>
    1. 柱状图（bar chart）：
    - 用于对比不同类别（如：地区、产品、部门）在某项数值上的差异（如：销售额、数量）
    - 示例：比较各城市的销售额

    2. 折线图（line chart）：
    - 适合展示连续时间序列趋势（如：每天、每月的变化）
    - 示例：展示近一个月每日的用户活跃数

    3. 饼状图（pie chart）：
    - 用于展示组成结构，表示整体中每一部分的占比（适用于少量分类，<10类）
    - 示例：展示各品类在总销售额中占比

    4. 散点图（scatter plot）：
    - 用于展示两个数值变量之间的关系（相关性/分布）
    - 示例：查看用户年龄与购买金额的关系

    5. 面积图（area chart）：
    - 和折线图类似，用于展示数值随时间的变化，强调累计或比例变化
    - 示例：展示各业务线用户增长趋势

    6. 箱型图（box plot）：
    - 展示数值数据的分布情况（中位数、极值、异常值），适用于对比不同组的分布
    - 示例：比较各地区的订单金额分布

    请根据以下内容进行判断：
    - 表的字段结构（字段名及含义）
    - 用户的自然语言查询意图
    - 数据类型和用途
    - 图表说明中的建议
    </assistant>

    <important>
    1. 已知数据以dataframe的格式存储在变量data中
    2. 使用Plotly Express库进行可视化
    3. 回答中只需要给出代码，无需解释，也不需要markdown格式标记
    4. 生成的图表对象名为fig，无需调用show()方法
    5. 请导入必要的库
    6. 如果是数值类数据，请确保横纵坐标按序列排列
    </important>
    """
)