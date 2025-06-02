from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field

# Define Pydantic models for the desired JSON structure
class Element(BaseModel):
    number: int
    page: int
    inspector: str
    name: str
    #N_Identification: Dict[str, int]  # Assuming string keys and values; change to Dict[str, int] if number_internal is an integer
    n_internal: Optional[int] # Assuming string keys and values; change to Dict[str, int] if number_internal is an integer
    factory: str
    building: str
#    regulation : RegulationResult
    

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

# FIXED: Make fields optional for OCR step
class Observation(BaseModel):
    element_number: int = Field(description="Numéro de l'élément concerné")
    element_name: str = Field(description="Nom de l'élément concerné")
    verified_point: Optional[str] = Field(default=None, description="Point vérifié où l'observation a été faite")
    description: str = Field(description="Description courte de l'observation")
    detailed_description: Optional[str] = Field(default=None, description="Description détaillée complète")
    observation_type: Optional[str] = Field(default=None, description="Type d'observation: anomalie, défaut, action, etc.")
    suggested_priority: Optional[str] = Field(default=None, description="Priorité suggérée")
    first_emission_date: Optional[str] = Field(default=None, description="Date d'émission au format YYYY-MM-DD")
    predicted_criticality: Optional[bool] = Field(default=None, description="Criticité prédite pour la sécurité")

# UPDATED: Add observations to Report class
class Report(BaseModel):
    document: Document
    intervention_control: InterventionControl
    elements: List[Element]
    observations: List[Observation] = Field(default_factory=list, description="Liste des observations extraites")