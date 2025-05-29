from pydantic import BaseModel, Field



class CleanDateModel(BaseModel):
    date: str = Field(description="La date nettoyée, sans aucun autre mot ou information.")