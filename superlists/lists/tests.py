from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item



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
        
    def test_home_page_can_save_a_POST_request(self):
        '''
        Notice that 'item_text' key is assigned 'A new list item' string in the post
        dic-like object. 'item_text' is in post because of name= 'item_text' in input
        tag in home.html. Now, the dictionary in expected_html further down is completely
        different, and it contains the same value as 'item_text.' Where in the first 
        'A new list item', the user supposedly entered it, the second is actually a 
        response from views.py back to the home.html file.  
        '''
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        # this tests the response for containing the string 'A new list item':
        self.assertIn('A new list item', response.content.decode())
        # this tests the html, rendered from the response
        expected_html = render_to_string(
            'home.html',
            {'new_item_text':  'A new list item'}
        )
        #this finally asserts that the HttpResponse object really is our home.html file,
        # plus the mapping of the 'new_item_text' python object to the string "A new list
        # item"
        self.assertEqual(response.content.decode(), expected_html)
        

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
