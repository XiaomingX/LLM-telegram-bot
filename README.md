# LLM-Telegram-Chatbot

这个 Telegram 聊天机器人是一个基于 Python 的机器人，用户可以通过 GPT4all Python 库和 python-telegram-bot 库与语言模型 (LLM) 进行交流。这个 README 提供了项目的概述以及如何快速上手的说明。

## 目录

- [LLM-Telegram-Chatbot](#llm-telegram-chatbot)
  - [目录](#目录)
  - [准备工作](#准备工作)
  - [快速上手](#快速上手)
  - [使用方法](#使用方法)
  - [指令](#指令)
  - [自定义语言模型](#自定义语言模型)
  - [贡献](#贡献)

## 准备工作

在使用 Telegram 聊天机器人之前，请确保您具备以下条件：

- 系统中安装了 Python 3。
- 已安装 [requirements.txt](requirements.txt) 文件中指定的必要 Python 库。可以通过以下命令安装它们：
  ```bash
  pip install -r requirements.txt
  ```

## 快速上手

1. 将项目代码克隆到本地：
   ```bash
   git clone https://github.com/Fatal3xcept10n/LLM-Telegram-Chatbot.git
   ```
2. 进入项目文件夹：
   ```bash
   cd LLM-Telegram-Chatbot
   ```
3. 安装所需的 Python 库：
   ```bash
   pip install -r requirements.txt
   ```
4. 生成 Telegram 机器人的 API 密钥：
   - 在 Telegram 上访问 BotFather，创建您的机器人并获取 API 密钥。
   - 在项目文件夹中创建一个名为 `apikey.py` 的文件。
   - 编辑该文件，添加以下内容，并将 [API 密钥] 替换为您自己的密钥：
     ```python
     API_KEY = '[API 密钥]'
     ```

## 使用方法

启动机器人，运行 [main.py](main.py) 文件：
```bash
python main.py
```
您可以在 Telegram 上通过以下命令与机器人互动：

- `/help`: 显示帮助菜单。
- `/hello`: 开始与机器人对话。
- `/stop`: 停止当前对话。
- `/persistence`: （目前不可用）切换会话持久化功能（即将推出）。

![菜单图片](https://github.com/Fatal3xcept10n/LLM-Telegram-Chatbot/blob/master/images/helpmenu.png?raw=true)

![对话图片](https://github.com/Fatal3xcept10n/LLM-Telegram-Chatbot/blob/master/images/conversation.png?raw=true)

## 指令

- 主要的命令处理逻辑位于 [commands.py](commands.py) 文件中。
- 您可以修改和扩展这些命令，以自定义机器人的行为。

## 自定义语言模型

在 [chatbot.py](chatbot.py) 文件中，您可以自定义机器人使用的语言模型 (LLM)。您还可以调整 LLM 的参数和设置，以满足您的需求。

## 贡献

欢迎任何形式的贡献！如果您想为项目做出贡献，请遵循以下步骤：
- Fork 本仓库。
- 为您的功能或修复创建一个新分支。
- 提交您的更改并推送到您的 Fork 中。
- 创建一个拉取请求 (Pull Request)，并详细描述您的更改。
