
import json
import bcrypt
import pandas as pd
import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).parent
USERS_FILE = BASE_DIR / "users.json"
RESULTS_FILE = BASE_DIR / "output" / "server_monitoring_results.csv"
ALERTS_FILE = BASE_DIR / "output" / "server_anomaly_alerts.csv"

st.set_page_config(
    page_title="Secure Anomaly Monitoring",
    page_icon="🔐",
    layout="wide"
)


def load_users():
    if not USERS_FILE.exists():
        return {}

    with open(USERS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def verify_login(username, password):
    users = load_users()
    user = users.get(username)

    if not user:
        return None

    try:
        stored_hash = user["password_hash"].encode("utf-8")
        if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
            if user.get("role") in ("owner", "viewer"):
                return user["role"]
    except (KeyError, ValueError, TypeError):
        return None

    return None


if "username" not in st.session_state:
    st.session_state.username = None

if "role" not in st.session_state:
    st.session_state.role = None


# LOGIN PAGE
if st.session_state.username is None:
    st.title("🔐 Secure Server Monitoring")
    st.write("Sign in with your authorized project account.")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

    if submitted:
        role = verify_login(username.strip(), password)

        if role:
            st.session_state.username = username.strip()
            st.session_state.role = role
            st.rerun()
        else:
            st.error("Invalid username or password.")

    st.stop()


# AUTHENTICATED AREA
st.title("IT Infrastructure Anomaly Detection")
st.write(
    f"Logged in as: {st.session_state.username} "
    f"| Role: {st.session_state.role.upper()}"
)

if st.button("Logout"):
    st.session_state.username = None
    st.session_state.role = None
    st.rerun()


# DASHBOARD VIEW
if RESULTS_FILE.exists():
    df = pd.read_csv(RESULTS_FILE)

    st.subheader("Server Monitoring Results")
    st.metric("Total Records", len(df))

    if "Status" in df.columns:
        anomaly_count = int((df["Status"] == "Anomaly").sum())
        normal_count = int((df["Status"] == "Normal").sum())

        col1, col2 = st.columns(2)
        col1.metric("Anomalies Flagged", anomaly_count)
        col2.metric("Normal Records", normal_count)

    st.dataframe(df, use_container_width=True)

else:
    st.warning(
        "Results CSV not found. Run your ML notebook and export "
        "server_monitoring_results.csv first."
    )


if ALERTS_FILE.exists():
    st.subheader("Potential Anomaly Alerts")
    alerts = pd.read_csv(ALERTS_FILE)
    st.dataframe(alerts, use_container_width=True)


# OWNER-ONLY AREA
if st.session_state.role == "owner":
    st.divider()
    st.subheader("🔒 Owner Controls")
    st.success("Owner role verified.")

    st.write("This section is reserved for authorized project management.")
    st.write(
        "Only add protected operations here after implementing "
        "server-side permission checks."
    )

else:
    st.info(
        "Viewer access: you can view the available monitoring results. "
        "Owner controls are not available to your account."
    )
