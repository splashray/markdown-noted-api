from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models import db, User
from flask import jsonify
from datetime import timedelta


def register_user(data):
    # Check if all required fields are present
    if not data.get('username') or not data.get('password'):
        return {"error": "Username and password are required"}, 400

    # Check if the username already exists
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return {"error": "Username already exists"}, 409

    # Hash the password
    hashed_password = generate_password_hash(data['password'], method='sha256')

    # Create a new User instance
    user = User(
        username=data['username'], 
        password=hashed_password
    )

    # Add the user to the session and commit the transaction
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        # Handle any errors that occur during the database transaction
        db.session.rollback()  # Rollback the transaction if there's an error
        return {"error": "An error occurred while registering the user"}, 500

     # Create a response dictionary excluding the password
    user_response = {
        "id": user.id,
        "username": user.username,
        # Add other fields you want to include in the response
    }

    # Return the response
    return { "user": user_response, "message": "User registered successfully"},201

def login_user(data):
    # Check if all required fields are present
    if not data.get('username') or not data.get('password'):
        return {"error": "Username and password are required"}, 400

    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return {"message": "Invalid credentials"}, 401

    # Modify the expiration time of the access token
    access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=24))
    
    # Create a response dictionary excluding the password
    user_response = {
        "id": user.id,
        "username": user.username,
        "access_token": access_token
        # Add other fields you want to include in the response
    }

    return { "user": user_response, "message": "User logged in successfully" }, 200

    

