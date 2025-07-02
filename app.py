import streamlit as st
from getChatResponse import get_chat_response
from dotenv import load_dotenv
from parse_json import display_learning_plan
from db_utils import save_plan
from plans import view_user_plans
from auth_ui import login_ui
from sqlalchemy.orm import joinedload
from models import SessionLocal, Plan

load_dotenv()

if not login_ui():
    st.stop()

query_params = st.query_params
plan_id = query_params.get("plan_id", [None])[0]

if plan_id:
    db = SessionLocal()
    plan = db.query(Plan).options(joinedload(Plan.user)).filter(Plan.id == int(plan_id)).first()
    db.close()

    if plan and plan.user.username == st.session_state.get("username"):
        st.title(f"📘 {plan.subject} ({plan.timeframe})")
        st.markdown(plan.content)
        st.markdown("[← Back to Home](/)", unsafe_allow_html=True)
        st.stop()
    else:
        st.error("❌ Plan not found or access denied.")
        st.stop()
        
st.title("Prompt to Course: Learn Skills Your Own Way")

subject = st.text_input("Enter your subject (e.g., Java, Python, AI, etc.)")
timeframe = st.text_input("Enter your time frame (e.g., 4 weeks, 3 months)")

def show_plan():
    if not subject or not timeframe:
        st.warning("Please enter both subject and timeframe.")
        return

    with st.spinner("Generating your personalized learning plan..."):
        try:
            res = get_chat_response(subject, timeframe)
            response_text = res.content if hasattr(res, "content") else str(res)

            # Save the plan in session so it persists after rerun
            st.session_state["last_plan"] = response_text
            st.session_state["last_subject"] = subject
            st.session_state["last_timeframe"] = timeframe

            display_learning_plan(response_text)
        except Exception as e:
            st.error(f"Error: {e}")



# After generating the plan
    if st.session_state.get("logged_in"):
        if st.button("Save Plan"):
            save_plan(st.session_state.username, subject, timeframe, response_text)
            st.success("Plan saved to your account.")
    else:
        st.info("Login to save your plan.")


st.button(label="Get Study Plan", on_click=show_plan)
if "last_plan" in st.session_state:
    st.markdown("### Previously Generated Plan:")
    display_learning_plan(st.session_state["last_plan"])

    if st.session_state.get("logged_in"):
        if st.button("Save Plan"):
            save_plan(
                st.session_state["username"],
                st.session_state.get("last_subject", ""),
                st.session_state.get("last_timeframe", ""),
                st.session_state["last_plan"]
            )
            st.success("✅ Plan saved to your account.")

if st.session_state.get("logged_in"):
    with st.sidebar:
        st.subheader("Your Account")
        st.success(f"Welcome, {st.session_state.username}!")

        if st.checkbox("Show My Saved Plans"):
            st.subheader("Saved Study Plans")
            view_user_plans(st.session_state.username)

        if st.button(" Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.rerun()

