# 🏠 Housing Price Prediction Project

## 📊 Overview:
The **Housing Price Prediction** project utilizes various machine learning models to predict housing prices based on several features of the properties. The project demonstrates how to leverage advanced regression techniques to derive insights from data and make accurate predictions.

## 🔍 Project Highlights:
- **Models Used**: Linear Regression, Ridge Regression, Lasso Regression, Elastic Net, Stochastic Gradient Descent, Random Forest, Support Vector Machines, LightGBM, XGBoost, and K-Nearest Neighbors.
- **Data Source**: The dataset used for this project contains information about housing characteristics in the USA, including features such as area income, house age, and population.
- **User-Friendly Interface**: Built with Streamlit, providing an interactive frontend for users to input property details and receive predicted prices.
- **Link**: **https://house-price-prediction-using-machine-learning-models.streamlit.app/**

## 💻 Features:
- **Model Selection**: Users can choose from multiple regression models to see how predictions vary.
- **Input Fields**: Users can enter key property features, such as:
  - Average Area Income
  - Average Area House Age
  - Average Area Number of Bedrooms
  - Area Population
- **Visualizations**: (Future work) Plans to integrate visualizations to showcase model performance and predictions.

## 📈 Results:
The project evaluates the performance of various regression models using the following metrics:

- **Mean Squared Error (MSE)**: Measures the average squared difference between predicted and actual values. A lower MSE indicates better model performance. For instance, the **Linear Regression** model achieved an MSE of approximately **10,549,721,686**, suggesting reasonable accuracy, whereas the **SGD Regressor** exhibited an exceptionally high MSE of **9.51E+34**, indicating poor performance.

- **Mean Absolute Error (MAE)**: Represents the average absolute difference between predicted and actual values. It provides an intuitive understanding of the prediction errors. The **KNN** model recorded an MAE of **198,086.24**, which highlights significant deviation from actual prices, whereas **Lasso Regression** and **Linear Regression** models showed much lower MAEs around **82,658**, suggesting higher reliability in their predictions.

- **R-squared (R²)**: This statistic measures the proportion of variance in the dependent variable (housing prices) that can be predicted from the independent variables. An R² value closer to **1** indicates a better fit of the model. The **Linear Regression** and **Ridge Regression** models achieved an R² of approximately **0.9146**, indicating that about **91.46%** of the variance in housing prices can be explained by the features used. In contrast, the **SVM** model had an R² value close to **0**, suggesting it was unable to capture the underlying patterns in the data.

### Summary of Model Performance:
- **Top Performers**:
  - **Linear Regression**: MSE: 10,549,721,686 | MAE: 82,657.95 | R²: 0.9146
  - **Ridge Regression**: MSE: 10,549,745,187 | MAE: 82,659.67 | R²: 0.9146
  - **Lasso Regression**: MSE: 10,549,717,660 | MAE: 82,657.95 | R²: 0.9146

- **Underperformers**:
  - **SGD Regressor**: MSE: 9.51E+34 | MAE: 2.49E+17 | R²: -7.70E+23
  - **Support Vector Machine**: MSE: 1.23547E+11 | MAE: 282,947.69 | R²: 0.0004
  - **K-Nearest Neighbors**: MSE: 60,395,811,313 | MAE: 198,086.24 | R²: 0.5114

### Insights:
- The **Linear Regression**, **Ridge**, and **Lasso Regression** models consistently produced similar performance metrics, indicating that linear relationships were effectively captured in the dataset.
- The **Random Forest** and **XGBoost** models, while less effective than linear models, showed potential for improvement through hyperparameter tuning.
- **Underperforming models** such as the **SGD Regressor** and **SVM** need further optimization or might benefit from alternative preprocessing or feature engineering techniques to enhance their predictive capabilities.

These results emphasize the importance of model selection and tuning in achieving reliable predictions. The project lays the groundwork for future improvements, including experimenting with ensemble methods and more complex models to further enhance accuracy.

## 🛠️ Future Improvements:
- **Enhance User Experience**: Improve the UI with additional features and better design.
- **More Models**: Implement and evaluate additional models for better predictions.
- **Feature Engineering**: Explore feature selection and engineering techniques to enhance model performance.

## 🚫 File Size Limitation
Please note that the **RandomForest.pkl** model file is approximately **35MB** in size, which exceeds GitHub's file upload limits for repositories. As a result, it is not included in this repository. You can obtain this file through direct communication or alternative file-sharing methods if needed or you can simply run the model with the dataset to obtain the file.

**Thank You** 🙏
