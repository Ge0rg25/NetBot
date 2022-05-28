import logging
from aiogram import Bot, Dispatcher, executor, types
import Database
import key
import config
import other

logging.basicConfig(level=logging.INFO)


db = Database.DateB()
bot = Bot(token=config.telegram_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await bot.send_video(message.from_user.id, 'https://du.sf-converter.com/go?payload=1*eJzVlGuPokgUhv'
                                               '%2BK6aQru8lqF1DcOqlM8NpCe8FuEfuLQSixFgoQENTJ%2FvctcDbT83E2'
                                               '%2B2EnMW8dSk8dznvq8etDkZ5zn6zz%2BOH54ViWWfH89FTXde'
                                               '%2BansvznvT8lD3VXukfv1QYOh%2FhcRZVc8V%2F'
                                               '%2BONb5jT46UTvHND0x4p5jrrdbpF0PZmRKFFuvTBNw5hUNCBpe1QbZbF33Xt'
                                               '%2B9IVcMpoTLCiyJOtIVSAgFFtTb7ktJrOhd1oXh'
                                               '%2BlS2W2S0EgBzbCCegKSezrqySqgAU67Rv%2Bw2O8'
                                               '%2FFOt2DUVPIOVsgsYuXIxUd0NOznFvZWMzFHPrpDmAll6IBQTBvWf8rU'
                                               'eQk9OZv0dRxPhKCsCO%2BIQAY1gSHsWBqACW4E898T3%2BlEJdvSXFDbA'
                                               'Ce2e%2BlyY5YBVmXChGIIuxiABNaOnXSbDPCizpogx57czHKPWdwQXu2F'
                                               'a9SNZqZ0PkG6Mjra%2BuAKosr7AAGGUEtx4%2FimOWIZAU%2BKAFvkulce'
                                               'UL%2FZfVYkdfonOuaxMQ0rx9dT8mCZYQhLKkgeCcY1GAPahCELOS2wwFpGm'
                                               '6LkmqKAoSaPe49aqo8qdDxR2WQERI5sW0Iu2BBz4i3giEgqRKjRs8VEWkAB9'
                                               'vRn1Q8m9lJAlIEkGCh%2F7SzK%2FjKmLmZWfwTr3c4%2Fbcp8yTCeVCs0aCR'
                                               'vg4GjPbYfDg%2Bxia3czn2njBl8YLviQFF94q16ZRvvAWufLmQPxPNXZsElgjz'
                                               'S9Yk8PaQ6qmfNYc%2FmksPJGG2JhIg93FqFfGNHztBjZT9tGmQnM2Dzem769XI'
                                               '%2FNM%2FXTVnUXvV1OV3fh8i%2BpwMB3IO3EyjGwYSu5tprL4PdYWEXPe%2FcAL3w'
                                               '4TFifrj9c8sbMAtIUWJ2ibWr2yp0fDCj2tb83HdT7pOp7B1FNN4PtYn1vJyPRn22Epu'
                                               '6n9ah2E2KD9UW3ErkreNjZMgsLampnovw0F5pRSiEzb3rxMtdQaa1QIH6Uh%2F3BGW9x'
                                               '%2BQUYlBXhNVPCwuXaChFqVW1UaVWB7HcVW71cTtao2qmq%2FDuSt3z8LecO4oqM75'
                                               'FDvyVD%2FBLkOOdIqhBzL%2Fwxy8V9Bfh%2Fj%2Fw3zhr4pK4uFpaz6FG6tYXf9lr1K'
                                               'siOok7mzGV1re3E798N3S3e0g0GNP%2BlIlIqbenYWCVmyvDB3mwweq%2Feba5vRbU1'
                                               '3FxfpSx9Z9Z2%2BH3Hn%2Fyvb42HylqKtxw1h2Xj64gonlxjV6zYxk5PwQvzravGRjC'
                                               '6BNpgOg8F2b5uTai2b26632e90qjiXtFwK9OZMvXJYLdFlE6P1hGNe0jImnPGZdyGJTz'
                                               'qDa06TTrezOZKcdGjRYdcOo0nQ%2Ba2I05oEv%2FOc%2B8AKo3x4%2Fs72X38Dp6SqQQ'
                                               '%3D%3D*1653576399*4faaf7ed69d5809e',
                         reply_markup=key.glav_key)
    db.add_user(message.from_user.id)


@dp.message_handler(content_types=['text'], text=['Полные лекции', 'Короткие видео', 'Ссылки, книги'])
async def obrab1(message: types.Message):
    if message.text == 'Полные лекции':
        await bot.send_message(message.from_user.id,
                               'Выберите тему:',
                               reply_markup=key.get_full_thems_keys())
    elif message.text == 'Короткие видео':
        await bot.send_message(message.from_user.id,
                               'Выберите тему: ',
                               reply_markup=key.get_short_thems_keys())
    elif message.text == 'Ссылки, книги':
        await bot.send_message(message.from_user.id,
                               """Список полезных ресурсов для пентестеров и хакеров

Друзья, представляю вашему вниманию список полезных ресурсов, 
благодаря которым можно существенно повысить свой скилл в различных аспектах тестирования на проникновение
и информационной безопасности:

• Мануалы по взлому:
http://www.ehacking.net/
http://www.securitytube.net/
http://www.hacking-tutorial.com/
https://www.offensive-security.com/
http://breakthesecurity.cysecurity.org/
http://www.spacerogue.net/wordpress/
https://www.youtube.com/user/Hak5Darren
https://www.youtube.com/user/sansinstitute
https://vimeo.com/channels/fullscopesecurity
http://www.kalitutorials.net/2013/08/kali-linux.html
https://www.youtube.com/user/DEFCONConference
https://en.wikibooks.org/wiki/Metasploit/VideoTutorials

• Антивирусы:
http://fuckingscan.me/
http://v2.scan.majyx.net/
http://nodistribute.com/
http://www.file2scan.net/
http://anubis.iseclab.org/
https://anonscanner.com/
http://virusscan.jotti.org/it
https://www.virustotal.com/nl/

• Сервисы для работы с IP:
http://ip-api.com/
http://ipaddress.com/
http://whatstheirip.com/
http://www.whatismyip.com/
http://www.ip2location.com/demo
http://www.my-ip-neighbors.com/
http://freegeoip.net/static/index.html
http://www.ip-adress.com/ipaddresstolocation/

• Проверка анонимности:
https://ipleak.net/
https://www.dnsleaktest.com/
https://diafygi.github.io/webrtc-ips/

• Идентификация фейков:
https://fakena.me/
http://www.fakenamegenerator.com/
http://names.igopaygo.com/people/fake_person""")


@dp.callback_query_handler(lambda c: c.data in other.get_short_groups_for_lambda())
async def obrab_short_vids(call: types.CallbackQuery):
    videos = db.get_short_vidios(call.data[6:])
    if not videos:
        await bot.send_message(call.from_user.id, f'У нас нет коротких видео по теме - {call.data[6:]}: ')
    for vid in videos:
        try:
            await bot.send_message(call.from_user.id, f'Видео по теме - {call.data[6:]}')
            await bot.send_video(call.from_user.id, vid[0])
        except BaseException:
            logging.warning("Что то не так с отправкой короткого видео")


@dp.callback_query_handler(lambda c: c.data in other.get_long_groups_for_lambda())
async def obrab_short_vids(call: types.CallbackQuery):
    videos = db.get_long_vidios(call.data[5:])
    if not videos:
        await bot.send_message(call.from_user.id, f'У нас нет полных лекций по теме - {call.data[5:]}')
    else:
        for vid in videos:
            try:
                await bot.send_message(call.from_user.id, f'Видео по теме - {call.data[5:]}: ')
                await bot.send_video(call.from_user.id, vid[0])
            except BaseException:
                logging.warning("Что то не так с отправкой короткого видео")


@dp.message_handler(commands=['developer'])
async def developer(message: types.Message):
    await bot.send_message(message.from_user.id, 'Содатель данного бота - Бобёр\n'
                                                 'тг - @Georgiy1928\n'
                                                 'дс - Бобёр#1098')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
