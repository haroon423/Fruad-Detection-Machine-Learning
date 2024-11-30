def test_fraud_model():
    from src.model import train_model
    accuracy = train_model()
    assert accuracy > 0.8  # Pass if model accuracy is above 80%
