# C 算命机器人
# 服务器端：接口 -》 langchain -〉 deepseek
# 客户端： 电报机器人、微信机器人、website
# 接口： http、https、websocket


#服务器：
1. 接口访问，python选型fastapi
2. /chat的接口，post请求
3. /add_ursl 从url中学习知识
4. /add_pdfs 从pdf里学习知识
5. /add_texts 从txt文本里学习

#人性化
1. 用户输入-》AI判断一下当前问题的情绪倾向？->判断-》反馈 -》agent判断
2. 工具调用： 用户发起请求->agent判断使用哪个工具->带着相关的参数去请求工具 -> 得到观察结果