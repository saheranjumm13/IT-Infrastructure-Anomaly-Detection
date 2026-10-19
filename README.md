
# IT Infrastructure Anomaly Detection System

## 📌 Project Overview

The **IT Infrastructure Anomaly Detection System** is a machine learning project that identifies unusual patterns in IT server performance. It analyzes CPU utilization, memory utilization, network activity, and response time using Python and the Isolation Forest algorithm.

The project also includes a Power BI dashboard for visualizing monitoring results and a Streamlit application with basic Owner and Viewer login roles.

## 🎯 Objectives

- Analyze server performance metrics.
- Clean and preprocess monitoring data.
- Detect potential anomalies using machine learning.
- Visualize server performance and anomaly alerts in Power BI.
- Demonstrate basic login authentication and role-based access in Streamlit.

## 🛠️ Technologies Used

- **Python** — Programming language
- **Pandas and NumPy** — Data processing and numerical operations
- **Scikit-learn** — Isolation Forest anomaly detection
- **Jupyter Notebook** — Model development and experimentation
- **Power BI Desktop** — Interactive data visualization
- **Streamlit** — Login interface and monitoring application
- **bcrypt** — Password hashing
- **JSON and CSV** — Account configuration and data exchange

## ⚙️ Project Workflow

1. Generate or prepare server monitoring data.
2. Clean the data and handle invalid or missing values.
3. Select and prepare CPU, memory, network, and response-time features.
4. Apply the Isolation Forest algorithm.
5. Label records as normal or potential anomalies.
6. Export monitoring results and anomaly alerts to CSV files.
7. Import the CSV files into Power BI to build a dashboard.
8. Run the Streamlit application to demonstrate Owner and Viewer access.

## 📂 Project Structure

```text
IT-Infrastructure-Anomaly-Detection/
├── IT_generated.ipynb
├── app.py
├── create_users.py
├── reset_password.py
├── users.json
├── powerbi-dashboard.png
├── README.md
├── .gitignore
└── output/
    ├── server_monitoring_results.csv
    └── server_anomaly_alerts.csv
```

The Power BI `.pbix` report can also be included if it contains no sensitive information and is reasonably sized.


## 📊 Power BI Dashboard

The dashboard visualizes server performance metrics and highlights
potential anomalies detected by the Isolation Forest model.

![Power BI Dashboard](powerbi-dashboard.png)


## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/IT-Infrastructure-Anomaly-Detection.git
cd IT-Infrastructure-Anomaly-Detection
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Install the required packages

```bash
python -m pip install pandas numpy scikit-learn jupyter streamlit bcrypt
```

### 3. Run the machine learning notebook

```bash
jupyter notebook
```

Open `IT_generated.ipynb` and run the cells in order to prepare the data, execute the model, and export the CSV results.

### 4. Set up user accounts

Run the account creation script:

```bash
python create_users.py
```

Follow the prompts to create the accounts. If an account already exists, use the appropriate password-reset procedure when needed.

### 5. Start the Streamlit application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

### 6. Open the Power BI dashboard

Open the `.pbix` report in Power BI Desktop. If you are setting it up for the first time, import the exported CSV files and create your report visuals.

## 🔐 Login and Access Control

The Streamlit prototype supports two account roles:

- **Owner:** Intended for authorized project management and Owner Controls.
- **Viewer:** Intended for viewing monitoring results and potential anomaly alerts.

Passwords are hashed with bcrypt rather than stored as plain text.

**Security note:** This is an educational prototype. The login interface does not independently protect notebook files, Power BI files, or CSV files. Additional access controls are required for production use.

## 📊 Expected Outputs

- Processed server monitoring dataset
- Anomaly predictions and anomaly scores
- Potential anomaly alerts
- Power BI monitoring dashboard
- Streamlit login and monitoring interface

## ⚠️ Limitations

- The current demonstration uses synthetic data.
- False positives and missed anomalies are possible.
- Real-world detection performance has not been established without verified incident labels.
- Live server monitoring and automatic notifications require additional implementation.
- The login prototype requires stronger protections before production deployment.

## 🔮 Future Enhancements

- Integrate real server logs and monitoring APIs.
- Add real-time anomaly detection.
- Send automated alerts through email or messaging services.
- Evaluate model performance using labelled real-world data.
- Improve authentication, audit logging, and access permissions.
- Automate dashboard data refresh.

## 👩‍💻 Author

**Saheranjum Makandar**

Data Science Student | Machine Learning Enthusiast

GitHub: https://github.com/saheranjumm13

## 📄 Disclaimer

This project is developed for educational and demonstration purposes. An anomaly prediction indicates unusual behavior and does not confirm a server failure.
