from typing import Optional, Dict, Any, List, Literal
from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from pydantic import Field


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
    #----------------------------------ATTRIBUTES----------------------------------
    # Just a try to add attributes juste for the moments (just for 1 kind of element)

    # type_de_traction_electrique: Optional[Literal["Entraînement par adhérence", "Entraînement attelé"]] 
    # modification_importante: Optional[Literal["Oui", "Non"]] 
    # societe_de_maintenance: Optional[str] 
    # type_de_traction_hydraulique: Optional[Literal["Entraînement direct", "Entraînement indirect"]] 
    # fabricant: Optional[str] 
    # charge_maximale_kg_var: Optional[int] 
    # date_de_fabrication: Optional[date] 
    # date_de_mise_en_service: Optional[date] 
    # parachute: Optional[Literal["Oui", "Non"]] 
    # nombre_d_etages: Optional[int] 
    # machinerie: Optional[Literal["Basse", "Haute", "Latérale", "Latérale basse", "Latérale haute", "Sans"]] 
    # nombre_de_personnes: Optional[int] 
    # motorisation: Optional[Literal["Une vitesse", "Deux vitesses", "Variateur de fréquence", "Hydraulique"]] 
    # type_de_traction: Optional[Literal["Électrique", "Hydraulique"]] 
    # type_d_ouverture: Optional[Literal["Automatique", "Manuelle"]] 
    # type_de_porte: Optional[Literal["Porte Coulissante", "Porte battante", "Porte pliante", "Porte à ouverture centrale", "Porte à guillotine"]] 
    # en_location: Optional[Literal["Oui", "Non"]] 
    # status: Optional[Literal["Actif", "Au chômage", "Au rebut", "En stock", "Au brouillon"]] 
    # vitesse_nominale_en_m_s_var: Optional[Decimal] 
    # certification_ce: Optional[Literal["Oui", "Non"]] 
    # type_de_control: Optional[Literal["Contrôle technique", "Vérification périodique"]] 


    # type_de_control : Optional[Literal['Contrôle technique', 'Vérification périodique']] = Field(description="Le type de contrôle effectué sur l'élément, si présent.")
    # date_de_mise_en_service : Optional[str] = Field(description="La date de mise en service de l'ascenseur, si présent.")
    # date_de_fabrication : Optional[str] = Field(description="La date de fabrication (peut être appelé plaque) de l'ascenseur, si présent.")
    # modification_importante : Optional[bool] = Field(description="La date de la dernière modification importante de l'ascenseur, si présent.")
    # societe_de_maintenance : Optional[str] = Field(description="La société de maintenance de l'ascenseur, si présent.")
    # fabricant : Optional[str] = Field(description="La marque du fabricant de l'ascenseur, si présent.")
    # charge_maximale_kg_var : Optional[int] = Field(description="La charge maximale en kilogrammes que l'ascenseur peut supporter, si présent.")
    # parachute : Optional[bool] = Field(description="Le parachute de l'ascenseur, si présent.")
    # nombre_d_etages : Optional[int] = Field(description="Le nombre d'étages (ou de niveaux) que l'ascenseur dessert, si présent.")
    # machinerie : Optional[Literal['Basse', 'Haute', 'Latérale', 'Latérale basse', 'Latérale haute', 'Sans', '']] = Field(description="La machinerie de l'ascenseur, si présent.")
    # nombre_de_personnes : Optional[int] = Field(description="Le nombre de personnes que l'ascenseur peut supporter, si présent.")
    # motorisation : Optional[Literal['Une vitesse', 'Deux vitesses', 'Variateur de fréquence', 'Hydraulique', '']] = Field(description="La motorisation de l'ascenseur, si présent.")
    # en_location : Optional[bool] = Field(description="L'ascenseur est-il en location, si présent.")
    # status : Optional[Literal['Actif', 'Au chômage', 'Au rebut', 'En stock', 'Au brouillon', '']] = Field(description="Le statut de l'ascenseur, si présent.")
    # vitesse_nominale_en_m_s_var : Optional[float] = Field(description="La vitesse nominale de l'ascenseur en mètres par seconde, si présent.")
    # certification_ce : Optional[bool] = Field(description="La certification CE (Conformité Européenne) de l'ascenseur, si présent.")
    # type_de_traction_electrique : Optional[Literal['Entraînement par adhérence', 'Entraînement attelé', '']] = Field(description="Le type de traction électrique de l'ascenseur, si présent.")
    # type_de_traction_hydraulique : Optional[Literal['Entraînement direct', 'Entraînement indirect', '']] = Field(description="Le type de traction hydraulique de l'ascenseur, si présent.")
    # type_de_traction : Optional[Literal['Électrique', 'Hydraulique', '']] = Field(description="Le type de traction de l'ascenseur, si présent.")
    # type_d_ouverture : Optional[Literal['Automatique', 'Manuelle', '']] = Field(description="Le type d'ouverture de l'ascenseur, si présent.")
    # type_de_porte : Optional[Literal['Porte Coulissante', 'Porte battante', 'Porte pliante', 'Porte à ouverture centrale', 'Porte à guillotine', '']] = Field(description="Le type de porte de l'ascenseur, si présent.")
    

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