document
    .getElementById("predictionForm")
    .addEventListener("submit", async function (e) {

        e.preventDefault();

        const payload = {

            gender: document.getElementById("gender").value,

            SeniorCitizen: Number(
                document.getElementById("SeniorCitizen").value
            ),

            Partner:
                document.getElementById("Partner").value,

            Dependents:
                document.getElementById("Dependents").value,

            tenure: Number(
                document.getElementById("tenure").value
            ),

            PhoneService:
                document.getElementById("PhoneService").value,

            MultipleLines:
                document.getElementById("MultipleLines").value,

            InternetService:
                document.getElementById("InternetService").value,

            OnlineSecurity:
                document.getElementById("OnlineSecurity").value,

            OnlineBackup:
                document.getElementById("OnlineBackup").value,

            DeviceProtection:
                document.getElementById("DeviceProtection").value,

            TechSupport:
                document.getElementById("TechSupport").value,

            StreamingTV:
                document.getElementById("StreamingTV").value,

            StreamingMovies:
                document.getElementById("StreamingMovies").value,

            Contract:
                document.getElementById("Contract").value,

            PaperlessBilling:
                document.getElementById("PaperlessBilling").value,

            PaymentMethod:
                document.getElementById("PaymentMethod").value,

            MonthlyCharges: Number(
                document.getElementById("MonthlyCharges").value
            ),

            TotalCharges: Number(
                document.getElementById("TotalCharges").value
            )
        };

        console.log("Payload Sent:", payload);

        try {

            const response = await fetch(
                "https://churn-prediction-rb7i.onrender.com/predict",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(payload)
                }
            );

            if (!response.ok) {

                const errorText = await response.text();

                document.getElementById("result").innerHTML =
                    `
                    API Error<br>
                    Status: ${response.status}
                    `;

                console.error(errorText);

                return;
            }

            const data = await response.json();

            const predictionText =
                data.prediction === 1
                    ? "Customer Likely To Churn"
                    : "Customer Likely To Stay";

            document.getElementById("result").innerHTML =
                `
                <h3>${predictionText}</h3>

                Probability:
                ${(data.probability * 100).toFixed(2)}%
                `;

        } catch (error) {

            document.getElementById("result").innerHTML =
                "Error connecting to API";

            console.error(error);
        }

    });