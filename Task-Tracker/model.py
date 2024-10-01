from pydantic import BaseModel
from datetime import datetime as dt


class Task(BaseModel):
    id : int
    description: str 
    status: str = "todo"
    createdAt: dt
    updatedAt: dt
    
    def json_custom(self):
        return {
            "id" : self.id,
            "description" : self.description,
            "status" : self.status,
            "createdAt" : self.createdAt,
            "updatedAt" : self.updatedAt
        }
    
    
class Test(BaseModel):
    test: str = "test"