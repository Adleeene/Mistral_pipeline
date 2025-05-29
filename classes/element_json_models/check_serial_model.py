from pydantic import BaseModel, Field



class CheckSerialModel(BaseModel):
    n_serie : str = Field(description="Uniquement le numéro de série de l'équipement, sans les autre information.")