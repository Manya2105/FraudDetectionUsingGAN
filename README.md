# SafePayAI

SafePayAI is an advanced fraud detection and prevention application designed to safeguard digital transactions by leveraging cutting-edge artificial intelligence techniques. With its seamless integration of machine learning models and user-friendly interfaces, SafePayAI offers a robust solution for identifying and mitigating fraudulent activities in real-time. By combining the power of Generative Adversarial Networks (GANs) for synthetic data generation and Random Forest classifiers for accurate predictions, SafePayAI ensures unparalleled security and efficiency in transaction monitoring.

---

## Features

### Frontend Features:
- **User Authentication**: Google Sign-In for secure access.
- **Transaction Dashboard**: View transaction history and analyze patterns.
- **Responsive UI**: Built with Tailwind CSS for mobile and desktop compatibility.
- **Animations**: Smooth transitions and interactive elements using Framer Motion.

### Backend Features:
- **AI-Powered Fraud Detection**: Integration of Random Forest and Generative Adversarial Networks (GAN) to detect and prevent fraudulent transactions.
- **Real-Time Analysis**: API provides instant fraud predictions using pre-trained models.
- **Data Augmentation**: GANs generate synthetic datasets to improve model performance and accuracy.
- **Database Integration**: Firebase backend to manage UPI IDs, transaction history, and analytics.

---

## Technologies Used

