from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string

# Create your tests here.
# class SmokeTest(TestCase):

# 	def test_bad_math(self):
# 		self.assertEqual(1+1,3)

class HomePagetest(TestCase):
	def test_root_url_resolve_to_home_page(self):
		found = resolve('/')
		self.assertEqual(found.func,home_page)
# way of obj 
	# def test_home_page_returns_correct_html(self):
	# 	request=HttpRequest()
	# 	response=home_page(request)
	# 	html = response.content.decode('utf8')
	# 	self.assertTrue(html.startswith('<html>'))
	# 	self.assertIn('<title>To-Do lists</title>',html)
	# 	self.assertTrue(html.strip().endswith('</html>'))

# way2 using Django test client

	def test_home_page_returns_correct_html(self):
		 request = HttpRequest()
		 response= home_page(request)
		 html = response.content.decode('utf8')
		 expeted_html = render_to_string('home.html')
		 self.assertEqual(html,expeted_html)
