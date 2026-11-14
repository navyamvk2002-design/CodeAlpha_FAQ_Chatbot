
import unittest
from chatbot import get_answer


class TestFAQChatbot(unittest.TestCase):

    def test_office_hours(self):
        answer = get_answer("What are your office hours?")
        self.assertEqual(
            answer,
            "Our working hours are 9 AM to 5 PM."
        )

    def test_contact_support(self):
        answer = get_answer("How can I contact support?")
        self.assertEqual(
            answer,
            "You can contact our support team through email."
        )

    def test_location(self):
        answer = get_answer("Where are you located?")
        self.assertEqual(
            answer,
            "We are located in Kerala, India."
        )

    def test_services(self):
        answer = get_answer("What services do you provide?")
        self.assertEqual(
            answer,
            "We provide web development and software solutions."
        )

    def test_unknown_question(self):
        answer = get_answer("What is the weather today?")
        self.assertIn("Sorry", answer)


if __name__ == "__main__":
    unittest.main()
