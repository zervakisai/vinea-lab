from pydantic import BaseModel, Field
from datetime import datetime


class Block(BaseModel):
    id: str
    location: str
    variety: str
    area_stremmata: float = Field(gt=0)
    soil_type: str
    root_depth_cm: float = Field(gt=0, le=300)
    irrigation_type: str

class HourlyWeather(BaseModel):
	block_id : str
	timestamp : datetime
	temp_C : float
	rel_humid : float = Field(ge=0,le=100)	
	air_speed : float = Field(ge=0)
	rain : float = Field(ge=0)


