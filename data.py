"""
Conference Data Module for Google Cloud Tech Summit 2026.
Contains schedule, talk details, speaker profiles, and category definitions.
"""

from datetime import datetime, date

CONFERENCE_INFO = {
    "title": "Google Cloud Tech Summit 2026",
    "subtitle": "Building the Future of Enterprise AI & Cloud Infrastructure",
    "date_str": "Thursday, October 15, 2026",
    "current_date": date.today().strftime("%B %d, %Y"), # e.g., August 05, 2026
    "location": "Moscone Center West, San Francisco & Online Virtual Stream",
    "timezone": "PST (UTC-8)",
    "lunch_break": {
        "title": "Networking & Catering Lunch Break",
        "description": "60-minute complimentary buffet lunch, developer lounge networking, and interactive sponsor booths.",
        "start_time": "12:15 PM",
        "end_time": "01:15 PM",
        "duration_minutes": 60
    }
}

CATEGORIES = [
    {
        "id": 1,
        "name": "AI & Machine Learning",
        "badge_color": "#4285F4", # Google Blue
        "description": "Deep dives into Vertex AI, Gemini models, ML workflows, and cloud TPU architecture."
    },
    {
        "id": 2,
        "name": "Cloud Infrastructure & Security",
        "badge_color": "#34A853", # Google Green
        "description": "Modern serverless, containerization, Zero-Trust security, and global multi-region databases."
    }
]

# Speakers Database
SPEAKERS = {
    "s1": {
        "id": "s1",
        "first_name": "Dr. Elena",
        "last_name": "Rostova",
        "role": "Principal AI Architect",
        "company": "Google Cloud",
        "linkedin": "https://www.linkedin.com/in/elena-rostova-gcp-ai",
        "avatar_bg": "linear-gradient(135deg, #4285F4, #91B4FB)",
        "bio": "Specializes in large-scale generative AI deployment and enterprise foundation model fine-tuning."
    },
    "s2": {
        "id": "s2",
        "first_name": "Marcus",
        "last_name": "Vance",
        "role": "Distinguished Staff Engineer",
        "company": "DeepMind Enterprise",
        "linkedin": "https://www.linkedin.com/in/marcus-vance-deepmind",
        "avatar_bg": "linear-gradient(135deg, #EA4335, #FF8A80)",
        "bio": "Lead researcher focusing on Gemini multimodal agentic workflows and prompt orchestration."
    },
    "s3": {
        "id": "s3",
        "first_name": "Sophia",
        "last_name": "Chen",
        "role": "VP of Cloud Serverless Engineering",
        "company": "Google Cloud",
        "linkedin": "https://www.linkedin.com/in/sophiachen-cloudrun",
        "avatar_bg": "linear-gradient(135deg, #FBBC04, #FFE082)",
        "bio": "Pioneer behind Google Cloud Run v2 architecture and zero-scale microservices optimization."
    },
    "s4": {
        "id": "s4",
        "first_name": "Alexandre",
        "last_name": "Dubois",
        "role": "Director of Data Analytics",
        "company": "DataTech Solutions",
        "linkedin": "https://www.linkedin.com/in/alex-dubois-bigquery",
        "avatar_bg": "linear-gradient(135deg, #34A853, #A5D6A7)",
        "bio": "BigQuery expert with over 12 years of experience building streaming analytics for Fortune 500 enterprises."
    },
    "s5": {
        "id": "s5",
        "first_name": "Priya",
        "last_name": "Sharma",
        "role": "Head of Cyber Threat Intelligence",
        "company": "Mandiant / Google Cloud",
        "linkedin": "https://www.linkedin.com/in/priya-sharma-security",
        "avatar_bg": "linear-gradient(135deg, #AB47BC, #E1BEE7)",
        "bio": "Leads incident response and Zero-Trust architecture implementations across global cloud environments."
    },
    "s6": {
        "id": "s6",
        "first_name": "Tariq",
        "last_name": "Al-Mansoor",
        "role": "Lead TPU Systems Architect",
        "company": "Google Hardware Lab",
        "linkedin": "https://www.linkedin.com/in/tariq-almansoor-tpu",
        "avatar_bg": "linear-gradient(135deg, #00ACC1, #80DEEA)",
        "bio": "Expert in Cloud TPU v5p pod clusters, distributed JAX parallelism, and high-throughput training loops."
    },
    "s7": {
        "id": "s7",
        "first_name": "Hannah",
        "last_name": "Kowalski",
        "role": "Principal Site Reliability Engineer",
        "company": "Kubernetes Core Team",
        "linkedin": "https://www.linkedin.com/in/hannah-kowalski-sre",
        "avatar_bg": "linear-gradient(135deg, #FF7043, #FFCCBC)",
        "bio": "SRE veteran specializing in GKE Enterprise multi-cluster management and Cloud Spanner global distribution."
    },
    "s8": {
        "id": "s8",
        "first_name": "Carlos",
        "last_name": "Mendoza",
        "role": "Principal Terraform & IaC Lead",
        "company": "HashiCorp / GCP Partner",
        "linkedin": "https://www.linkedin.com/in/carlos-mendoza-iac",
        "avatar_bg": "linear-gradient(135deg, #5C6BC0, #C5CAE9)",
        "bio": "Author of open-source GCP Terraform modules with over 20M downloads worldwide."
    },
    "s9": {
        "id": "s9",
        "first_name": "Naomi",
        "last_name": "Tanaka",
        "role": "Senior Graph Database Scientist",
        "company": "Cloud Data Labs",
        "linkedin": "https://www.linkedin.com/in/naomi-tanaka-graph",
        "avatar_bg": "linear-gradient(135deg, #EC407A, #F8BBD0)",
        "bio": "Builds knowledge graphs and real-time recommendation engines on Google Cloud Spanner & Vertex Graph Search."
    },
    "s10": {
        "id": "s10",
        "first_name": "Vikram",
        "last_name": "Deshmukh",
        "role": "Principal Cloud Security Consultant",
        "company": "Google Cloud",
        "linkedin": "https://www.linkedin.com/in/vikram-deshmukh-security",
        "avatar_bg": "linear-gradient(135deg, #26A69A, #B2DFDB)",
        "bio": "Advises financial institutions on IAM policies, Cloud Security Command Center Premium, and compliance."
    }
}

