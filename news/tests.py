from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.james = Editor(first_name='James', last_name='Muia', email='james@moringa.com')
    
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    #Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):
    
    def setUp(self):
        #Creating and saving an editor
        self.james = Editor(first_name='James', last_name='Muia', email='james@moringa.com')
        self.james.save_editor()

        
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        #Creating a new article and saving it
        self.new_article = Article(title = 'Test Article', post='Just a random one', editor = self.james)
        self.new_article.save()

        #Add the tag to the article
        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        Article.objects.all().delete()
        tags.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.today_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2020-7-28'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)