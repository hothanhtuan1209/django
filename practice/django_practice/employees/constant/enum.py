from enum import Enum


class ActiveStatus(Enum):
    ACTIVE = "Active"
    DISABLED = "Disabled"


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"
