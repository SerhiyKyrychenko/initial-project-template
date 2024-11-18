# app_blog/views.py
from django.shortcuts import render  # Виправлено імпорт
from django.views.generic import TemplateView

# Створіть свої представлення тут.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):  # Вирівняно відступи
        return render(request, 'index.html', context=None)  # Виправлено лапки
