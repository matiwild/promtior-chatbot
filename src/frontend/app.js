document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const questionInput = document.querySelector("input");
    const answerDiv = document.querySelector("#answer");
    const errorDiv = document.querySelector("#error");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();
        const question = questionInput.value.trim();

        if (!question) {
            errorDiv.textContent = "Please ask a question!";
            errorDiv.style.display = "block"; 
            answerDiv.style.display = "none"; 
            return;
        }

        try {
            const response = await fetch("https://promtior-chatbot-production.up.railway.app/ask", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ question }),
            });

            if (!response.ok) {
                throw new Error("Failed to get answer from backend");
            }

            const data = await response.json();
            answerDiv.textContent = data.answer;
            answerDiv.style.display = "block";
            errorDiv.style.display = "none";
        } catch (error) {
            errorDiv.textContent = "Something went wrong. Please try again later.";
            errorDiv.style.display = "block";
            answerDiv.style.display = "none";
        }
    });
});
