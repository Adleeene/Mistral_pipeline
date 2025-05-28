from typing import Optional, Dict, Any, List
from pydantic import BaseModel

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

class Report(BaseModel):
    document: Document
    intervention_control: InterventionControl
    elements: List[Element]