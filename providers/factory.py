from providers.open_ai import OpenAIProvider
from providers.googlestudio import GoogleStudioProvider

class LLMFactory:

    @staticmethod
    def create(
        provider: str,
        api_key: str,
        model: str
    ):

        providers = {
            "openai": OpenAIProvider,
            "google-studio": GoogleStudioProvider
        }

        if provider not in providers:
            raise ValueError(
                f"Unsupported provider: {provider}"
            )

        return providers[provider](
            api_key=api_key,
            model=model
        )