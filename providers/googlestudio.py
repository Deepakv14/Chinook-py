from google import genai
from providers.llm import LLMProvider

class GoogleStudioProvider(LLMProvider):
    def __init__(self, api_key: str, model: str):
        self.api_key=api_key
        self.client = genai.Client(api_key=self.api_key)
        self.model = model

    def generate_text(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )
        content = response.text

        if content is None:
            raise ValueError("No content returned")

        return content