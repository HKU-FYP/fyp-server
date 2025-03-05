from typing import Literal
from dataclasses import dataclass

from src.shared.llm.openai_llm import OpenAIChatLLM
from src.shared.llm.utils import load_prompt_messages, fill_message_placeholders


@dataclass
class NewsArticleDto:
    title: str
    content: str

@dataclass
class SentimentAnalysisResultDto:
    sentiment: Literal['Positive', 'Negative', 'Neutral']
    analysis: str

class SentimentAnalyzer:
    def __init__(self, llm: OpenAIChatLLM):
        self.llm = llm
        self.msg = load_prompt_messages("src/shared/llm/prompts/sentiment_analysis.txt")

    def analyze_sentiment(self, news_article: NewsArticleDto, stock_name: str) -> SentimentAnalysisResultDto:
        messages = fill_message_placeholders(self.msg, placeholders={
            "title": news_article.title, "content": news_article.content, "stock_name": stock_name
        })

        resp = self.llm.predict_json(messages)
        return SentimentAnalysisResultDto(sentiment=resp['sentiment'], analysis=resp['analysis'])
