from pydantic import BaseModel


class CalculationRequest(BaseModel):

    shell_flow: float
    shell_cp: float

    tube_flow: float
    tube_cp: float

    shell_inlet_temp: float
    shell_outlet_temp: float

    tube_inlet_temp: float
    tube_outlet_temp: float

    area: float