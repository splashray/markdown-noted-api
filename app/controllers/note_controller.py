from markdown2 import markdown
from app.models import db, Note

def create_note_for_user(user_id, data):
     # Check if all required fields are present
    if not data.get('title') or not data.get('content'):
        return {"error": "Title and content are required"}, 400

    # Create a Note instance
    note = Note(
        title=data['title'],
        content=data['content'],
        rendered_html=markdown(data['content']),
        user_id=user_id
    )
    
    # Add the note to the session and commit the transaction
    try:
        db.session.add(note)
        db.session.commit()
    except Exception as e:
        # Handle any errors that occur during the database transaction
        db.session.rollback()  # Rollback the transaction if there's an error
        return {"error": "An error occurred while creating the note"}, 500
    
    note_data = note.to_dict()
    return {"message": "Note created successfully", "note": note_data}, 201

def get_notes_for_user(user_id):
    if not user_id:
        return {"error": "User ID is missing"}, 400

    try:
        # Fetch notes for the user
        notes = Note.query.filter_by(user_id=user_id).all()
        if not notes:
            return {"message": "No notes found for this user"}, 404

        # Convert notes to dictionaries
        note_data = [note.to_dict() for note in notes]
        return {"notes": note_data}, 200
    except Exception as e:
        # Log the exception if needed
        print(f"Error retrieving notes: {e}")
        return {"error": "An error occurred while retrieving notes"}, 500


def get_note_for_user(user_id, note_id):
    if not user_id or not note_id:
        return {"error": "User ID and Note ID are required"}, 400

    try:
        # Fetch the note by its ID and ensure it belongs to the given user
        note = Note.query.filter_by(id=note_id, user_id=user_id).first()
        if not note:
            return {"error": "Note not found or does not belong to the user"}, 404

        # Convert the note to a dictionary
        note_data = note.to_dict()
        return {"note": note_data}, 200
    except Exception as e:
        # Log the exception if needed
        print(f"Error retrieving note: {e}")
        return {"error": "An error occurred while retrieving the note"}, 500
    
def update_note_for_user(user_id, note_id, data):
    if not user_id or not note_id:
        return {"error": "User ID and Note ID are required"}, 400

    try:
        # Fetch the note by its ID and ensure it belongs to the given user
        note = Note.query.filter_by(id=note_id, user_id=user_id).first()
        if not note:
            return {"error": "Note not found or does not belong to the user"}, 404

        # Update the note fields
        note.title = data.get('title', note.title)
        note.content = data.get('content', note.content)
        note.rendered_html = markdown(note.content)  # Re-render the HTML from the updated Markdown content

        # Commit the changes to the database
        try:
            db.session.commit()
        except Exception as e:
            # Handle any errors that occur during the database transaction
            db.session.rollback()  # Rollback the transaction if there's an error
            return {"error": "An error occurred while modifying the user"}, 500
        

        return {"message": "Note updated successfully", "note": note.to_dict()}, 200
    except Exception as e:
        # Log the exception if needed
        print(f"Error updating note: {e}")
        return {"error": "An error occurred while modifying the note"}, 500

def delete_note_for_user(user_id, note_id):
    if not user_id or not note_id:
        return {"error": "User ID and Note ID are required"}, 400

    try:
        # Fetch the note by its ID and ensure it belongs to the given user
        note = Note.query.filter_by(id=note_id, user_id=user_id).first()
        if not note:
            return {"error": "Note not found or does not belong to the user"}, 404

        # Delete the note
        db.session.delete(note)
        db.session.commit()

        return {"message": "Note deleted successfully"}, 200
    except Exception as e:
        # Log the exception if needed
        print(f"Error deleting note: {e}")
        return {"error": "An error occurred while deleting the note"}, 500