### Frontend:
- [React](https://reactjs.org/)
- [Vite](https://vitejs.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Framer Motion](https://www.framer.com/motion/)
- [Radix UI](https://www.radix-ui.com/)

### Backend:
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Firebase](https://firebase.google.com/)
- [Generative Adversarial Networks (GAN)](https://en.wikipedia.org/wiki/Generative_adversarial_network)
- [Random Forest](https://scikit-learn.org/stable/modules/ensemble.html#forest)

---

## Installation

### Frontend Setup:
1. Clone the frontend repository:
   ```bash
   git clone https://github.com/yourusername/fraudAI_Frontend_React.git
   ```
2. Navigate to the project directory:
   ```bash
   cd fraudAI_Frontend_React
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Start the development server:
   ```bash
   npm run dev
   ```
5. Open the app in your browser at [http://localhost:3000](http://localhost:3000).

### Backend Setup:
1. Clone the backend repository:
   ```bash
   git clone https://github.com/yourusername/fraudAI_Backend.git
   ```
2. Navigate to the backend directory:
   ```bash
   cd fraudAI_Backend
   ```
3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure the trained model file `best_rf_model.pkl` is present in the directory.
5. Start the Flask server:
   ```bash
   python app.py
   ```
6. The API will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

![AI Model visual Diagram](https://raw.githubusercontent.com/Shabopp/FraudDetectionUsingGAN/main/SystemDesignDiagrams/SystemDesign.png)

## AI Model: Fraud Detection Process

The core of SafePayAI lies in its AI-driven fraud detection mechanism, developed using a combination of GAN and Random Forest models. Here’s an in-depth breakdown:

### Step 1: Data Preparation
- **Load Dataset**: Start with a transactional dataset containing both fraudulent and non-fraudulent records. Ensure it is preprocessed (e.g., handling missing values, scaling, and encoding).
- **Split Data**: Divide into training (80%) and testing (20%) sets.
- **Feature Engineering**: Normalize numerical features and one-hot encode categorical variables.

### Step 2: Train a GAN for Synthetic Data Generation
- **GAN Architecture**:
  - Generator: Creates synthetic transaction data from random noise.
  - Discriminator: Differentiates between real and synthetic data.
- **Training Process**:
  - Alternate between training the discriminator on real and synthetic data and training the generator to fool the discriminator.
  - Use Binary Cross-Entropy (BCE) loss for both.
- **Validation**: Evaluate synthetic data quality through visualization and statistical metrics.

### Step 3: Use Synthetic Data to Augment the Dataset
- **Generate Synthetic Data**: Use the trained GAN to create synthetic transactions for both fraud and non-fraud labels.
- **Merge Data**: Combine synthetic and real data to balance the dataset and reduce class imbalance.

### Step 4: Train the Random Forest Model
- **Dataset Splitting**: Split the augmented dataset into training and validation sets.
- **Training**: Train the Random Forest model using the sklearn library.
- **Hyperparameter Tuning**: Optimize parameters (e.g., n_estimators, max_depth) using cross-validation.
- **Evaluation**: Assess model performance using metrics like accuracy, precision, recall, F1-score, and AUC-ROC.

### Step 5: Fraud Prediction Workflow
- **Input Processing**: Preprocess transaction data received from the frontend.
- **Prediction**: Pass processed data through the trained Random Forest model to classify transactions as `Fraud` or `Not Fraud`.
- **Output**: Display results on the frontend dashboard in real time.

### Step 6: Workflow Automation
- Modularized preprocessing, GAN training, synthetic data generation, and Random Forest training into reusable functions.
- Integrated the workflow into a script for seamless execution.

---
![AI Model visual Diagram](https://raw.githubusercontent.com/Shabopp/FraudDetectionUsingGAN/main/SystemDesignDiagrams/AIMODEL_VISUAL.png)

## Fraud Detection Parameters and Features
1. **Transaction Amount Anomalies**: Detects transactions that significantly deviate from a user's historical average or usual behavior.
2. **Transaction Frequency**: Flags unusual spikes in the number of transactions within a short time period (e.g., multiple transactions in minutes).
3. **Recipient Verification Status**: Checks whether the recipient is verified, registered recently, or flagged as suspicious.
4. **Recipient Blacklist Status**: Identifies transactions to or from blacklisted UPI IDs, accounts, or merchants.
5. **Device Fingerprinting**: Analyzes mismatches in the device ID, browser, or OS used for the transaction compared to prior user sessions.
6. **VPN or Proxy Usage**: Flags transactions originating from masked IP addresses, indicating possible fraud attempts.
7. **Geo-Location Flags**: Identifies if transactions are initiated from unusual or high-risk geolocations.
8. **Behavioral Biometrics**: Monitors user interaction patterns, such as typing speed or mouse movement, for deviations from typical behavior.
9. **Time Since Last Transaction with Recipient**: Evaluates if the recipient is a new contact or there has been a significant time gap since the last transaction.
10. **Social Trust Score**: Scores recipients based on their relationship with the user (e.g., presence in contact list or prior transactions).
11. **Account Age**: Analyzes the age of the user’s account, flagging newly created accounts performing high-risk transactions.
12. **High-Risk Transaction Times**: Flags transactions occurring during non-business hours or at unusual times.
13. **Past Fraudulent Behavior Flags**: Checks if the user or recipient has been flagged for prior fraudulent activity.
14. **Location-Inconsistent Transactions**: Detects transactions initiated from multiple geolocations in a short time frame, indicating compromised credentials.
15. **Normalized Transaction Amount**: Compares the transaction amount against normalized values for similar users or demographic profiles.
16. **Transaction Context Anomalies**: Flags transactions that do not align with the user's typical spending habits (e.g., sudden large purchases).
17. **Fraud Complaints Count**: Analyzes the frequency of fraud complaints linked to a UPI ID, device, or account.
18. **Merchant Category Mismatch**: Checks if the merchant's behavior aligns with their declared category (e.g., high-value transactions for a low-value merchant).
19. **User Daily Limit Exceeded**: Flags transactions that exceed predefined daily transaction limits.
20. **Recent High-Value Transaction Flags**: Detects if the user recently performed a high-value transaction, increasing risk for subsequent fraudulent activity.

---

## API Endpoints

### Base URL: `http://127.0.0.1:5000/`

#### Home
- **GET** `/`
  - Returns a welcome message.

#### Predict
- **POST** `/predict`
  - **Request Body**: JSON object containing features for prediction.
    ```json
    {
      "features": [value1, value2, value3, ...]
    }
    ```
  - **Response**: JSON object containing the prediction.
    ```json
    {
      "prediction": ["Fraud" or "Not Fraud"]
    }
    ```
  - **Error Responses**:
    - 400: No input data provided.
    - 500: Internal server error.

---

## Model Training

Open the Jupyter Notebook `FraudDetectionUsingGAN.ipynb` for training.

### Detailed Steps:
1. **Data Preprocessing**: Prepare the dataset by normalizing and encoding features.
2. **GAN Implementation**: Define and train the generator and discriminator networks.
3. **Synthetic Data Generation**: Create augmented data using the trained GAN.
4. **Random Forest Training**: Train the model using the augmented dataset and save the trained model as `best_rf_model.pkl`.


![Data Flow Diagram](https://raw.githubusercontent.com/Shabopp/FraudDetectionUsingGAN/main/SystemDesignDiagrams/WorkFlowDiagram.png)


