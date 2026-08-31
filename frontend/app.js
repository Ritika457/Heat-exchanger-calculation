const pageContent = document.getElementById("pageContent");

document.getElementById("calculateBtn").addEventListener("click", showCalculatePage);
document.getElementById("historyBtn").addEventListener("click", showHistoryPage);

showCalculatePage();


// =========================
// Calculate Page
// =========================

function showCalculatePage() {

    pageContent.innerHTML = `

    <div class="calculation-layout">

        <!-- LEFT SIDE : INPUTS -->
        <div class="input-section">

            <div class="input-header">
                <span>Tags</span>
                <span>Values</span>
            </div>
            <div class="form">

                <label>Shell Flow</label>
                <input type="number" id="shell_flow">

                <label>Shell Cp</label>
                <input type="number" id="shell_cp">

                <label>Tube Flow</label>
                <input type="number" id="tube_flow">

                <label>Tube Cp</label>
                <input type="number" id="tube_cp">

                <label>Shell Inlet Temp</label>
                <input type="number" id="shell_inlet_temp">

                <label>Shell Outlet Temp</label>
                <input type="number" id="shell_outlet_temp">

                <label>Tube Inlet Temp</label>
                <input type="number" id="tube_inlet_temp">

                <label>Tube Outlet Temp</label>
                <input type="number" id="tube_outlet_temp">

                <label>Area</label>
                <input type="number" id="area">

                <br><br>

                <button id="calculate">Calculate</button>

            </div>

        </div>


        <!-- RIGHT SIDE : CURRENT CALCULATION -->
        <div class="result-section">

            <h2>Current Calculation</h2>

            <div id="currentCalculation">

            </div>

        </div>

    </div>
    `;

    document
        .getElementById("calculate")
        .addEventListener("click", calculateHeatExchanger);

    loadLiveValues();
    setInterval(loadLiveValues, 60000);
}

async function loadLiveValues() {

    try {

        const response = await fetch("/api/live-tags");
        const data = await response.json();

        const getTagValue = (tagName) => {
            const tag = data.find(row => row.Name === tagName);
            return tag ? Number(tag.Value) : "";
        };

        // Live values
        document.getElementById("shell_flow").value =
            getTagValue("201FIC2601PV");

        document.getElementById("tube_flow").value =
            getTagValue("201FI1102PV");

        document.getElementById("shell_inlet_temp").value =
            getTagValue("201TI2603PV");

        document.getElementById("shell_outlet_temp").value =
            getTagValue("201TI1103PV");

        document.getElementById("tube_inlet_temp").value =
            getTagValue("201TI1102PV");

        document.getElementById("tube_outlet_temp").value =
            getTagValue("201TI1104PV");

        // Fixed values
        document.getElementById("shell_cp").value = 0.5105;
        document.getElementById("tube_cp").value = 0.455;
        document.getElementById("area").value = 354;

    }
    catch (error) {

        console.error("Failed to load live values:", error);

    }
}


// =========================
// History Page
// =========================

function showHistoryPage() {

    pageContent.innerHTML = `

    <h2>Calculation History</h2>


    <br><br>

    <table id="historyTable" border="1" width="100%">

        <thead>
            <tr>
                <th>ID</th>
                <th>Shell Flow</th>
                <th>Shell Cp</th>
                <th>Tube Flow</th>
                <th>Tube Cp</th>
                <th>Qs</th>
                <th>Qt</th>
                <th>U Shell</th>
                <th>U Tube</th>

                <th>Shell Inlet Temperature</th>
                <th>Shell Outlet Temperature</th>
                <th>Tube Inlet Temperature</th>
                <th>Tube Outlet Temperature</th>

                <th>Area</th>

                <th>R</th>
                <th>S</th>
                <th>A</th>
                <th>B</th>
                <th>C</th>
                <th>FT</th>

                <th>LMTD</th>
                <th>Corrected LMTD</th>
                <th>ADELTLN</th>

                <th>Approach Temp</th>

                <th>Created Date</th>
            </tr>
        </thead>

        <tbody>

        </tbody>

    </table>

    `;

    loadHistory();
}

// =========================
// Calculate API
// =========================

