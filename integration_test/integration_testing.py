import unittest
import requests

BASE_URL = "http://localhost:5000/api"

class TestStudentRegistrationSystem(unittest.TestCase):

    def test_register_student(self):
        """Test registering a new student."""
        payload = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "course": "Computer Science"
        }
        response = requests.post(f"{BASE_URL}/students", json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())

    def test_get_student_details(self):
        """Test retrieving details of a registered student."""
        student_id = self._register_student()
        response = requests.get(f"{BASE_URL}/students/{student_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "John Doe")

    def test_update_student_info(self):
        """Test updating a student's information."""
        student_id = self._register_student()
        update_payload = {
            "name": "Johnathan Doe",
            "email": "johnathan.doe@example.com"
        }
        response = requests.put(f"{BASE_URL}/students/{student_id}", json=update_payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Johnathan Doe")

    def test_delete_student(self):
        """Test deleting a student record."""
        student_id = self._register_student()
        response = requests.delete(f"{BASE_URL}/students/{student_id}")
        self.assertEqual(response.status_code, 204)
        # Verify deletion
        response = requests.get(f"{BASE_URL}/students/{student_id}")
        self.assertEqual(response.status_code, 404)

    def test_register_student_with_existing_email(self):
        """Test registering a student with an existing email."""
        self._register_student()
        payload = {
            "name": "Jane Doe",
            "email": "john.doe@example.com",  # Same email as before
            "course": "Mathematics"
        }
        response = requests.post(f"{BASE_URL}/students", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

    def _register_student(self):
        """Helper method to register a student and return the student ID."""
        payload = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "course": "Computer Science"
        }
        response = requests.post(f"{BASE_URL}/students", json=payload)
        return response.json()["id"]

if __name__ == "__main__":
    unittest.main()