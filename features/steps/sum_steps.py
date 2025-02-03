import json
import os

from behave import given, when, then
from utils.helpers import *

@given('I have two numbers {num1:d} and {num2:d}')
def step_given_two_numbers(context, num1, num2):
    context.num1 = num1
    context.num2 = num2

@when('I add the numbers')
def step_when_add_numbers(context):
    context.result = context.num1 + context.num2

@then('the result should be {expected_result:d}')
def step_then_result_should_be(context, expected_result):
    assert context.result == expected_result, f"Expected {expected_result}, but got {context.result}"

@given('I have test data from {filename}')
def step_given_test_data_from_file(context, filename):
    file_path = os.path.join(get_project_root(), 'test_data', filename)
    with open(file_path) as f:
        context.test_data = json.load(f)

