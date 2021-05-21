from behave import *
import datetime


@given('Exists a session for the movie "{movie_name}"')
def step_impl(context, movie_name):
    from CinemaApp.models import Session, Movie
    movie = Movie.objects.get(name=movie_name)
    for row in context.table:
        session = Session(movie=movie)
        for heading in row.headings:
            if heading == "duration":
                time = list(map(int, row[heading].split(':')))
                session.duration = datetime.timedelta(hours=time[0], minutes=time[1], seconds=time[2])
            else:
                setattr(session, heading, row[heading])
        session.save()


@then('I edit the current session')
def step_impl(context):
    context.browser.find_by_id('Edit').click()
    form = context.browser.find_by_tag('form').first
    for heading in context.table.headings:
        if heading == "date":
            context.browser.fill(heading, context.table[0][heading])
        else:
            element = context.browser.find_by_id(heading).first
            element.select(context.table[0][heading])
    form.find_by_value('Update').first.click()


@then('I delete the current session')
def step_impl(context):
    context.browser.find_by_id('delete_session').click()


@then('There is no "{link_text}" link available')
def step_impl(context, link_text):
    assert context.browser.is_element_not_present_by_xpath('//a[text()="'+link_text+'"]')
