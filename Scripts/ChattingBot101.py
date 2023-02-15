import openai
import requests
import sys

# 将你的OpenAI API密钥替换成这里的字符串
openai.api_key = "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"

# 设置OpenAI API的模型ID和引擎ID
model_engine = {
    "model": "text-davinci-002",
    "engine": "davinci"
}

# 使用OpenAI API发送请求并获取响应
def ask_question(question):
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=question,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except openai.error.RateLimitError as e:
        print("OpenAI API Error: {}".format(str(e)))
        sys.exit(1)

# 命令行交互
while True:
    question = input("You: ")
    answer = ask_question(question)
    print("ChatGPT: " + answer)
