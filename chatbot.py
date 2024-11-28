# 导入GPT4All库和线程模块
from gpt4all import GPT4All
import threading

# 选择语言模型
model = GPT4All("gpt4all-13b-snoozy-q4_0.gguf")

# 定义一些状态变量
isRunning = False  # 表示对话是否正在进行
prompt = ""  # 存储用户输入的提示词
response = ""  # 存储模型生成的响应

# 定义线程事件，用于控制提示词和响应的处理
promptEvent = threading.Event()
responseEvent = threading.Event()

# 启动对话的函数
# 这个函数会不断监听用户输入，并生成相应的回答
def startConversation():
    global isRunning, prompt, response, promptEvent, responseEvent

    # 使用模型的对话会话
    with model.chat_session():
        while isRunning:
            # 等待用户输入提示词
            promptEvent.wait()
            promptEvent.clear()
            print("处理用户输入: " + prompt)
            response = generateResponse(prompt)  # 生成对提示词的响应
            print("处理完成")
            responseEvent.set()  # 通知主线程响应已经生成
        print("退出会话...")

# 生成对用户输入的响应
# 这个函数调用GPT4All模型来生成答案
def generateResponse(prompt):
    return model.generate(
        prompt,
        max_tokens=200,  # 最大生成的词数
        temp=0.7,  # 控制生成的多样性
        top_k=40,  # 从概率前k个单词中选择下一个单词
        top_p=0.4,  # 使用概率累计方法选择单词
        repeat_penalty=1.18,  # 惩罚重复生成的词
        repeat_last_n=64,  # 针对最近生成的64个单词进行重复惩罚
        n_batch=8,  # 一次生成的批次大小
        n_predict=None,  # 默认不设置预测步数
        streaming=False  # 不使用流式生成
    )