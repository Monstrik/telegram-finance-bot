import logging
import os

# import aiohttp
from aiogram import Bot, Dispatcher, executor, types

import exceptions
import expenses
from categories import Categories
from middlewares import AccessMiddleware

logging.basicConfig(level=logging.INFO)

# PROXY_URL = os.getenv("TELEGRAM_PROXY_URL")
# PROXY_AUTH = aiohttp.BasicAuth(
#     login=os.getenv("TELEGRAM_PROXY_LOGIN"),
#     password=os.getenv("TELEGRAM_PROXY_PASSWORD")
# )
# bot = Bot(token=API_TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

ACCESS_ID = os.getenv("TELEGRAM_ACCESS_ID")
dp.middleware.setup(AccessMiddleware(ACCESS_ID))


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """Send help text"""
    await message.answer(
        "Expenses Tracker Bot\n\n"
        "Add exp: 250 taxi\n"
        "Day stats: /today\n"
        "Month stats: /month\n"
        "Last expenses: /expenses /exp /e\n"
        "List Categories: /categories /cat /c")


@dp.message_handler(lambda message: message.text.startswith('/del'))
async def del_expense(message: types.Message):
    """del expense by id"""
    row_id = int(message.text[4:])
    expenses.delete_expense(row_id)
    answer_message = "Deleted"
    await message.answer(answer_message)


@dp.message_handler(commands=['categories', 'cats', 'cat', 'c'])
async def categories_list(message: types.Message):
    """Send categories list"""
    categories = Categories().get_all_categories()
    answer_message = "Categories:\n\n* " + \
                     ("\n* ".join([c.name + ' (' + ", ".join(c.aliases) + ')' for c in categories]))
    await message.answer(answer_message)


@dp.message_handler(commands=['today', 'day', 'd'])
async def today_statistics(message: types.Message):
    """Send today statistics"""
    answer_message = expenses.get_today_statistics()
    await message.answer(answer_message)


@dp.message_handler(commands=['month', 'm'])
async def month_statistics(message: types.Message):
    """Send month statistics"""
    answer_message = expenses.get_month_statistics()
    await message.answer(answer_message)


@dp.message_handler(commands=['expenses', 'exp', 'e'])
async def list_expenses(message: types.Message):
    """Send last expenses"""
    last_expenses = expenses.last()
    if not last_expenses:
        await message.answer("Hurray! No expenses.")
        return

    last_expenses_rows = [
        f"${expense.amount} for {expense.category_name} - press "
        f"/del{expense.id} for delete"
        for expense in last_expenses]
    answer_message = "Last expenses:\n\n* " + "\n\n* " \
        .join(last_expenses_rows)
    await message.answer(answer_message)


@dp.message_handler()
async def add_expense(message: types.Message):
    """add expense"""
    try:
        expense = expenses.add_expense(message.text)
    except exceptions.NotCorrectMessage as e:
        await message.answer(str(e))
        return
    answer_message = (
        f"Added ${expense.amount} to {expense.category_name}.\n\n"
        f"{expenses.get_today_statistics()}")
    await message.answer(answer_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
