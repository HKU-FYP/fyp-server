from dataclasses import dataclass

from src.shared.llm.openai_llm import OpenAIChatLLM
from src.shared.llm.utils import load_prompt_messages, fill_message_placeholders


@dataclass
class FinancialMetricsResultDto:
    metrics: list[str]

class FinancialMetricAnalyzer:
    def __init__(self, llm: OpenAIChatLLM):
        self.llm = llm
        self.msg = load_prompt_messages("src/shared/llm/prompts/analyze_metrics.txt")

    def analyze_metrics(self, content: str) -> FinancialMetricsResultDto:
        messages = fill_message_placeholders(self.msg, placeholders={
            "content": content})

        resp = self.llm.predict_json(messages)
        return FinancialMetricsResultDto(metrics=resp["key_metrics"])
