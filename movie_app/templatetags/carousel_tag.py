from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag(takes_context=True)
def render_carousel(context):
    # Add any carousel rendering logic here

    latest_movies = context.get('latest_movies', [])
    
    return render_to_string('movie_app/carousel.html', {'latest_movies': latest_movies})