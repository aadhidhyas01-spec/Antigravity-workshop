"""
Flask Web Application for Google Cloud Tech Summit 1-Day Conference.
"""

from flask import Flask, render_template, request, jsonify
from data import CONFERENCE_INFO, CATEGORIES, SPEAKERS, TALKS, get_all_talks, get_talk_by_id, filter_talks

app = Flask(__name__)

@app.route("/")
def index():
    query = request.args.get("q", "").strip()
    category = request.args.get("category", "").strip()
    speaker = request.args.get("speaker", "").strip()
    
    filtered_talks = filter_talks(search_query=query, category_id=category, speaker_name=speaker)
    speakers_list = list(SPEAKERS.values())
    
    return render_template(
        "index.html",
        conf=CONFERENCE_INFO,
        categories=CATEGORIES,
        speakers=speakers_list,
        talks=filtered_talks,
        all_talks_count=len(TALKS),
        active_query=query,
        active_category=category,
        active_speaker=speaker
    )

@app.route("/api/talks")
def api_talks():
    query = request.args.get("q", "").strip()
    category = request.args.get("category", "").strip()
    speaker = request.args.get("speaker", "").strip()
    
    results = filter_talks(search_query=query, category_id=category, speaker_name=speaker)
    return jsonify({
        "status": "success",
        "count": len(results),
        "total": len(TALKS),
        "talks": results
    })

@app.route("/api/talk/<int:talk_id>")
def api_talk_detail(talk_id):
    talk = get_talk_by_id(talk_id)
    if talk:
        return jsonify({"status": "success", "talk": talk})
    return jsonify({"status": "error", "message": "Talk not found"}), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template("index.html", 
        conf=CONFERENCE_INFO, 
        categories=CATEGORIES, 
        speakers=list(SPEAKERS.values()), 
        talks=get_all_talks(),
        all_talks_count=len(TALKS),
        error="Page not found. Redirected to home."
    ), 404

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
