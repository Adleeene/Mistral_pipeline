from typing import Optional
from pydantic import BaseModel, Field



class ResponseModel(BaseModel):
    explication: str = Field(description="L'explication de ce que signifie le terme recherché.")
    arrete: Optional[str] = Field(description="L'arrêté ministériel mentionné dans les résultats de la recherche.")
