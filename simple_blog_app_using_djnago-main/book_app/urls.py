from django.urls import path,include
from . import views

app_name = 'book_app'


urlpatterns = [
path("",views.index,name="index"), 
path("search",views.search,name="search"), 
path("post/<id>",views.post_one,name="post_one"),
path("new_comment/<id>",views.new_comment,name="new_comment"),
]