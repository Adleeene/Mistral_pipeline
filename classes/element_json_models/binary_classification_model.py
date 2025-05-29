from typing import Literal
from pydantic import BaseModel, Field


class BinaryClassificationModel(BaseModel):
    """
    Page classification response model.
    """
    result: Literal[
        "yes",
        "no"
    ] = Field(description="Type de la page, parmi les catégories suivantes: Yes, No")
        
    # explanation: str = Field(description="Une courte explication de ton raisonnement pour identifier cette page.")