# BasketBall-Shot-Prediction
The objective of this machine learning project is to develop a prediction model for NBA shot selection. This involves the identification of key features and variables that significantly influence shooting performance.<br>
[Link for Logistic_Regression and Neural Network Model](https://github.com/pradeep0875/BasketBall-Shot-Prediction/blob/main/NBA_SHOT_PREDICTION_Logistic_Regression_N_Neural_Network.ipynb)<br>
[Link for Random_Forest and XG_Boost Model](https://github.com/pradeep0875/BasketBall-Shot-Prediction/blob/main/NBA_Shot_Prediction_RANDOM_FOREST_N_XGBOOST.ipynb)<br>
[Link for Pycaret](https://github.com/pradeep0875/BasketBall-Shot-Prediction/blob/main/NBA_SHOT_PREDICTION_ML_PYCARET.ipynb)<br>
## DATA SOURCE
Dataset contains shots taken during the 2014-2015 season. Dataset isscraped from NBA's REST API.<br>
[Link for the dataset](https://www.kaggle.com/dansbecker/nba-shot-logs)<br>
Our dataset initially had 21 features out of which few were shortlisted based on their importance for prediction. It consists of approx. 128K observations.
## Models used for making predictions
There is a long list of methods that can be used to predict accuracy of the shots attempted by a player that includes Logistic regression, SVM, Neural Network, Random Forest, XGBoost,
Naive Bayes, etc.<br>
In our project, we have used 4 models to conduct a comparative study, aiming to analyze differences in accuracy. Models that we have used are:<br>
XGBoost<br>
Random Forest<br>
Logistic Regression<br>
Neural Network<br>
Models were assessed by accuracy, processing time, confusion matrix.<br>
## CONCLUSION
XGBoost: Accuracy - 0.62, Faster processing<br>
Random Forest: Accuracy - 0.61<br>
Logistic Regression (L2): Accuracy - 0.60, Efficient (0.363s)<br>
Neural Network (Dropout): Accuracy - 0.62, Longer processing (70s)<br>
Model Selection with PyCaret: Gradient Boosting Classifier: Accuracy - 0.62, Processing 10.90s<br>
These findings underscore the trade-offs between accuracy and computational efficiency in selecting the most suitable model for deployment. Considering the challenges associated with analyzing behavioral data and the limited features available, achieving an accuracy of around 60% is commendable.
