from app.models.calculation_response import CalculationResponse
from app.repositories.calculation_repository import CalculationRepository

from app.calculations.heat_duty import (
    calculate_qs,
    calculate_qt
)

from app.calculations.constants import (
    calculate_r,
    calculate_s,
    calculate_a,
    calculate_b,
    calculate_c,
    calculate_ft

)
from app.calculations.lmtd import (
    calculate_lmtd,
    corrected_lmtd
)
from app.calculations.heat_transfer import (
    approach_temperature,
    calculate_adeltln,
    calculate_u_shell,
    calculate_u_tube
)
class CalculationService:

    def calculate(self, request):

        r = calculate_r(
            request.shell_inlet_temp,
            request.shell_outlet_temp,
            request.tube_inlet_temp,
            request.tube_outlet_temp
        )

        s = calculate_s(
            request.shell_inlet_temp,
            request.tube_inlet_temp,
            request.tube_outlet_temp
        )

        a = calculate_a(r, s)
        b = calculate_b(r, s)
        c = calculate_c(r, s)
        ft = calculate_ft(a, b, c)

        lmtd = calculate_lmtd(
            request.shell_inlet_temp,
            request.shell_outlet_temp,
            request.tube_inlet_temp,
            request.tube_outlet_temp
        )

        corrected = corrected_lmtd(
            lmtd,
            ft
        )

        adeltln = calculate_adeltln(
            request.area,
            corrected
        )

        qs = calculate_qs(
            request.shell_flow,
            request.shell_cp,
            request.shell_inlet_temp,
            request.shell_outlet_temp
        )

        qt = calculate_qt(
            request.tube_flow,
            request.tube_cp,
            request.tube_inlet_temp,
            request.tube_outlet_temp
        )

        u_shell = calculate_u_shell(qs, adeltln)
        u_tube = calculate_u_tube(qt, adeltln)

        approach = approach_temperature(
            request.shell_inlet_temp,
            request.tube_outlet_temp
        )

        response = CalculationResponse(

            r=r,
            s=s,

            a=a,
            b=b,
            c=c,

            ft=ft,

            lmtd=lmtd,
            corrected_lmtd=corrected,

            adeltln=adeltln,

            qs=qs,
            qt=qt,

            u_shell=u_shell,
            u_tube=u_tube,

            approach_temperature=approach
        )
        CalculationRepository.save_calculation(request, response)

        return response
