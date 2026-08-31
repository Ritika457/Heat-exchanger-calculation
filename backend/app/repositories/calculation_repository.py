from app.database.connection import get_connection


class CalculationRepository:

    @staticmethod
    def save_calculation(request, response):

        connection = None
        cursor = None

        try:

            connection = get_connection()
            cursor = connection.cursor()

            query = """

                INSERT INTO HeatExchangerCalculation
                (
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
                    Qs,
                    Qt,
                    UShell,
                    UTube,
                    ApproachTemperature
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """

            cursor.execute(
                query,

                request.shell_flow,
                request.shell_cp,
                request.tube_flow,
                request.tube_cp,

                request.shell_inlet_temp,
                request.shell_outlet_temp,

                request.tube_inlet_temp,
                request.tube_outlet_temp,

                request.area,

                response.r,
                response.s,
                response.a,
                response.b,
                response.c,
                response.ft,
                response.lmtd,
                response.corrected_lmtd,
                response.adeltln,
                response.qs,
                response.qt,
                response.u_shell,
                response.u_tube,
                response.approach_temperature

            )

            connection.commit()

        except Exception:
            if connection:
                connection.rollback()
            raise

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()