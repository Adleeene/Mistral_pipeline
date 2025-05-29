from pydantic import BaseModel, Field



class FindCityModel(BaseModel):
    ville: str = Field(description="Le nom de la ville, si présent")