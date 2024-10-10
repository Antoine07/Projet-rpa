from typing import TypedDict, List

class TrainerPerSchoolType(TypedDict):
    trainer_name: str
    school_name: str
    total_students: int
    
class BpfType(TypedDict):
    amount: float
    totalStudent: int
    trainer_per_school: List[TrainerPerSchoolType]