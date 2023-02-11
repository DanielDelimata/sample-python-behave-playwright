import os
from xml.etree.cElementTree import Element, SubElement, ElementTree

import allure
from allure_commons.types import AttachmentType
from behave.api.async_step import use_or_create_async_context
from behave.runner import Context
from playwright.async_api import async_playwright

from features.lib.pages.customers_page import CustomersPage


def before_scenario(context: Context, scenario):
    use_or_create_async_context(context)
    loop = context.async_context.loop
    context.playwright = loop.run_until_complete(async_playwright().start())
    context.browser = loop.run_until_complete(context.playwright.chromium.launch(headless=True))
    context.page = loop.run_until_complete(context.browser.new_page())
    context.customers_page = CustomersPage(context)


def after_scenario(context: Context, scenario):
    loop = context.async_context.loop

    if scenario.status == "failed":
        allure.attach(loop.run_until_complete(context.page.screenshot()), name="Screenshot",
                      attachment_type=AttachmentType.PNG)
    loop.run_until_complete(context.page.close())


def before_all(context):
    allure_results_dir = os.path.join("../../allure_results")
    os.makedirs(allure_results_dir, exist_ok=True)
    environment = Element("environment")
    for key, value in os.environ.items():
        param = SubElement(environment, "parameter")
        SubElement(param, "key").text = key
        SubElement(param, "value").text = value
    ElementTree(environment).write(os.path.join(allure_results_dir, "environment.xml"))
