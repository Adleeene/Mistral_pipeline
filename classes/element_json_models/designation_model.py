from pydantic import BaseModel, Field
from typing import List , Optional


class Element(BaseModel):
    element_number: int = Field(description="L'ordre dans lequel l'élément apparait, cela peut être le N° Ordre ou le numéro de la fiche si ils sont là, sinon juste un index.")
    element_name: str = Field(description="Le nom de l'élément d'équipement (un ou plusieurs mots).")
    element_id: str = Field(description="Le numéro d’identification unique associé à l’équipement: mentionné comme **numéro de série** ou **numéro interne** ou similaire.")
    explanation: Optional[str] = Field(description="Une description de ce qu'est l'élément d'équipement.")
    arrete: Optional[str] = Field(description="Le texte de référence de l'élément d'équipement (un arrêté ministériel par exemple), si présent.")

class Designations(BaseModel):
    n_elements: int = Field(description="Le nombre d'éléments pertinants trouvés dans le text")
    elements: List[Element]