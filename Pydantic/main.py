from typing import Self, Any

from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator

class HyperSkillUser(BaseModel):
    name: str = Field(min_length=8, max_length=20)
    active_subscription: bool = Field(default=True)
    active_moths: int = Field(gt=0, lt=13)

    @field_validator('name')
    @classmethod
    def name_must_contain_space(cls, value: str) -> str:
        if ' ' in value:
            raise ValueError("Name must not contain space")
        return value.title()

    @model_validator(mode='after')
    def validate_subscription_consistency(self) -> Self:
        """Ensure active_months aligns with subscription status"""
        if self.active_subscription and self.active_moths == 0:
            raise ValueError("Active subscription requires mwonths > 0")
        if not self.active_subscription and self.active_moths > 0:
            raise ValueError("Active subscription must have 0 active months")
        return self

    @model_validator(mode="before")
    def valudate_input(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            raise ValueError("Data should not be dictionary format")
        return data

    @model_validator(mode="wrap")
    @classmethod
    def validate_logic(cls, validate_data: Any):
        """
            Validate subscription logic after processing raw input and field-level validation.
            """
        if validate_data["active_subscription"] and validate_data["active_months"] == 0:
            raise ValueError("Active subscription requires at least 1 active month")
        if not validate_data['active_subscription'] and validate_data['active_months'] > 0:
            raise ValueError("Inactive subscription cannot have active months")
        return validate_data


# ge : greater or equal to
# le: lesser or equal to
# gt: greater than
# lt: less than

user = HyperSkillUser(name="John_Gabriel", active_subscription=True, active_moths=3)

data = {"name": "John_Gabriel", "active_subscription": True, "active_moths": 3}
user = HyperSkillUser(**data)
print(user)


# try:
#     user = HyperSkillUser(name="John", active_subscription=True, active_moths="Thee")
#     print(user.name)
# except Exception as e:
#     print(e)

print(type(user.model_dump_json()))
print(user.model_dump_json())

print(type(user.model_dump()))
print(user.model_dump())

person = HyperSkillUser(name="John_Gabriel", active_moths=4)
print(person)



# try:
#     user = HyperSkillUser(name="John Doe", active_subscription=True, active_moths=3)
#     print(user)
# except ValidationError as e:
#     print(e)

try:
    user = HyperSkillUser(name="Alice_Smith_ffff", active_subscription=False, active_moths=5)
    print(f"Valid user: {user}")
except ValidationError as e:
    print(e)

