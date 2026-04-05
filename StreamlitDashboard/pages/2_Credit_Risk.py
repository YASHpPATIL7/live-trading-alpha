import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import (confusion_matrix, classification_report,
    roc_auc_score, roc_curve, precision_recall_curve, average_precision_score)
from sklearn.utils import resample
import plotly.graph_objects as go
import os

st.set_page_config(page_title="P2: Credit Risk", page_icon="🏦", layout="wide")
st.title("🏦 Project 2 — Logistic Regression: Loan Default Prediction")

st.markdown("""
Binary classification on Kaggle's **Give Me Some Credit** dataset.
Predict whether a borrower will default within 2 years.
""")

# Check for data file — works both locally and in Docker
DATA_PATHS = [
    os.path.join(os.path.dirname(__file__), "..", "data", "cs-training.csv"),       # Docker / dashboard local
    os.path.join(os.path.dirname(__file__), "..", "..", "LogisticRegression", "cs-training.csv"),  # repo root
]
DATA_PATH = None
for p in DATA_PATHS:
    if os.path.exists(p):
        DATA_PATH = p
        break

if DATA_PATH is None:
    st.warning("⚠️ Dataset not found. Please ensure `cs-training.csv` exists in `data/` or `LogisticRegression/`.")
    st.stop()

if st.sidebar.button("🚀 Run Model", type="primary"):
    with st.spinner("Training Logistic Regression..."):
        # Load data
        df = pd.read_csv(DATA_PATH, index_col=0)
        df = df.rename(columns={
            "SeriousDlqin2yrs": "Target",
            "RevolvingUtilizationOfUnsecuredLines": "Revolving_util",
            "age": "Age",
            "NumberOfTime30-59DaysPastDueNotWorse": "Late_30_59",
            "DebtRatio": "DTI",
            "MonthlyIncome": "Monthly_income",
            "NumberOfOpenCreditLinesAndLoans": "Open_credit_lines",
            "NumberOfTimes90DaysLate": "Late_90",
            "NumberRealEstateLoansOrLines": "RE_loans",
            "NumberOfTime60-89DaysPastDueNotWorse": "Late_60_89",
            "NumberOfDependents": "Dependents"
        })

        features = ["DTI", "Age", "Late_30_59", "Late_60_89", "Late_90",
                     "Revolving_util", "Monthly_income", "Open_credit_lines"]
        df = df[features + ["Target"]].copy()
        for col in ["Revolving_util", "DTI", "Monthly_income"]:
            df[col] = df[col].clip(upper=df[col].quantile(0.99))
        df.dropna(inplace=True)

        # Balance classes
        df_maj = df[df["Target"] == 0]
        df_min = df[df["Target"] == 1]
        df_min_up = resample(df_min, replace=True, n_samples=len(df_maj)//3, random_state=42)
        df_bal = pd.concat([df_maj, df_min_up]).sample(frac=1, random_state=42).reset_index(drop=True)

        X = df_bal[features].values
        y = df_bal["Target"].values
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y)
        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)
        X_test_s  = scaler.transform(X_test)

        lr = LogisticRegression(C=1.0, max_iter=1000, class_weight="balanced", random_state=42)
        lr.fit(X_train_s, y_train)
        y_pred = lr.predict(X_test_s)
        y_prob = lr.predict_proba(X_test_s)[:, 1]
        auc = roc_auc_score(y_test, y_prob)
        avg_prec = average_precision_score(y_test, y_prob)
        cm = confusion_matrix(y_test, y_pred)
        tn, fp, fn, tp = cm.ravel()

        # --- Metrics ---
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("AUC-ROC", f"{auc:.4f}")
        col2.metric("Avg Precision", f"{avg_prec:.4f}")
        col3.metric("Defaults Caught (TP)", tp)
        col4.metric("Missed Defaults (FN)", fn)

        # --- Charts ---
        tab1, tab2, tab3, tab4 = st.tabs(["🔲 Confusion Matrix", "📈 ROC Curve", "📊 PR Curve", "📉 Coefficients"])

        with tab1:
            fig1 = go.Figure(data=go.Heatmap(
                z=cm, x=["Pred: No Default", "Pred: Default"],
                y=["Actual: No Default", "Actual: Default"],
                colorscale="Blues", text=cm, texttemplate="%{text}", textfont=dict(size=18)
            ))
            fig1.update_layout(title="Confusion Matrix", height=400)
            st.plotly_chart(fig1, use_container_width=True)

        with tab2:
            fpr, tpr, _ = roc_curve(y_test, y_prob)
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(x=fpr, y=tpr, name=f"AUC={auc:.4f}",
                fill="tozeroy", fillcolor="rgba(31,119,180,0.1)"))
            fig2.add_trace(go.Scatter(x=[0,1], y=[0,1], name="Random",
                line=dict(color="red", dash="dash")))
            fig2.update_layout(title="ROC Curve", height=500, xaxis_title="FPR", yaxis_title="TPR")
            st.plotly_chart(fig2, use_container_width=True)

        with tab3:
            prec, rec, _ = precision_recall_curve(y_test, y_prob)
            baseline = float(y_test.sum()) / len(y_test)
            fig3 = go.Figure()
            fig3.add_trace(go.Scatter(x=rec, y=prec, name=f"AP={avg_prec:.4f}",
                fill="tozeroy", fillcolor="rgba(44,160,44,0.1)"))
            fig3.add_trace(go.Scatter(x=[0,1], y=[baseline,baseline], name="Baseline",
                line=dict(color="red", dash="dash")))
            fig3.update_layout(title="Precision-Recall Curve", height=500,
                xaxis_title="Recall", yaxis_title="Precision")
            st.plotly_chart(fig3, use_container_width=True)

        with tab4:
            coef_df = pd.DataFrame({"Feature": features, "Coefficient": lr.coef_[0]})
            coef_df = coef_df.sort_values("Coefficient")
            colors = ["#d62728" if c > 0 else "#1f77b4" for c in coef_df["Coefficient"]]
            fig4 = go.Figure(go.Bar(x=coef_df["Coefficient"], y=coef_df["Feature"],
                orientation="h", marker_color=colors))
            fig4.update_layout(title="Feature Coefficients (red = raises default risk)", height=400)
            st.plotly_chart(fig4, use_container_width=True)
else:
    st.info("👈 Click **Run Model** in the sidebar to start.")
