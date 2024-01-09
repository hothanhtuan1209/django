from enum import Enum


class ActiveStatus(Enum):
    """
    Enum representing the active status of an entity.

    Attributes:
        ACTIVE (str): Represents the active status.
        DISABLED (str): Represents the disabled status
    """

    ACTIVE = "Active"
    DISABLED = "Disabled"


class Gender(Enum):
    """
    Enum representing the gender of an individual.

    Attributes:
        MALE (str): Represents the male gender.
        FEMALE (str): Represents the female gender.
        OTHER (str): Represents other or non-binary gender.
    """

    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"
