from flask import Flask, request, jsonify, abort
import sqlite3, os, datetime
from contextlib import closing

DB_PATH = os.path.join(os.path.dirname(__file__), "notes.sqlite3")

app = Flask(__name__)

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with closing(get_conn()) as conn, conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT DEFAULT '',
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)



# Flask 3: initialize DB at startup
with app.app_context():
    init_db()


@app.route("/ping")
def ping():
    return {"ok": True, "message": "pong"}

@app.route("/notes", methods=["GET"])
def list_notes():
    with closing(get_conn()) as conn:
        cur = conn.execute("SELECT * FROM notes ORDER BY id DESC")
        notes = [dict(row) for row in cur.fetchall()]
        return jsonify(notes)

@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json()
    title = data.get("title", "")
    content = data.get("content", "")
    if not title:
        abort(400, description="Title is required")
    now = datetime.datetime.utcnow().isoformat()
    with closing(get_conn()) as conn, conn:
        conn.execute(
            "INSERT INTO notes (title, content, created_at, updated_at) VALUES (?, ?, ?, ?)",
            (title, content, now, now),
        )
    return {"message": "Note created!"}, 201

if __name__ == "__main__":
    app.run(debug=True)
