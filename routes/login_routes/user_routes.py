from database import text

def get_user(req_body, session_user):
    name = req_body['name']
    print(f"##################################{name}")
    records = session_user.execute(text("SELECT * from profile.client_onboarding_details where first_name = :db_name"),{"db_name": name}).fetchall()
    print(records)
    return {"message": records}