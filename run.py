from app import create_app
print("Initializing the application...")

app = create_app()

if __name__ == "__main__":
    print("Starting the Flask application...")
    app.run(debug=True, host="127.0.0.1", port=5000)
