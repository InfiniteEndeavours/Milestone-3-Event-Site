from event_finder import create_flask_app, fake_data, db
import os

app = create_flask_app()

# Run the app if this file is run directly
if __name__ == "__main__":
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()
    #     fake_data()
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG")
            )
