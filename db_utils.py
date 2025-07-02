from models import SessionLocal, User, Plan
import bcrypt



def create_user(username, password):
    db = SessionLocal()
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user = User(username=username, hashed_password=hashed_pw.decode())
    db.add(user)
    db.commit()
    db.close()

def get_user(username):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    db.close()
    return user

def verify_user(username, password):
    user = get_user(username)
    if user:
        return bcrypt.checkpw(password.encode(), user.hashed_password.encode())
    return False

def save_plan(username, subject, timeframe, content):
    db = SessionLocal()
    user = get_user(username)
    plan = Plan(subject=subject, timeframe=timeframe, content=content, user_id=user.id)
    db.add(plan)
    db.commit()
    db.close()
