# -*- coding: utf-8 -*-
"""NBA SHOT PREDICTION Logistic Regression N Neural Network.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1P_IgAo6wj1CUtGqHNJlM-nhqh9R2NeHT
"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.regularizers import l2

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

from google.colab import drive
drive.mount('/content/drive')

nba = pd.read_csv("/content/drive/MyDrive/Projects/shot_logs.csv")
df = nba.copy()
df.head()

df.info()

df.SHOT_CLOCK = df.SHOT_CLOCK.fillna(df.SHOT_CLOCK.mean())

len(df.TOUCH_TIME[df.TOUCH_TIME<0])

df.TOUCH_TIME[df.TOUCH_TIME<0] = df.TOUCH_TIME.mean()

len(df.TOUCH_TIME[df.TOUCH_TIME<0])

len(df.TOUCH_TIME[df.TOUCH_TIME>24.0])

df.TOUCH_TIME[df.TOUCH_TIME>24.0] = 24

df.LOCATION = df.LOCATION.map({"H":1,"A":0})
df.W = df.W.map({"W":1,"L":0})
df.PTS_TYPE = df.PTS_TYPE.map({2:0,3:1})
df.SHOT_RESULT = df.SHOT_RESULT.map({"made":1,"missed":0})

df = df.rename(columns={"LOCATION":"HOME_AWAY","PTS_TYPE":"3PTS_SHOT","player_name":"PLAYER_NAME","player_id":"PLAYER_ID"})

df.GAME_CLOCK = df.GAME_CLOCK.apply(lambda x: int(x.split(":")[0])*60 + int(x.split(":")[1]))

df = df.drop(columns=["GAME_ID",
                          "MATCHUP",
                          "W",
                          "PLAYER_NAME",
                          "SHOT_NUMBER",
                          "CLOSEST_DEFENDER",
                          "CLOSEST_DEFENDER_PLAYER_ID",
                          "FGM",
                          "PTS",
                          "PLAYER_ID"], axis=1)

X1 = df[["HOME_AWAY",	"FINAL_MARGIN",	"PERIOD",	"GAME_CLOCK",	"SHOT_CLOCK",	"DRIBBLES",	"TOUCH_TIME",	"SHOT_DIST", "3PTS_SHOT",	"CLOSE_DEF_DIST"]]
Y1 = df['SHOT_RESULT']

X1_Train, X1_Test, Y1_Train, Y1_Test = train_test_split(X1, Y1, test_size=0.2)

scaler = StandardScaler()
X1_Train_scaled = scaler.fit_transform(X1_Train)
X1_Test_scaled = scaler.transform(X1_Test)

# LOGISTIC REGRESSION WITHOUT REGULARIZATION ON ALL FEATURES

# Commented out IPython magic to ensure Python compatibility.
# %%time
# Log_Reg1 = LogisticRegression()
# Log_Reg1.fit(X1_Train_scaled, Y1_Train)

Y1_Pred = Log_Reg1.predict(X1_Test_scaled)

Accuracy = accuracy_score(Y1_Test, Y1_Pred)
Confusion_Matrix = confusion_matrix(Y1_Test, Y1_Pred)
Classification_Report = classification_report(Y1_Test, Y1_Pred)

print(f'Accuracy: {Accuracy}')
print('Confusion Matrix:')
print(Confusion_Matrix)
print('Classification Report:')
print(Classification_Report)

# LOGISTIC REGRESSION WITHOUT REGULARIZATION ON TOP 5 FEATURES OF XGBOOST PLOT IMPORTANCE

X2 = df[["FINAL_MARGIN",	"SHOT_CLOCK",	"TOUCH_TIME",	"SHOT_DIST",	"CLOSE_DEF_DIST"]]
Y2 = df['SHOT_RESULT']

X2_Train, X2_Test, Y2_Train, Y2_Test = train_test_split(X2, Y2, test_size=0.2)

scaler = StandardScaler()
X2_Train_scaled = scaler.fit_transform(X2_Train)
X2_Test_scaled = scaler.transform(X2_Test)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# Log_Reg2 = LogisticRegression()
# Log_Reg2.fit(X2_Train_scaled, Y2_Train)

Y2_Pred = Log_Reg2.predict(X2_Test_scaled)

Accuracy = accuracy_score(Y2_Test, Y2_Pred)
Confusion_Matrix = confusion_matrix(Y2_Test, Y2_Pred)
Classification_Report = classification_report(Y2_Test, Y2_Pred)

print(f'Accuracy: {Accuracy}')
print('Confusion Matrix:')
print(Confusion_Matrix)
print('Classification Report:')
print(Classification_Report)

# LOGISTIC REGRESSION WITH L2 REGULARIZATION ON ALL FEATURES

# Commented out IPython magic to ensure Python compatibility.
# %%time
# Log_Reg1L2 = LogisticRegression(penalty='l2')
# Log_Reg1L2.fit(X1_Train_scaled, Y1_Train)

Y1L2_Pred = Log_Reg1L2.predict(X1_Test_scaled)

Accuracy = accuracy_score(Y1_Test, Y1L2_Pred)
Confusion_Matrix = confusion_matrix(Y1_Test, Y1L2_Pred)
Classification_Report = classification_report(Y1_Test, Y1L2_Pred)

print(f'Accuracy: {Accuracy}')
print('Confusion Matrix:')
print(Confusion_Matrix)
print('Classification Report:')
print(Classification_Report)

# LOGISTIC REGRESSION WITH L2 REGULARIZATION ON TOP 5 FEATURES OF XGBOOST PLOT IMPORTANCE

# Commented out IPython magic to ensure Python compatibility.
# %%time
# Log_Reg2L2 = LogisticRegression(penalty='l2')
# Log_Reg2L2.fit(X2_Train_scaled, Y1_Train)

Y2L2_Pred = Log_Reg2L2.predict(X2_Test_scaled)

Accuracy = accuracy_score(Y2_Test, Y2L2_Pred)
Confusion_Matrix = confusion_matrix(Y2_Test, Y2L2_Pred)
Classification_Report = classification_report(Y2_Test, Y2L2_Pred, zero_division=1)

print(f'Accuracy: {Accuracy}')
print('Confusion Matrix:')
print(Confusion_Matrix)
print('Classification Report:')
print(Classification_Report)

# NEURAL NETWORK AHEAD

# NEURAL NETWORK WITHOUT REGULARIZATION

model1 = Sequential()
model1.add(Dense(64, input_dim=X1_Train_scaled.shape[1], activation='relu'))
model1.add(Dense(32, activation='relu'))
model1.add(Dense(32, activation='relu'))
model1.add(Dense(1, activation='sigmoid'))

model1.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Commented out IPython magic to ensure Python compatibility.
# %%time
# nn1 = model1.fit(X1_Train_scaled, Y1_Train, epochs=10, batch_size=64, validation_split=0.2)

Y1_Pred_prob = model1.predict(X1_Test_scaled)

Y1_Pred_classes = (Y1_Pred_prob > 0.5).astype(int)

Accuracy = accuracy_score(Y1_Test, Y1_Pred_classes)
Confusion_Matrix = confusion_matrix(Y1_Test, Y1_Pred_classes)
Classification_Report = classification_report(Y1_Test, Y1_Pred_classes, zero_division=1)

print(f'Accuracy: {Accuracy}')
print('Confusion Matrix:')
print(Confusion_Matrix)
print('Classification Report:')
print(Classification_Report)

plt.plot(nn1.history['accuracy'], label='Training Accuracy')
plt.plot(nn1.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# NN WITH L2 REGULARIZATION

model2 = Sequential()
model2.add(Dense(64, input_dim=X1_Train_scaled.shape[1], activation='relu', kernel_regularizer=l2(0.01)))
model2.add(Dense(32, activation='relu', kernel_regularizer=l2(0.01)))
model2.add(Dense(32, activation='relu', kernel_regularizer=l2(0.01)))
model2.add(Dense(1, activation='sigmoid'))  # Output layer

model2.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Commented out IPython magic to ensure Python compatibility.
# %%time
# nn2 = model2.fit(X1_Train_scaled, Y1_Train, epochs=10, batch_size=64, validation_split=0.2)

Y1_Pred_prob = model2.predict(X1_Test_scaled)

Y1_Pred_classes = (Y1_Pred_prob > 0.5).astype(int)

Accuracy = accuracy_score(Y1_Test, Y1_Pred_classes)
Confusion_Matrix = confusion_matrix(Y1_Test, Y1_Pred_classes)
Classification_Report = classification_report(Y1_Test, Y1_Pred_classes, zero_division=1)

print(f'Accuracy: {Accuracy}')
print('Confusion Matrix:')
print(Confusion_Matrix)
print('Classification Report:')
print(Classification_Report)

plt.plot(nn2.history['accuracy'], label='Training Accuracy')
plt.plot(nn2.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# NN WITH DROPOUT REGULARIZATION

model3 = Sequential()
model3.add(Dense(64, input_dim=X1_Train_scaled.shape[1], activation='relu'))
model3.add(Dropout(0.2))

model3.add(Dense(32, activation='relu'))
model3.add(Dropout(0.2))

model3.add(Dense(32, activation='relu'))
model3.add(Dropout(0.2))

model3.add(Dense(1, activation='sigmoid'))

model3.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Commented out IPython magic to ensure Python compatibility.
# %%time
# nn3 = model3.fit(X1_Train_scaled, Y1_Train, epochs=10, batch_size=64, validation_split=0.2)

Y1_Pred_prob = model3.predict(X1_Test_scaled)

Y1_Pred_classes = (Y1_Pred_prob > 0.5).astype(int)

Accuracy = accuracy_score(Y1_Test, Y1_Pred_classes)
Confusion_Matrix = confusion_matrix(Y1_Test, Y1_Pred_classes)
Classification_Report = classification_report(Y1_Test, Y1_Pred_classes, zero_division=1)

print(f'Accuracy: {Accuracy}')
print('Confusion Matrix:')
print(Confusion_Matrix)
print('Classification Report:')
print(Classification_Report)

plt.plot(nn3.history['accuracy'], label='Training Accuracy')
plt.plot(nn3.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()