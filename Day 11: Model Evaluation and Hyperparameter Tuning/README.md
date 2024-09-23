# Day 11: Model Evaluation and Hyperparameter Tuning

## Goal:
The goal of this session is to teach students how to evaluate machine learning models using key metrics and optimize models using hyperparameter tuning. By the end of this session, students will understand performance metrics (such as precision, recall, F1-score) and learn how to improve models using techniques like **Grid Search** and **Cross-Validation**.

---

## Topics Covered:

### 1. **Model Evaluation**:
   - **Train-Test Split**: Splitting data into training and test sets.
   - **Confusion Matrix**: Understanding true positives, false positives, true negatives, and false negatives.
   - **Evaluation Metrics**:
     - **Accuracy**: The ratio of correctly predicted instances to the total instances.
     - **Precision**: The ratio of true positive predictions to the total predicted positives.
     - **Recall**: The ratio of true positive predictions to all actual positives.
     - **F1-Score**: The harmonic mean of precision and recall.

### 2. **Cross-Validation**:
   - **Cross-Validation**: Splitting data into multiple folds to evaluate the model more reliably.
   - **K-Fold Cross-Validation**: Using multiple data splits for better model performance estimates.

### 3. **Hyperparameter Tuning**:
   - **Hyperparameters**: Parameters that control the learning process (e.g., the number of trees in a random forest).
   - **Grid Search**: Tuning hyperparameters by testing all possible combinations of a predefined grid.
   - **Random Search**: An alternative approach to hyperparameter tuning by randomly sampling combinations of hyperparameters.

### 4. **Hands-on Activity**:
   - **Optimize a Random Forest Model**: Perform **Grid Search** on a **RandomForestClassifier** to find the best hyperparameters using **GridSearchCV**.

---

## Notebooks:

1. **Part1_Model_Evaluation_and_Metrics.ipynb**:
   - Explains how to evaluate a classification model using metrics like accuracy, precision, recall, and F1-score.
   - Demonstrates the use of the **confusion matrix** for interpreting model predictions.
   - Includes **cross-validation** to assess model performance reliably.

2. **Part2_Hyperparameter_Tuning.ipynb**:
   - Walks through the process of hyperparameter tuning using **GridSearchCV**.
   - Tunes a **RandomForestClassifier** to find the best combination of hyperparameters.
   - Demonstrates how to evaluate the optimized model on a test dataset.

---

## Key Learning Outcomes:

- Understand how to evaluate model performance using key metrics (accuracy, precision, recall, F1-score).
- Learn how to interpret a **confusion matrix** to understand model predictions.
- Use **cross-validation** to estimate model performance more reliably.
- Understand the difference between **hyperparameters** and **model parameters**.
- Perform hyperparameter tuning using **GridSearchCV** to find the best set of hyperparameters for a model.

---

## Resources:

- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Understanding Confusion Matrix and Metrics](https://en.wikipedia.org/wiki/Confusion_matrix)
- [Hyperparameter Tuning Guide](https://scikit-learn.org/stable/modules/grid_search.html)

---

### Activity:

**Optimize a Pre-trained Model**:
- In this activity, you will use **GridSearchCV** to find the optimal hyperparameters for a **RandomForestClassifier**.
- After finding the best hyperparameters, you will evaluate the optimized model and compare its performance before and after hyperparameter tuning.

---

**Important Notes**:
- Make sure you have **scikit-learn** installed in your environment.
- Experiment with different hyperparameters and models (e.g., Logistic Regression, SVM) to see how tuning affects performance.