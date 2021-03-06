from functools import reduce

from behave import *
import operator
from django.db.models import Q
import os


@given('Exists a hall')
def step_impl(context):
    from CinemaApp.models import Hall
    for row in context.table:
        hall = Hall()
        for heading in row.headings:
            setattr(hall, heading, row[heading])
        hall.save()


@given('Exists a schedule')
def step_impl(context):
    from CinemaApp.models import Schedule
    for row in context.table:
        schedule = Schedule()
        for heading in row.headings:
            setattr(schedule, heading, row[heading])
        schedule.save()


@when('I register a session at the movie "{movie_name}"')
def step_impl(context, movie_name):
    from CinemaApp.models import Movie
    movie = Movie.objects.get(name=movie_name)
    for row in context.table:
        context.browser.visit(context.get_url('CinemaApp:create_session', movie.pk))
        if context.browser.url == context.get_url('CinemaApp:create_session', movie.pk):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                if heading == "date":
                    context.browser.fill(heading, row[heading])
                else:
                    element = context.browser.find_by_id(heading).first
                    element.select(row[heading])
            form.find_by_value('Submit').first.click()


@then('I\'m viewing the details of the session for the movie "{movie_name}"')
def step_impl(context, movie_name):
    from CinemaApp.models import Movie
    movie = Movie.objects.get(name=movie_name)
    if context.browser.url != context.get_url('CinemaApp:detail_movie', movie.pk):
        context.browser.visit(context.get_url('CinemaApp:detail_movie', movie.pk))
    review_par_links = context.browser.find_by_id('schedule_table')
    for i, row in enumerate(context.table):
        assert review_par_links[0].text.split('\n')[1].startswith(row['duration'] + " " + row['date'] + " " + row['hall'] + " " + row['schedule'])


@then('There are {count:n} sessions')
def step_impl(context, count):
    from CinemaApp.models import Session
    assert count == Session.objects.count()


