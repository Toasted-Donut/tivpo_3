from datetime import date
from date_stuff import prev_month
from behave import *


@given('date is 18.10.2023')
def step_impl(context):
    context.date = date(2023,10,18)


@when('fun is called1')
def step_impl(context):
    context.date = prev_month(context.date)


@then('date now is 18.09.2023')
def step_impl(context):
    assert context.date == date(2023,9,18)


@given('date is 01.01.2023')
def step_impl(context):
    context.date = date(2023,1,1)


@when('fun is called2')
def step_impl(context):
    context.date = prev_month(context.date)


@then('date now is 01.12.2022')
def step_impl(context):
    assert context.date == date(2022,12,1)
