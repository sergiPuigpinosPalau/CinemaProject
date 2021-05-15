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
                if heading == 'image':
                    context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()


@then('I\'m viewing the details of the session for the movie "{movie_name}"')
def step_impl(context, movie_name):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from CinemaApp.models import Movie
    q_list.append(Q(('restaurant', Movie.objects.get(name=movie_name))))
    from CinemaApp.models import Session
    session = Session.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(session)


@then('There are {count:n} dishes')
def step_impl(context, count):
    from myrestaurants.models import Dish
    assert count == Dish.objects.count()


@when('I edit the current dish')
def step_impl(context):
    context.browser.find_link_by_text('edit').click()
    # TODO: Test also using direct edit view link
    # context.browser.visit(context.get_url('myrestaurants:dish_edit', dish.pk))
    form = context.browser.find_by_tag('form').first
    for heading in context.table.headings:
        context.browser.fill(heading, context.table[0][heading])
    form.find_by_value('Submit').first.click()