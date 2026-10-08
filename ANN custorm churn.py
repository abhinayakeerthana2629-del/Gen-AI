# Customer Churn prediction using ANN
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Step 1: Create dataset
np.random.seed(42)
tenure = np.random.randint(1, 60, 1000)
monthly_charges = np.random.uniform(20, 120, 1000)
data_usage = np.random.randint(1, 50, 1000)
support_tickets = np.random.randint(0, 10, 1000)

# Churn rule
churn = ((tenure < 12) & (support_tickets > 3)) | (monthly_charges > 100)
churn = churn.astype(int)

# Create dataframe
df = pd.DataFrame({
    'Tenure': tenure,
    'MonthlyCharges': monthly_charges,
    'DataUsage': data_usage,
    'SupportTickets': support_tickets,
    'Churn': churn
})
print(df.head())

# Step 2: Inputs and outputs
X = df[['Tenure', 'MonthlyCharges', 'DataUsage', 'SupportTickets']]
Y = df['Churn']

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Step 4: Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 5: Build ANN model
model = Sequential([
    Dense(16, activation='relu', input_shape=(4,)),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Step 6: Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Step 7: Model summary
model.summary()

# Step 8: Train model
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=1)

# Step 9: Evaluate
loss, acc = model.evaluate(X_test, y_test)
print('Loss:', loss)
print('Accuracy:', acc)

# Step 10: Predict new customer
new_customer = np.array([[10, 110, 20, 5]])
new_customer_scaled = scaler.transform(new_customer)
prediction = model.predict(new_customer_scaled)
print('\nChurn Probability:', prediction[0][0])
print('Predicted Churn:', 'Yes' if prediction[0][0] > 0.5 else 'No')

# Step 11: Visualize training
plt.figure(figsize=(8, 5))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('ANN Loss Curve')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid()
plt.show()