async function calculateHeatExchanger() {

    const data = {

        shell_flow: parseFloat(document.getElementById("shell_flow").value),
        shell_cp: Number(document.getElementById("shell_cp").value),
        tube_flow: parseFloat(document.getElementById("tube_flow").value),
        tube_cp: Number(document.getElementById("tube_cp").value),

        shell_inlet_temp: Number(
            document.getElementById("shell_inlet_temp").value
        ),

        shell_outlet_temp: Number(
            document.getElementById("shell_outlet_temp").value
        ),

        tube_inlet_temp: Number(
            document.getElementById("tube_inlet_temp").value
        ),

        tube_outlet_temp: Number(
            document.getElementById("tube_outlet_temp").value
        ),

        area: Number(document.getElementById("area").value)
    };


    try {

        const response = await fetch("/api/calculate", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)

        });


        const result = await response.json();


        if (!response.ok) {
            throw new Error(result.detail || "Calculation failed");
        }


        console.log(result);

        showCurrentCalculation(data, result);

        alert("Calculation Successful");

    }

    catch (error) {

        console.error(error);

        alert("Calculation Failed: " + error.message);

    }
}

function showCurrentCalculation(input, result) {

    const container = document.getElementById("currentCalculation");

    if (!container) return;


    container.innerHTML = `

        <h3>Input Values</h3>

        <div class="result-grid">

            <div><span>Shell Cp</span><strong>${input.shell_cp}</strong></div>
            <div><span>Tube Cp</span><strong>${input.tube_cp}</strong></div>

            <div><span>Shell Inlet Temp</span><strong>${input.shell_inlet_temp}</strong></div>
            <div><span>Shell Outlet Temp</span><strong>${input.shell_outlet_temp}</strong></div>

            <div><span>Tube Inlet Temp</span><strong>${input.tube_inlet_temp}</strong></div>
            <div><span>Tube Outlet Temp</span><strong>${input.tube_outlet_temp}</strong></div>

            <div><span>Area</span><strong>${input.area}</strong></div>

        </div>


        <h3>Calculated Values</h3>

        <div class="result-grid">

            <div>
                <span>R</span>
                <strong>${Number(result.r).toFixed(3)}</strong>
            </div>

            <div>
                <span>S</span>
                <strong>${Number(result.s).toFixed(3)}</strong>
            </div>

            <div>
                <span>A</span>
                <strong>${Number(result.a).toFixed(3)}</strong>
            </div>

            <div>
                <span>B</span>
                <strong>${Number(result.b).toFixed(3)}</strong>
            </div>

            <div>
                <span>C</span>
                <strong>${Number(result.c).toFixed(3)}</strong>
            </div>

            <div>
                <span>FT</span>
                <strong>${Number(result.ft).toFixed(3)}</strong>
            </div>

            <div>
                <span>LMTD</span>
                <strong>${Number(result.lmtd).toFixed(2)}</strong>
            </div>

            <div>
                <span>Corrected LMTD</span>
                <strong>${Number(result.corrected_lmtd).toFixed(2)}</strong>
            </div>

            <div>
                <span>ADELTLN</span>
                <strong>${Number(result.adeltln).toFixed(2)}</strong>
            </div>

            <div>
                <span>Approach Temperature</span>
                <strong>${Number(result.approach_temperature).toFixed(2)}</strong>
            </div>

        </div>

    `;
}



// =========================
// Load History
// =========================

async function loadHistory() {

    try {

        const response = await fetch("/api/history");

        const data = await response.json();

        const tbody = document.querySelector("#historyTable tbody");

        if (!tbody) return;

        tbody.innerHTML = "";

        data.forEach(item => {

            tbody.innerHTML += `
                <tr>
                    <td>${item.Id}</td>

                    <td>${item.ShellFlow}</td>
                    <td>${item.ShellCp}</td>

                    <td>${item.TubeFlow}</td>
                    <td>${item.TubeCp}</td>

                    <td>${item.Qs.toFixed(3)}</td>
                    <td>${item.Qt.toFixed(3)}</td>
                    <td>${item.UShell.toFixed(3)}</td>
                    <td>${item.UTube.toFixed(3)}</td>

                    <td>${item.ShellInletTemp}</td>
                    <td>${item.ShellOutletTemp}</td>

                    <td>${item.TubeInletTemp}</td>
                    <td>${item.TubeOutletTemp}</td>

                    <td>${item.Area}</td>

                    <td>${item.R.toFixed(2)}</td>
                    <td>${item.S.toFixed(2)}</td>
                    <td>${item.A.toFixed(2)}</td>
                    <td>${item.B.toFixed(2)}</td>
                    <td>${item.C.toFixed(2)}</td>

                    <td>${item.FT.toFixed(3)}</td>

                    <td>${item.LMTD.toFixed(1)}</td>
                    <td>${item.CorrectedLMTD.toFixed(1)}</td>

                    <td>${item.ADELTLN.toFixed(1)}</td>

                    <td>${item.ApproachTemperature.toFixed(2)}</td>

                    <td>${item.CreatedDate}</td>
                </tr>
            `;
        });

    }
    catch (error) {

        console.error(error);

    }
}