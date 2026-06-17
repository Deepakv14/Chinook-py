from openai import OpenAI
from providers.llm import LLMProvider

class OpenAIProvider(LLMProvider):
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)
        self.model = model

    def generate_text(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        content = response.choices[0].message.content   
        if content is None:
            raise ValueError("No content returned")

        return content 