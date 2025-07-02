from models import SessionLocal, Plan
import streamlit as st

def view_user_plans(username):
    db = SessionLocal()
    plans = db.query(Plan).filter(Plan.user.has(username=username)).all()
    db.close()

    if not plans:
        st.info("You have no saved plans yet.")
        return

    st.markdown("### Your Saved Plans:")
    for plan in plans:
        plan_url = f"?plan_id={plan.id}"
        st.markdown(f" [{plan.subject} ({plan.timeframe})]({plan_url})", unsafe_allow_html=True)
