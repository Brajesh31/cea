import streamlit as st
import pandas as pd
import numpy as np

def generate_synthetic_data():
    # Generate synthetic data
    np.random.seed(42)
    n_samples = 100
    n_features = 4
    X = np.random.randn(n_samples, n_features)
    y = np.random.randint(0, 3, n_samples)  # Three classes
    df = pd.DataFrame(X, columns=[f"Feature_{i+1}" for i in range(n_features)])
    df['target'] = y
    return df

def train_model(df):
    X = df.drop(columns=['target'])
    y = df['target']
    # Dummy model for demonstration
    class_counts = y.value_counts().to_dict()
    most_common_class = max(class_counts, key=class_counts.get)
    return most_common_class

def evaluate_model(df, most_common_class):
    y_true = df['target']
    y_pred = np.full_like(y_true, most_common_class)
    accuracy = np.mean(y_true == y_pred)
    return accuracy, y_pred

def main():
    st.title("Dummy Classifier")
    st.write("This app demonstrates a dummy classifier using synthetic data.")

    # Generate synthetic data
    df = generate_synthetic_data()

    # Display dataset
    st.subheader("Synthetic Dataset")
    st.write(df)

    # Train model
    most_common_class = train_model(df)

    # Display most common class
    st.subheader("Most Common Class")
    st.write("The most common class in the dataset is:", most_common_class)

    # Evaluate model
    accuracy, y_pred = evaluate_model(df, most_common_class)
    st.subheader("Model Evaluation")
    st.write("Accuracy:", accuracy)

    # Display predicted values
    st.subheader("Predicted Values")
    st.write("Predicted values:", y_pred)

if __name__ == "__main__":
    main()