# Exactly 8 Talks for the 1-Day Event
TALKS = [
    {
        "id": 1,
        "title": "Building Enterprise Autonomous Agents with Vertex AI & Gemini 1.5 Pro",
        "category_id": 1,
        "category_name": "AI & Machine Learning",
        "time_slot": "09:00 AM - 09:45 AM",
        "start_time": "09:00",
        "end_time": "09:45",
        "description": "Learn how to architect, evaluate, and deploy production-ready agentic systems using Vertex AI Agent Builder, Gemini 1.5 Pro long-context windows, and function calling workflows.",
        "speakers": [SPEAKERS["s1"], SPEAKERS["s2"]] # 2 speakers max
    },
    {
        "id": 2,
        "title": "Serverless at Scale: Deep Dive into Cloud Run v2 Architecture",
        "category_id": 2,
        "category_name": "Cloud Infrastructure & Security",
        "time_slot": "09:50 AM - 10:35 AM",
        "start_time": "09:50",
        "end_time": "10:35",
        "description": "An insider exploration of Cloud Run v2 capabilities including sidecar containers, direct VPC egress, custom metrics autoscaling, and cold-start minimization techniques.",
        "speakers": [SPEAKERS["s3"]] # 1 speaker
    },
    {
        "id": 3,
        "title": "Real-Time Data Pipelines with BigQuery Continuous Queries & Apache Beam",
        "category_id": 1,
        "category_name": "AI & Machine Learning",
        "time_slot": "10:40 AM - 11:25 AM",
        "start_time": "10:40",
        "end_time": "11:25",
        "description": "Discover how BigQuery streaming dataframes and Apache Beam on Dataflow enable sub-second ETL, automated continuous queries, and instant ML inference on incoming telemetry.",
        "speakers": [SPEAKERS["s4"]] # 1 speaker
    },
    {
        "id": 4,
        "title": "Zero-Trust Security & Mandiant Threat Intelligence Integration on GCP",
        "category_id": 2,
        "category_name": "Cloud Infrastructure & Security",
        "time_slot": "11:30 AM - 12:15 PM",
        "start_time": "11:30",
        "end_time": "12:15",
        "description": "Explore real-world cloud threat vectors and implement BeyondCorp Zero-Trust controls alongside Mandiant proactive threat hunting integrated into Chronicle Security Operations.",
        "speakers": [SPEAKERS["s5"], SPEAKERS["s10"]] # 2 speakers max
    },
    # Lunch Break occurs from 12:15 PM to 01:15 PM (60 mins)
    {
        "id": 5,
        "title": "Fine-Tuning Open LLMs on Cloud TPU v5p Pod Clusters with JAX",
        "category_id": 1,
        "category_name": "AI & Machine Learning",
        "time_slot": "01:15 PM - 02:00 PM",
        "start_time": "13:15",
        "end_time": "14:00",
        "description": "Step-by-step hands-on guide on configuring TPU v5p supercomputers, distributing model weights via MaxText & JAX, and accelerating multi-terabyte dataset training.",
        "speakers": [SPEAKERS["s6"]] # 1 speaker
    },
    {
        "id": 6,
        "title": "Multi-Region Global Resilience with Cloud Spanner & GKE Enterprise",
        "category_id": 2,
        "category_name": "Cloud Infrastructure & Security",
        "time_slot": "02:05 PM - 02:50 PM",
        "start_time": "14:05",
        "end_time": "14:50",
        "description": "Architecting mission-critical active-active workloads across three continents using GKE Anthos Service Mesh and Cloud Spanner's true global ACID transaction consistency.",
        "speakers": [SPEAKERS["s7"]] # 1 speaker
    },
    {
        "id": 7,
        "title": "Infrastructure as Code: Advanced Terraform Patterns & Policy Engine for GCP",
        "category_id": 2,
        "category_name": "Cloud Infrastructure & Security",
        "time_slot": "02:55 PM - 03:40 PM",
        "start_time": "14:55",
        "end_time": "15:40",
        "description": "Best practices for modular Terraform codebase design, automated governance with Policy Controller, drift detection pipelines, and zero-downtime infrastructure updates.",
        "speakers": [SPEAKERS["s8"]] # 1 speaker
    },
    {
        "id": 8,
        "title": "Graph Analytics & Vector Search Engine with Google Cloud Databases",
        "category_id": 1,
        "category_name": "AI & Machine Learning",
        "time_slot": "03:45 PM - 04:30 PM",
        "start_time": "15:45",
        "end_time": "16:30",
        "description": "Combining Graph queries with vector embeddings in AlloyDB and Vertex AI Vector Search to power hybrid RAG architectures and enterprise knowledge graphs.",
        "speakers": [SPEAKERS["s9"]] # 1 speaker
    }
]

