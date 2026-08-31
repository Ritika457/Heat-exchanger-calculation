document.getElementById("loginForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const errorMessage = document.getElementById("error-message");

    errorMessage.textContent = "";

    try {
        const response = await fetch("/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username,
                password
            })
        });

        const data = await response.json();

        if (data.success) {
            sessionStorage.setItem("isLoggedIn", "true");
            console.log("LOGIN SUCCESS - ONLY DASHBOARD");
        //    window.open("livetags.html", "_blank");
            window.location.href = "dashboard.html";;
        } else {
            errorMessage.textContent = "Invalid User ID or Password";
        }

    } catch (error) {
        errorMessage.textContent = "Unable to connect to server.";
    }
});