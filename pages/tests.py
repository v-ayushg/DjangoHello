from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

# For our first tests, we’ll check that the two URLs for our website, 
# the homepage and about page, both return HTTP status codes of 200, 
# the standard response for a successful HTTP request.

class HomepageTests(SimpleTestCase):
    def test_url_exits_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

# we added the name "home" for the homepage path and "about" for the about page. 
# To check both, we can use the very handy Django utility function reverse. 
# Don’t forget to import reverse at the top of the file and add a new unit test for each below.

    def test_url_availability_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

# We have tested our URL locations and names so far but not our templates. 
# Let’s make sure that the correct templates–home.html and about.html–are used on each page and 
# that they display the expected content of "<h1>Homepage</h1>" and "<h1>About page</h1>" respectively.
# We can use assertTemplateUsed and assertContains to achieve this.
        
    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):  # new
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")


# Class for About page
        
class AboutpageTests(SimpleTestCase):
    def test_url_exits_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_availability_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):  # new
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About page</h1>")
