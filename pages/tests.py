from django.test import SimpleTestCase

# Create your tests here.
class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    #Cursor generated tests -- very cool
    # def test_home_page_status_code(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)

    # def test_home_page_contains_correct_html(self):
    #     response = self.client.get('/')
    #     self.assertContains(response, "Homepage")

    # def test_home_page_does_not_contain_incorrect_html(self):
    #     response = self.client.get('/')
    #     self.assertNotContains(response, "Hi there! I should not be on the page.")

class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)