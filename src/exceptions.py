
class SummarizerError(Exception):
    """Base exception for the application."""


class InvalidInputError(SummarizerError):
    """Raised when user input is invalid."""


class GeminiAPIError(SummarizerError):
    """Raised when communication with Gemini fails."""


class PromptError(SummarizerError):
    """Raised when prompt generation fails."""