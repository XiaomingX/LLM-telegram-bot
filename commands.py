from telegram.ext import CommandHandler, MessageHandler, Filters
import threading
import chatbot as cb

# 这个函数用来处理 LLM 的输入和输出
# 从用户获取输入，传递给机器人，并将回复输出给用户
def IOhandler(update, context):
    if cb.isRunning:
        # 获取用户的输入
        cb.prompt = update.message.text
        print("\n机器人正在运行，获取输入：" + cb.prompt)
        # 向用户发送 "正在思考..." 以告知用户正在处理
        context.bot.send_message(chat_id=update.effective_chat.id, text='正在思考...')
        # 发出事件告知机器人开始处理
        cb.promptEvent.set()
        # 等待机器人处理完成
        cb.responseEvent.wait()
        # 清除事件，为下次使用做准备
        cb.responseEvent.clear()
        print("完成，回复内容：" + cb.response)
        # 向用户发送机器人的回复
        context.bot.send_message(chat_id=update.effective_chat.id, text=cb.response)

IOFunc = MessageHandler(Filters.text, IOhandler)

# 显示帮助信息，使用 /help 命令
def help(update, context):
    update.message.reply_text("这个机器人允许你使用 Telegram 与 LLM 进行沟通！\n\n/help 显示此帮助页面\n/hello 开始沟通\n/stop 停止沟通\n/persistence [on|off] 切换讨论记录保留")

helpFunc = CommandHandler('help', help)

# 使用 /hello 命令启动 LLM
def hello(update, context):
    if cb.isRunning == False:
        cb.isRunning = True
        # 开始新的讨论线程
        conversationThread = threading.Thread(target=cb.startConversation)
        conversationThread.start()
        context.bot.send_message(chat_id=update.effective_chat.id, text='你好！输入一个输入来开始讨论...')
    else:
        update.message.reply_text("讨论已经在进行中...")

startFunc = CommandHandler('hello', hello)

# 使用 /stop 命令停止 LLM
def stop(update, context):
    if cb.isRunning == False:
        update.message.reply_text("没有什么可停止的...")
    else:
        update.message.reply_text("已停止...")
        cb.isRunning = False

stopFunc = CommandHandler('stop', stop)

# 启用实验性的讨论保留，使用 /persistence [on|off] 命令
def persistence(update, context):
    if cb.isRunning == False:
        if len(context.args) == 1:
            param = context.args[0].lower()
            
            if param == "on":
                cb.persistance = True
                update.message.reply_text("讨论保留已启用...")
            elif param == "off":
                cb.persistance = False
                update.message.reply_text("讨论保留已关闭...")
            else:
                update.message.reply_text("未知的参数：" + param)
        else:
            update.message.reply_text("用法：/persistence [on|off]")
    else:
        update.message.reply_text("必须先停止讨论才能切换保留状态...")

persistFunc = CommandHandler('persistence', persistence, pass_args=True)