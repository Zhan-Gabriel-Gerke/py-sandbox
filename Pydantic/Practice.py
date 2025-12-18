from typing import Self, Any, Optional

from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator


class Practice(BaseModel):
    sensor_id: str
    temperature: Optional[float] = Field(default=None, ge=-50, le=100)
    status: str
    is_emergency: bool = Field(default=False)

    @field_validator("sensor_id")
    @classmethod
    def validate_sensor_id(cls, value: str) -> str:
        if not value.startswith("SNS-"):
            raise ValueError("Sensor ID must start with 'SNS-'")
        return value


    # @model_validator(mode="after")
    # def validate_temperature(self) -> Self:
    #     if self.temperature > 80:
    #         self.is_emergency = True
    #     return self.temperature, self.is_emergency

    @field_validator("status")
    @classmethod
    def validate_status(cls, value: Any) -> Self:
        valid_types = ["online", "offline", "maintenance"]
        if value not in valid_types:
            raise ValueError("Status must be 'online', 'offline' or 'maintenance")
        return value

    @model_validator(mode="after")
    def check_sensor_logic(self) -> Self:
        if self.temperature is not None and self.temperature > 80:
            self.is_emergency = True

        if self.status in ["online", "maintenance"] and self.temperature is None:
            raise ValueError("The temperature is required when senser in 'online' or 'maintenance'")
        return self

# try:
#     test = Practice(sensor_id="SNS-111", temperature=44, status="online")
#     print(test.model_dump_json())
# except ValidationError as e:
#     print(e)
#
# try:
#     test1 = Practice(sensor_id="SNS-112", temperature=90, status="online")
#     print(test1.model_dump_json())
# except ValidationError as e:
#     print(e)
#
# try:
#     test2 = Practice(sensor_id="SNS-113", status="offline")
#     print(test2.model_dump_json())
# except ValidationError as e:
#     print(e)

def run_test(name, data):
    print(f"--- {name} ---")
    try:
        p = Practice(**data)
        print(p.model_dump_json(indent=2))
    except Exception as e:
        print(f"FAILED:\n{e}")

run_test("VALID ONLINE", {"sensor_id": "SNS-111", "temperature": 44, "status": "online"})
run_test("EMERGENCY", {"sensor_id": "SNS-112", "temperature": 90, "status": "online"})
run_test("VALID OFFLINE", {"sensor_id": "SNS-113", "status": "offline"})
run_test("INVALID STATUS", {"sensor_id": "SNS-114", "status": "broken"})