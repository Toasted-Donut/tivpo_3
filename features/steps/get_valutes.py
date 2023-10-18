from currency_stuff import get_valutes
from behave import *


@given('today date')
def step_impl(context):
    context.datedelta=0


@when('flag is false')
def step_impl(context):
    context.dict = get_valutes(context.datedelta,False)


@then('dictionary have currencies values for today without rub')
def step_impl(context):
    assert context.dict["CharCode"][0] != "RUB"


@given('yesterday date')
def step_impl(context):
    context.datedelta = 1


@when('flag is true')
def step_impl(context):
    context.dict = get_valutes(context.datedelta, True)


@then('dictionary have currencies values for yesterday with rub')
def step_impl(context):
    assert context.dict["CharCode"][0] == "RUB"