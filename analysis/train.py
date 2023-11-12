import pandas as pd
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import LSTM, Dense

# Load the Excel dataset
df = pd.read_excel('excels/train.xlsx')  # Update with your actual file path

# Convert "CODIGO" to categorical using LabelEncoder
label_encoder = LabelEncoder()
df['CODIGO'] = label_encoder.fit_transform(df['CODIGO'])

# Prepare sequences for LSTM
sequence_length = 10  # Adjust as needed
X, y = [], []
for i in range(len(df) - sequence_length):
    X.append(df.iloc[i:i+sequence_length]['CODIGO'].values)
    y.append(df.iloc[i+sequence_length]['CANTIDADCOMPRA'])

X = pd.DataFrame(X)  # Convert to DataFrame
y = pd.Series(y)

# Reshape X to (samples, time steps, features)
X = X.values.reshape(X.shape[0], sequence_length, 1)

# Define the model
model = Sequential()
model.add(LSTM(50, input_shape=(sequence_length, 1)))
model.add(Dense(1))  # Assuming regression, change activation for classification
model.compile(loss='mean_squared_error', optimizer='adam')  # Adjust loss for your task

# Train the model
history = model.fit(X, y, epochs=150, batch_size=32, validation_split=0.2)

# Print the loss on the training set
train_loss = history.history['loss'][-1]
print(f'Training Loss: {train_loss}')

# Print the loss on the validation set (test set in this case)
val_loss = history.history['val_loss'][-1]
print(f'Validation Loss: {val_loss}')
