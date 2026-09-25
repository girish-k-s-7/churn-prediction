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