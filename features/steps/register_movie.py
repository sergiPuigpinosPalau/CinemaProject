from behave import *
import operator
from functools import reduce
from django.db.models import Q

use_step_matcher("parse")


@given('Exists a movie')
def step_impl(context):
    from CinemaApp.models import Movie
    for row in context.table:
        movie = Movie()
        for heading in row.headings:
            setattr(movie, heading, row[heading])
        movie.save()


@when(u'I register a movie')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('CinemaApp:create_movie'))
        if context.browser.url == context.get_url('CinemaApp:create_movie'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
                #context.wait()
                context.browser.find_by_css('li.ui-menu-item').first.click()
            form.find_by_value('Submit').first.click()


@then(u'I\'m viewing the details page of a movie')
def step_impl(context):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from CinemaApp.models import Movie
    movie = Movie.objects.filter(reduce(operator.and_, q_list)).get()
    if context.browser.url != context.get_url('CinemaApp:detail_movie', movie.pk):
        context.browser.visit(context.get_url('CinemaApp:detail_movie', movie.pk))
    assert context.browser.find_by_id('Title').text.startswith(movie.name)


@then('I delete the current movie')
def step_impl(context):
    context.browser.find_by_id('delete_movie').click()


@then(u'There are {count:n} movies')
def step_impl(context, count):
    from CinemaApp.models import Movie
    assert count == Movie.objects.count()