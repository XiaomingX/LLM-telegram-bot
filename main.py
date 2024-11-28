import commands as c  # 导入命令模块
import apikey as key  # 导入API密钥模块
from telegram.ext import Updater  # 从telegram.ext模块中导入Updater类

# 主函数
def main():
    # 使用API密钥创建Updater和Dispatcher对象
    updater = Updater(key.API_KEY, use_context=True)  # 使用apikey模块中的API_KEY进行身份验证
    dispatcher = updater.dispatcher  # 获取dispatcher对象，用于注册命令处理函数

    # 添加命令处理器
    dispatcher.add_handler(c.helpFunc)  # 添加帮助命令处理器
    dispatcher.add_handler(c.startFunc)  # 添加启动命令处理器
    dispatcher.add_handler(c.stopFunc)  # 添加停止命令处理器
    dispatcher.add_handler(c.persistFunc)  # 添加持久化命令处理器
    dispatcher.add_handler(c.IOFunc)  # 添加输入/输出命令处理器

    # 启动机器人
    updater.start_polling()  # 开始轮询以接收来自Telegram的消息
    updater.idle()  # 保持机器人运行，直到用户手动停止

# 如果该脚本是被直接运行，而不是被导入，调用main函数
if __name__ == "__main__":
    main()