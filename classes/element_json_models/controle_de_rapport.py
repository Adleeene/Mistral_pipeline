from pydantic import BaseModel, Field
from typing import Optional



class Document(BaseModel):
    """
    A class used to represent the PDF Document.
    """
    number: str = Field(description="Le numéro ou la référence du document, ce n'est pas le numéro de l'équipement.")
    date: str = Field(description="La date de rédaction du document, le format doit être 'DD-MM-YYYY'.")
    # pages_number set to len(input_document) in the document extraction loop
    # name set to the file_name from the url in the document extraction loop
    nombre_de_fiches: Optional[int] = Field(description="Le nombre de fiches dans le document, si c'est explicitement mentionné dans le document.")



class InspectionReport(BaseModel):
    name: str = Field(description="Le nom du control d'intervention.") # Peut-être a enlever
    start_date: str = Field(description="La date de début du control d'intervention, le format doit être 'DD-MM-YYYY'.")
    end_date: str = Field(description="La date de fin du control d'intervention (cela peut-être la même que celle de début si l'intervention n'a duré qu'un jour), le format doit être 'DD-MM-YYYY'.")

    # Inspector
    inspector_company: Optional[str] = Field(description="L'agence supervisant le control d'intervention, tel que apave, bureau veritas, etc.")
    inspector_agency: Optional[str] = Field(description="La ville de l'entreprise qui a effectué le control d'intervention.")
    inspector_name: Optional[str] = Field(description="L'inspecteur ou l'intervenant ou le vérificateur en charge du control d'intervention.")
    
    # Customer
    customer_company: Optional[str] = Field(description="Le nom de l'entrepise du client")
    customer_address: Optional[str] = Field(description="L'adresse où le control d'intervention est effectué.")
    # customer_factory: Optional[str] = Field(description="Le nom du site si il est explicitement mentionné comme 'Site : Nom du site'. Sinon laisser vide.")