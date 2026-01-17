from pydantic import BaseModel

class BookCreate(BaseModel):
    id:int
    title:str
    author:str
    
class BookResponse(BaseModel):
    id:int
    title:str
    author:str
    available:bool