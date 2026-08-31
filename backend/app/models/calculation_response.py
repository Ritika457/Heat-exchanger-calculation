from pydantic import BaseModel


class CalculationResponse(BaseModel):

    r: float
    s: float

    a: float
    b: float
    c: float

    ft: float

    lmtd: float
    corrected_lmtd: float

    adeltln: float

    qs: float
    qt: float

    u_shell: float
    u_tube: float

    approach_temperature: float