from datetime import date

from date_stuff import get_date
from behave import *


'start date is today'
def step_impl(context):
    context.date = date.today()


@when('step back is 5 days')
def step_impl(context):
    context.date = get_date(5,False,context.date)


@then('date now is 5 days back')
def step_impl(context):
    assert context.date.day+5 == date.today().day


'start date is 12.03.2023'
def step_impl(context):
    context.date = date(2023,3,12)


@when('step back is 4 days')
def step_impl(context):
    context.date = get_date(4,False,context.date)


@then('date now is 8 march 2023')
def step_impl(context):
    assert context.date == date(2023,3,8)