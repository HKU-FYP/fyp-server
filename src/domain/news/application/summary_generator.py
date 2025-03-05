from src.shared.llm.openai_llm import OpenAIChatLLM
from src.shared.llm.utils import load_prompt_messages, fill_message_placeholders


class SummaryGeneratorLLM:
    def __init__(self, llm: OpenAIChatLLM):
        self.llm = llm
        self.msg = load_prompt_messages("src/shared/llm/prompts/generate_summary_prompt.txt")

    def generate_summary(self, content: str) -> str:
        messages = fill_message_placeholders(self.msg, placeholders={"article_content": content})
        resp = self.llm.predict_json(messages)
        return resp["summary"]
