from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string


from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home_page)  
    
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home_page(request)
        # think about similarities here between render and render to string:
        # render takes a temoplate and outs the html intp response.content,
        # while render_to_string takes html in a template and turns it into
        # a string so that the contents can be compared easily  
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
