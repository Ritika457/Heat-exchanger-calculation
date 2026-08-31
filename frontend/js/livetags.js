async function loadLiveTags() {

    try {

        const response = await fetch("/api/live-tags");
        const data = await response.json();

        const tbody = document.querySelector("#liveTable tbody");
        tbody.innerHTML = "";

        const tagNames = [];

        data.forEach(row => {

            tagNames.push(`'${row.Name}'`);

            tbody.innerHTML += `
                <tr>
                    <td><input type="checkbox"></td>
                    <td>${row.Name}</td>
                    <td>${row.Value}</td>
                    <td>${row.Time}</td>
                </tr>
            `;

        });

        document.getElementById("tagNames").innerText = tagNames.join(", ");

    }

    catch (error) {

        console.error(error);

    }

}
const today = new Date();

const formattedDate =
    String(today.getDate()).padStart(2, '0') + "-" +
    String(today.getMonth() + 1).padStart(2, '0') + "-" +
    today.getFullYear();

document.getElementById("currentDate").innerText = formattedDate;
loadLiveTags();

setInterval(loadLiveTags, 60000);