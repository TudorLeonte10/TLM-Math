from pydantic import BaseModel, Field

class PowRequest(BaseModel):
    base: float = Field(..., description="Base number")
    exp: float = Field(..., description="Exponent")

class FibRequest(BaseModel):
    n: int = Field(..., ge=0, description="n-th Fibonacci index")

class FactRequest(BaseModel):
    n: int = Field(..., ge=0, description="Factorial input")

class ResultResponse(BaseModel):
    result: float
