from pydantic import BaseModel, Field, StrictInt

class InputSchema(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: int = Field(..., ge=0)
    total_rooms: StrictInt = Field(..., ge=0)
    total_bedrooms: StrictInt = Field(..., ge=0)
    population: int = Field(..., ge=0)
    households: StrictInt = Field(..., ge=0)
    median_income: float = Field(...,gt=0)

class OutputSchema(BaseModel):
    predicted_price: float

