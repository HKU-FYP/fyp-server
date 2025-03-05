from pyexpat.errors import messages
from dataclasses import dataclass

from src.shared.llm.openai_llm import OpenAIChatLLM
from src.shared.llm.utils import load_prompt_messages, fill_message_placeholders

@dataclass
class StockImpactAnalysisResultDto:
    easy: str
    intermediate: str
    expert: str

class StockImpactAnalyzer:
    def __init__(self, llm: OpenAIChatLLM):
        self.llm = llm
        self.msg = load_prompt_messages("src/shared/llm/prompts/analyze_stock_impact.txt")

    def analyze_stock_impact(self, stock: str, content: str) -> StockImpactAnalysisResultDto:
        messages = fill_message_placeholders(self.msg, placeholders={
            'stock': stock,
            'content': content
        })

        resp = self.llm.predict_json(messages)
        return StockImpactAnalysisResultDto(resp['easy'], resp['intermediate'], resp['expert'])


