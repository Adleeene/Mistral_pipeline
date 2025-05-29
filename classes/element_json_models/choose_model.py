from pydantic import BaseModel, Field



class ResponseModel(BaseModel):
    response: str = Field(description="La réponse du modèle de comparaison.")
