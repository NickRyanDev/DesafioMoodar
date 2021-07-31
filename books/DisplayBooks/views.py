from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def GetBooks(TemplateView):
    template_name = 'books.html'
    def get_context_data(self, *args, **kwargs):
        context = {
            'books' : Get_Books(),
            'povcha' : Get_PovCharacter(),
            'character' : Get_Details(),
            'cover' : Get_Covers(),
        }
        return context
