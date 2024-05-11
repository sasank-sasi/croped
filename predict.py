from joblib import load

# Load the saved model and LabelEncoder
model = load('crop_prediction_model.joblib')
le = load('label_encoder.joblib')

# Take user input for the features
temperature = float(input("Enter Temperature (in Celsius): "))
humidity = float(input("Enter Humidity (in %): "))
pH = float(input("Enter pH value: "))
rainfall = float(input("Enter Rainfall (in mm): "))

# Prepare the new data point
new_data = [[temperature, humidity, pH, rainfall]]

# Make the prediction using the loaded model
prediction = model.predict(new_data)

# Transform the prediction back to the original label using the loaded LabelEncoder
predicted_crop = le.inverse_transform(prediction)

# Print the predicted crop
print(f"Predicted Crop: {predicted_crop[0]}")