from dataclasses import dataclass

from src.shared.llm.openai_llm import OpenAIChatLLM
from src.shared.llm.utils import load_prompt_messages, fill_message_placeholders


@dataclass
class KeywordGenerationResultDto:
    keywords: list[str]

class ExampleKeywordsGenerator:
    def __init__(self, llm: OpenAIChatLLM):
        self.llm = llm
        self.msg = load_prompt_messages("src/shared/llm/prompts/generate_keyword.txt")

    def generate_keywords(self, stock_name: str) -> KeywordGenerationResultDto:
        messages = fill_message_placeholders(self.msg, placeholders={
            'stock_name': stock_name})

        resp = self.llm.predict_json(messages)
        return KeywordGenerationResultDto(resp['keywords'])
