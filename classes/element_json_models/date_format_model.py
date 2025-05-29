from pydantic import BaseModel, Field



class DateFormatModel(BaseModel):
    date: str = Field(description="La date dans le format JJ/MM/AAAA.")