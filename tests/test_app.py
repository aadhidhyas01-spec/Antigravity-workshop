"""
Unit Test Suite for Google Cloud Tech Summit 1-Day Conference Flask Application.
"""

import unittest
from app import app
from data import TALKS, CONFERENCE_INFO, filter_talks, get_talk_by_id

class ConferenceAppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_homepage_status(self):
        """Test home page loads with 200 OK and contains header info."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Google Cloud Tech Summit", response.data)
        self.assertIn(b"09:00 AM", response.data)

    def test_total_talks_count(self):
        """Requirement 2: Validate 1-day event has exactly 8 talks in total."""
        self.assertEqual(len(TALKS), 8)

    def test_max_speakers_per_talk(self):
        """Requirement 3 & 4: Each talk must have 1 or 2 max speakers."""
        for talk in TALKS:
            num_speakers = len(talk["speakers"])
            self.assertTrue(1 <= num_speakers <= 2, f"Talk ID {talk['id']} has invalid speaker count {num_speakers}")

    def test_talk_schema_attributes(self):
        """Requirement 4: Verify talk schema (id, title, speakers, category, description, time)."""
        for talk in TALKS:
            self.assertIn("id", talk)
            self.assertIn("title", talk)
            self.assertIn("speakers", talk)
            self.assertIn("category_id", talk)
            self.assertIn("category_name", talk)
            self.assertIn("description", talk)
            self.assertIn("time_slot", talk)

    def test_speaker_schema_attributes(self):
        """Requirement 5: Verify speaker schema (First Name, Last Name, LinkedIn URL)."""
        for talk in TALKS:
            for speaker in talk["speakers"]:
                self.assertIn("first_name", speaker)
                self.assertIn("last_name", speaker)
                self.assertIn("linkedin", speaker)
                self.assertTrue(speaker["linkedin"].startswith("http"), f"Speaker {speaker} missing valid LinkedIn URL")

    def test_lunch_break_duration(self):
        """Requirement 7: Verify a lunch break of 60 minutes is provided."""
        lunch = CONFERENCE_INFO["lunch_break"]
        self.assertEqual(lunch["duration_minutes"], 60)
        self.assertEqual(lunch["start_time"], "12:15 PM")
        self.assertEqual(lunch["end_time"], "01:15 PM")

    def test_search_by_category(self):
        """Requirement 6: Search/Filter by category."""
        cat_1_results = filter_talks(category_id=1)
        self.assertTrue(len(cat_1_results) > 0)
        for t in cat_1_results:
            self.assertEqual(t["category_id"], 1)

        cat_2_results = filter_talks(category_id=2)
        self.assertTrue(len(cat_2_results) > 0)
        for t in cat_2_results:
            self.assertEqual(t["category_id"], 2)

    def test_search_by_speaker(self):
        """Requirement 6: Search/Filter by speaker name."""
        results = filter_talks(speaker_name="Elena")
        self.assertTrue(len(results) >= 1)
        self.assertIn("Autonomous Agents", results[0]["title"])

    def test_search_by_title(self):
        """Requirement 6: Search/Filter by title keyword."""
        results = filter_talks(search_query="BigQuery")
        self.assertTrue(len(results) >= 1)
        self.assertIn("BigQuery", results[0]["title"])

    def test_api_talks_endpoint(self):
        """Test /api/talks REST endpoint."""
        response = self.client.get('/api/talks?q=Vertex')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(json_data["status"], "success")
        self.assertTrue(json_data["count"] >= 1)

    def test_api_talk_detail_endpoint(self):
        """Test single talk API detail endpoint."""
        response = self.client.get('/api/talk/1')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(json_data["talk"]["id"], 1)

    def test_api_talk_not_found(self):
        """Test non-existent talk returns 404."""
        response = self.client.get('/api/talk/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
