# Flask Notes API

Tiny REST API with Flask + SQLite.


A simple REST API built ""Flask"" and ""SQLite""", made for learning backend development.

It allows to create, read, update and delete notes using HTTP requests.

## Features

* Health check endpoint ('/ping')
* Create, list, update and delete notes.
* Stores data locally using ""SQLite""
* Built with ""Flask 3""
* Simple and clean structure - perfect for beginners

--------------------------------------------


## How it works

When you run the app, Flask starts a local server on  
[`http://127.0.0.1:5000`](http://127.0.0.1:5000).

The app exposes several **API endpoints**:

| Method | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/ping` | Health check |
| `GET` | `/notes` | List all notes |
| `POST` | `/notes` | Create a new note |
| `PUT` | `/notes/<id>` | Update a note |
| `DELETE` | `/notes/<id>` | Delete a note |

Each note has:
- `id` — unique identifier  
- `title` — note title (required)  
- `content` — optional text content  
- `created_at` — timestamp  
- `updated_at` — timestamp  

------------------------------------------


## Installation

1.Clone this repository:

'''bash 
git clone git@github.com:Killo0077/flask-notes-api.git
cd flask-notes-api

------------------------------------------------

2. Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies:

pip install flask

4. Run the app

flask --app app run --debug

##### Open your browser at: #######

http://127.0.0.1:5000/ping




--------------------------------------------------

### Example requestL ####


1. Create a note: 

curl -X POST http://127.0.0.1:5000/notes \
  -H "Content-Type: application/json" \
  -d '{"title":"My first note","content":"Hello Flask!"}'


2. List notes:

curl http://127.0.0.1:5000/notes

3. Database

sudo apt install sqlitebrowser


#### Author #####

Made by @Killo0077 while learning Flask and backend fundamentals.