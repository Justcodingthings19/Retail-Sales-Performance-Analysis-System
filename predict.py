import joblib

model = joblib.load(
    "models/sales_model.pkl"
)

quantity = float(
    input("Enter Quantity: ")
)

price = float(
    input("Enter Price: ")
)

prediction = model.predict(
    [[quantity, price]]
)

print(
    "Predicted Sales:",
    prediction[0]
)
