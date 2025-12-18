from pydantic import BaseModel, Field, ValidationError


class OpenAIRequest(BaseModel):
    model: str = Field(..., description="The model yo use, e.g., 'gpt-3.5-turbo'")
    temperature: float = Field(default=0.7, ge=0, le=2, description="Controls randomness(0-2)")
    max_tokens: int = Field(default=256, ge=1, le=4096, description="Maximum number of tokens")
    prompt: str = Field(..., min_length=1, description="The input prompt for the model")

request_data = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.8,
    "max_tokens": 150,
    "prompt": "What is the capital of France?"
}


try:
    validated_request = OpenAIRequest(**request_data)
    print(f"Validated request: {validated_request}")
except ValidationError as e:
    print("Validation Error:", e)