from typing import Optional, Dict, Any, List, Literal, Union, Type
from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from pydantic import Field,validator,create_model,root_validator,model_validator,AfterValidator,ValidationInfo
from .element_json_models import *
from typing_extensions import Self,TypeVar,override,Annotated






# FIXED: Make fields optional for OCR step
class Observation(BaseModel):
    element_number: int = Field(description="Index de l'élément concerné")
    n_serie: str = Field(description="Numéro de l'élément concerné, peut etre un string par exemple : 1137/45SHZ568 ")
    element_name: str = Field(description="Nom de l'élément concerné")
    verified_point: Optional[str] = Field(default="", description="Point vérifié où l'observation a été faite")
    description: str = Field(description="Description courte de l'observation")
    detailed_description: Optional[str] = Field(default="", description="Description détaillée complète")
    observation_type: Optional[str] = Field(default="", description="Type d'observation: anomalie, défaut, action, etc.")
    suggested_priority: Optional[str] = Field(default="", description="Priorité suggérée")
    first_emission_date: Optional[str] = Field(default="", description="Date d'émission au format YYYY-MM-DD")
    predicted_criticality: bool = Field(default="", description="Criticité prédite pour la sécurité")
    observation_number: str = Field(description="Numéro de l'observation")
    
class n_internal (BaseModel) : 
    number_name : str = Field(description="Nom du Numéro d'identification de l'élément")
    number_internal :str = Field(description="Numéro d'identification de l'élément")
    

class Element(BaseModel,extra="allow" ):
    number: str
    pages: list[int] = Field(description="Toutes les pages ou cet element precis est present")
    inspector: str
    name: str
    # n_internal: Optional[List[str]] = Field(description="Numéro d'identification de l'élément")
    n_internal : List[n_internal]
    factory: str
    building: str
    regulation: Literal["ascenseurs", "mont_charge"]
    l_element_n_a_pas_ete_verifie: bool = Field(description="Indique si l'élément n'a pas été vérifié, s'il est présent.")



class Document(BaseModel):
    name: str
    number: int
    date: str  # Format YYYY-MM-DD
    pages_number: int 

class InterventionControl(BaseModel):
    name: str
    start_date: str  # Format YYYY-MM-DD
    end_date: str  # Format YYYY-MM-DD
    inspector_company: str
    inspector_agency: str
    inspector_name: str
    customer_company: str
    customer_adress: str
    customer_factory: str
    elements_number: int
    tasks_number: int



class Report(BaseModel):
    document: Document
    intervention_control: InterventionControl
    elements: List[Element]
    observations: List[Observation] = Field(description=" Les observations des éléments si présentes, si l'observation n'est pas indiquée explicitement, extrait les avis ou les remarques sous forme de phrase descriptive sur l'element")
    # elements: List[Element]








     