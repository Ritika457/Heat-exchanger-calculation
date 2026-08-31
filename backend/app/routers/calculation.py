from fastapi import APIRouter
from app.services.calculation_service import CalculationService
from app.models.calculation_request import CalculationRequest
from app.database.connection import get_connection

router = APIRouter()

service = CalculationService()

@router.post("/calculate")
def calculate(request: CalculationRequest):
    result = service.calculate(request)
    return result


@router.get("/history")
def get_history():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            Id,
            ShellFlow,
            ShellCp,
            TubeFlow,
            TubeCp,
            ShellInletTemp,
            ShellOutletTemp,
            TubeInletTemp,
            TubeOutletTemp,
            Area,
            R,
            S,
            A,
            B,
            C,
            FT,
            LMTD,
            CorrectedLMTD,
            ADELTLN,
            ApproachTemperature,
            Qs,
            Qt,
            UShell,
            UTube,
            CreatedDate
        FROM HeatExchangerCalculation
        ORDER BY Id DESC
    """)

    columns = [column[0] for column in cursor.description]

    data = []

    for row in cursor.fetchall():
        data.append(dict(zip(columns, row)))

    conn.close()

    return data