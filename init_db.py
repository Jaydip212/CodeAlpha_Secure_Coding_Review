from login import app, db, User, bcrypt

with app.app_context():
    db.create_all()
    # Create a test user
    hashed_password = bcrypt.hashpw(b"testpassword", bcrypt.gensalt())
    user = User(username="testuser", password_hash=hashed_password)
    db.session.add(user)
    db.session.commit()
    print("Database initialized!")