from app import create_app
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create an instance of the Flask application
app = create_app()

if __name__ == "__main__":
    # Retrieve the port and host from environment variables
    port = int(os.getenv("FLASK_RUN_PORT", 5000))
    host = os.getenv("FLASK_RUN_HOST", "127.0.0.1")
    
    # Run the application
    app.run(debug=True, host=host, port=port)
