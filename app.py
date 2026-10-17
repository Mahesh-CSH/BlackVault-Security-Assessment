from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response

DOCUMENTS = [
    {"id": 1, "title": "Company Overview", "owner": "public"},
    {"id": 2, "title": "Security Policy", "owner": "public"},
    {"id": 3, "title": "BlackVault Internal Audit", "owner": "admin"},
]

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>BlackVault Document Portal</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: #f2f5f9;
            color: #172033;
        }
        header, section {
            background: white;
            padding: 24px;
            margin-bottom: 20px;
            border-radius: 10px;
        }
        h1 { color: #173b68; }
        input, button {
            padding: 10px;
            margin-top: 10px;
        }
        li { margin: 12px 0; }
    </style>
</head>
<body>
    <header>
        <h1>BlackVault</h1>
        <p>Corporate Document Management Portal</p>
    </header>

    <section>
        <h2>Search Documents</h2>
        <form action="/search" method="get">
            <input name="q" placeholder="Enter document title">
            <button type="submit">Search</button>
        </form>
    </section>

    <section>
        <h2>Available Documents</h2>
        <ul>
        {% for doc in documents %}
            <li>
                <strong>{{ doc.title }}</strong>
                — Document ID: {{ doc.id }}
            </li>
        {% endfor %}
        </ul>
    </section>
</body>
</html>
"""

@app.route("/")
def index():
    visible_documents = [
        doc for doc in DOCUMENTS if doc["owner"] == "public"
    ]
    return render_template_string(
        PAGE, documents=visible_documents
    )

@app.route("/search")
def search():
    query = request.args.get("q", "").strip().lower()

    results = [
        doc for doc in DOCUMENTS
        if query in doc["title"].lower()
        and doc["owner"] == "public"
    ]

    return jsonify({
        "query": query,
        "results": results
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/document/<int:doc_id>")
def document_detail(doc_id):
    doc = next(
        (item for item in DOCUMENTS if item["id"] == doc_id),
        None
    )

    if doc is None:
        return jsonify({"error": "Document not found"}), 404

    if doc["owner"] != "public":
        return jsonify({"error": "Access denied"}), 403

    return jsonify({
        "id": doc["id"],
        "title": doc["title"],
        "owner": doc["owner"]
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