def get_all_talks():
    return TALKS

def get_talk_by_id(talk_id):
    for talk in TALKS:
        if talk["id"] == int(talk_id):
            return talk
    return None

def filter_talks(search_query="", category_id=None, speaker_name=""):
    results = []
    query = search_query.strip().lower()
    speaker_q = speaker_name.strip().lower()

    for talk in TALKS:
        # Category Filter
        if category_id is not None and category_id != "" and str(category_id) != "all":
            if str(talk["category_id"]) != str(category_id):
                continue
        
        # Speaker Dropdown Filter
        if speaker_q:
            match_spk = False
            for spk in talk["speakers"]:
                full_name = f"{spk['first_name']} {spk['last_name']}".lower()
                if speaker_q in full_name or speaker_q in spk["id"].lower():
                    match_spk = True
                    break
            if not match_spk:
                continue

        # General Text Query Filter (Title, Description, Speaker Names, Category Name)
        if query:
            in_title = query in talk["title"].lower()
            in_desc = query in talk["description"].lower()
            in_cat = query in talk["category_name"].lower()
            in_speakers = any(
                query in spk["first_name"].lower() or 
                query in spk["last_name"].lower() or 
                query in f"{spk['first_name']} {spk['last_name']}".lower() or
                query in spk.get("role", "").lower()
                for spk in talk["speakers"]
            )
            if not (in_title or in_desc or in_cat or in_speakers):
                continue

        results.append(talk)
    return results
