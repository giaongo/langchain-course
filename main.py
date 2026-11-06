import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    llm = ChatOpenAI(
        model="Qwen/Qwen2.5-1.5B-Instruct",
        base_url=os.environ["VERDA_ENDPOINT2"].rstrip("/") + "/v1",
        api_key=os.environ["VERDA_API_KEY2"],
        temperature=0,
        max_tokens=2000,
        timeout=180,
    )

    response = llm.invoke("Explain security in AI")
    print(response)
    return response.content


if __name__ == "__main__":
    main()
