from pydantic import BaseModel, Field
from typing import Optional , List



class Element(BaseModel):
    # Place dans le pdf
    page: int = Field(description="Le numéro de la page où se trouve l'élément dans le document.")

    # Données générales
    name: str = Field(description="Le nom de l'élément, par exemple 'ascenseur' ou 'monte-charge'")
    building: Optional[str] = Field(description="Le nom du bâtiment où se trouve l'élément, réferencé comme 'batiment', si présent.")

    # Autres informations
    date_de_verification: Optional[str] = Field(description="La date de vérification (ou de prestation) de l'élément, s'il est présent. À ne pas confondre avec la date de fabrication ou la date de mise en service.")
    l_element_n_a_pas_ete_verifie: Optional[bool] = Field(description="Indique si l'élément n'a pas été vérifié, s'il est présent.")
    localisation: Optional[str] = Field(description="La localisation de l'élément, réferencée comme 'localisation' ou 'service' ou 'batiment', si présente.")


class NumeroInterne(BaseModel):
    number: str = Field(description="Le numéro d'identification entier de l'élément. Ce n'est pas une description, mais le numéro lui-même.")
    name: str = Field(description="Le type de numéro d'identification, tel que 'Numéro d'identification', 'Numéro d'équipement', 'N° identification', 'TAG', 'N° interne', 'Data Flash', 'Poste Technique', 'PT', 'N° interne'.")


class Reperes(BaseModel):
    n_serie: Optional[str] = Field(description="Le numéro de série de l'élément, s'il est présent.")
    n_internal: List[NumeroInterne] = Field(description="Les numéros internes associés à l'élément autre que le numéro de série, si présents.")