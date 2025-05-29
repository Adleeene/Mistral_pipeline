from typing import Literal
from pydantic import BaseModel, Field



class PageClassificationModel(BaseModel):
    """
    Page classification response model.
    """
    result: Literal[
        "page_de_garde_couverture", 
        "page_remplie_de_reglementations_code_de_travail",
        "page_qui_decrit_un_equipement", 
        "page_avec_des_observations"
    ] = Field(description="Type de la page, parmi les catégories suivantes: page_de_garde_couverture, page_remplie_de_reglementations_code_de_travail, page_qui_decrit_un_equipement, page_avec_des_observations.")
    
    # explanation: str = Field(description="Une courte explication de ton raisonnement pour identifier cette page.")