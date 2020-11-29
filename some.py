import logging
import parseit

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1466769274:AAErB_nLhv0tdYSbEQDqgr0g5lOmCpog6p4'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['getdrugs'])
async def get_info(message: types.Message):
	await message.answer('Введите название лекарства')
	@dp.message_handler()
	async def get_drug_name(message: types.Message):
		order = message.text
		parseit.makelist(order)
		some = parseit.showlist()
		for x in some:
			a = x[1] + ' ' + x[2] + '\n' + x[4]
			await message.answer(a)
		parseit.clearlist()
		

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)