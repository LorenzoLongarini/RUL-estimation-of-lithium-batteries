import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

#define LSTM model
def model_LSTM(X_train, 
               units = 128, 
               return_sequences = True):
    model = Sequential()
    model.add(LSTM(units=units, 
                   return_sequences=return_sequences, 
                   input_shape=(X_train.shape[1], X_train.shape[2])))

    model.add(Dense(units=1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


#function to train LSTM
def train_LSTM(X_train, 
               y_train, 
               epochs = 100, 
               batch_size=1, 
               verbose=2):
    model = model_LSTM(X_train=X_train)
    history = model.fit(X_train, 
              y_train, 
              epochs=epochs, 
              batch_size=batch_size, 
              verbose=verbose)
    return history.history['loss']