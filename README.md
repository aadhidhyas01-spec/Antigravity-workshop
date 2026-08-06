# Google Cloud Tech Summit 2026 - 1-Day Technical Conference Web Application

A modern, high-performance 1-day technical conference website for **Google Cloud Tech Summit 2026**. Built with **Python and Flask** on the server side, with a responsive front-end featuring Glassmorphism UI, real-time multi-criteria search, category tab filtering, 1-day timetable schedule view, speaker directory, modal session previews, and a 60-minute lunch break.

---

## Features Summary

1. **Home Page**: Displays event date, location (Moscone Center West & Virtual), schedule, and live timetable.
2. **8 Technical Talks**: 8 curated sessions covering Vertex AI, Cloud Run v2, BigQuery, Mandiant Zero-Trust Security, Cloud TPUs, Cloud Spanner & GKE, Terraform, and Vector Search.
3. **1 or 2 Max Speakers per Talk**: Every talk has 1 or 2 featured speakers with avatar cards.
4. **Complete Talk Data Schema**:
   - `ID` (e.g. Session #01 - #08)
   - `Title`
   - `Speakers` (List of speaker objects)
   - `Category` (1: *AI & Machine Learning*, 2: *Cloud Infrastructure & Security*)
   - `Description`
   - `Time Slot` (e.g., 09:00 AM - 09:45 AM)
5. **Detailed Speaker Schema**:
   - `First Name`
   - `Last Name`
   - `LinkedIn URL` (direct link badge)
   - Role / Title & Company bio
6. **Search & Filter Capabilities**:
   - Instant live search bar by Title, Speaker Name, Description, or Topic.
   - Category filter tabs (*All*, *AI & Machine Learning*, *Cloud Infrastructure & Security*).
   - Speaker filter dropdown list.
7. **60-Minute Lunch Break**: Dedicated networking & catering lunch break scheduled from 12:15 PM to 01:15 PM.
8. **View Toggles**: Switch between **Timeline Timetable View** and **Grid Cards View**.
9. **Interactive Modal Dialogs**: Click any session card to reveal deep-dive abstracts and full speaker bios with direct LinkedIn links.

---

## Directory Structure

```
d:/project/New folder/
├── app.py                  # Main Flask web server & API routes
├── data.py                 # Conference schedule, talk data, speakers, and filter helpers
├── requirements.txt        # Python dependencies (Flask >= 2.0.0)
├── static/
│   ├── css/
│   │   └── style.css       # Google Cloud theme design tokens, glassmorphism, responsive rules
│   └── js/
│       └── main.js         # Client-side instant search, tab filters, modal popups, view toggle
├── templates/
│   └── index.html          # Main HTML5 page with Jinja2 template engine
├── tests/
│   └── test_app.py         # Pytest / Unittest suite for routes, schemas, and search logic
└── README.md               # Setup, running, testing & modification guide
```

---

## Setup & Quick Start Guide

### Prerequisites
- **Python 3.8+** installed on your system.

### 1. Installation
Clone or navigate to the project directory and install the required dependencies:

```bash
cd "d:\project\New folder"
pip install -r requirements.txt
```

### 2. Running the Web Application
Start the Flask development server:

```bash
python app.py
```

The application will launch locally at:
👉 **`http://127.0.0.1:5000`**

---

## Running Automated Tests

To run the complete test suite verifying all 12 test specifications (talk counts, speaker rules, schema attributes, lunch break length, and search filters):

```bash
python -m unittest tests/test_app.py
```

Expected output:
```text
Ran 12 tests in 0.060s
OK
```

---

## How to Make Further Changes

### 1. Adding or Modifying Talks
Open `data.py` and modify or append objects to the `TALKS` list:

```python
{
    "id": 9,
    "title": "Your New Session Title",
    "category_id": 1, # 1 for AI & ML, 2 for Cloud Infra
    "category_name": "AI & Machine Learning",
    "time_slot": "04:35 PM - 05:20 PM",
    "description": "Session abstract description...",
    "speakers": [SPEAKERS["s1"]]
}
```

### 2. Adding Speakers
In `data.py`, add new entries to the `SPEAKERS` dictionary:

```python
"s11": {
    "id": "s11",
    "first_name": "Jane",
    "last_name": "Doe",
    "role": "Senior Cloud Architect",
    "company": "Google Cloud",
    "linkedin": "https://www.linkedin.com/in/janedoe",
    "avatar_bg": "linear-gradient(135deg, #4285F4, #91B4FB)",
    "bio": "Bio description here..."
}
```

### 3. Modifying Styling & Aesthetics
Theme colors and design tokens can be customized in `static/css/style.css` under the `:root` pseudo-class:

```css
:root {
    --g-blue: #4285F4;
    --g-red: #EA4335;
    --g-yellow: #FBBC04;
    --g-green: #34A853;
    --bg-dark: #090D16;
}
```

### 4. REST API Integration
The server provides two JSON API endpoints out of the box:
- `GET /api/talks?q={query}&category={cat_id}&speaker={name}` - Filtered sessions list.
- `GET /api/talk/<int:talk_id>` - Specific session payload with speaker details.
