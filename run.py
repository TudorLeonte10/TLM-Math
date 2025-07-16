from app import create_app
print("Initializing the application...")

app = create_app()

if __name__ == "__main__":
    print("Starting the Flask application...")
    app.run(debug=True, host="0.0.0.0", port=5000)
