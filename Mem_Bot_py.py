
from typing import Text
import vk_api, random, json
from vk_api import longpoll
from vk_api import upload
from vk_api import keyboard
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

# криптобот токен TOKEN = 'b67a3fc0f8b1967462ccb0286df9ffba68698cf3e9e6354d53ef2bef6ff1147e68bf067c1586083ca662a'
TOKEN = "28853c67a17b8fa800d88eec13666ee34392a3c66d220377b40a41f19540afe8673cd6fa3919864fdfd58"
# Вак бот токен TOKEN = '1e943b35a07460af3cfc0dfc2e64e3c4325b50af16bdd0c21975532a2bcd1e76c796168f2bd3b926ce7d4'

music = ['audio534311809_456240505']

video = ["video-527771830_456239259", "video-194273774_456239017", 
        "video-194273774_456239018", "video-533909106_456239947",
        "video534311809_456239058", "video-187227252_456249330",
        "video-207121328_456239017", "video-56263398_456287681",
        "video-174825465_456239602","video-162181333_456239860",
        "video-198797033_456240612", "video-190340814_456256486",
        "video-190340814_456256478", "video-99872432_456273153",
        "video-99872432_456273152", "video-99872432_456273149",
        "video-99872432_456256881", "video-99872432_456256080",
        "video-99872432_456260081", "video618650795_456239109",
        "video-124668503_456281547", "video-143968551_456240702",
        "video-12353330_456264660", "video-190340814_456256523"
        ]

joke = ["Шли как то 100 негров по пусыне и нашли джина. Джин сказал что исполнит лишь по одному желанию на каждого. 99 негров загадали стать белыми, а 100 умирая от смеха загадал чтобы они опять стали черными",
        "Заходит значит Змей Горынычь в бар. Одна голова\n - Что то здесь жарко\n - Пасть закрой...",
        "Что скзал Дед Мороз когда увидел мужика который хочет повеситься?\n- На стульчик встал, хоть стишок расскажи)",
        "- Есть хорошая и плохая новость, с какой начать?\n- Ну давай с хорошей\n- Дед храпеть перестал...",
        "Сидят как то 2 шизофреника на рельсах, а к ним 5-ый подсаживается", 
        "Только профессиональный диджей может одновременно гладить двух собак",
        "Гитлер застрелился...\n Увидев счетчик за газ", 
        "Недавно видел самую вежливую драку. 4 пацана одного пинали. Один этот чихает и все такие\n- Будь здоров",
        "Что красное и вредно для зубов?\n - Кирпич",
        "Девиз хорошего снайпера:\n- В одно ухо влетело, из другого вылетело", 
        "Куда едет гей-ковбой?\n На Dickий запад",
        "Идет как то весной Штирлец по улице и видит мужика в фуфайке и на лыжах\n Фуфлыжник, подумал Штирлец",
        "Вышли как то из бара подыпившие Мюллер и Штирлец.\n Мюллер:\n - Пойдем может девченок снимем?)\nШтирлец:\n- Да не, пусть еще немного повисят",
        "— Я боюсь прыгать — вдруг парашют не раскроется?\n— Еще никто никогда не жаловался, что у него не раскрылся парашют.",
        "— Будешь выходить — труп вынеси!\n — Может быть, мусор?\n— Может — мусор, может — сантехник, бог его знает…",
        "— Моя девушка порвала со мной, и я забрал ее кресло-каталку. Угадайте, кто приполз ко мне на коленях?",
        "Если бы моя бабушка знала, сколько денег я сэкономил на ее похоронах, то она бы перевернулась в канаве.",
        "— Кот умер год назад. Так я до сих пор замедляю шаг в коридоре, там, где он любил лежать, чтобы не споткнуться об него в темноте.\n— Может, пора его похоронить?",
        "Однорукий человек заплакал, увидев магазин «секонд-хенд».",
        "— Не, я через балкон не полезу, у меня клаустрофобия!\n— Клаустрофобия — это боязнь замкнутого пространства. Где ты тут видишь замкнутое пространство?\n - В гробу! В гробу замкнутое пространство!",
        "— А у геймеров бывают профессиональные заболевания?\n— Ага — ГЕЙморрой … ",
        "— Как называется человек, у которого нет левой руки, левой ноги, левого глаза и левого уха?\n — All right.",
        "Курить по 3 пачки в день — это трудный путь, но разве нам нужны легкие?"
        ]

photo = ["photo-194273774_457239039"]

mems = ["photo-194273774_457239040", "photo-194273774_457239041",
        "photo-194273774_457239042", "photo-194273774_457239043",
        "photo-194273774_457239044", "photo-194273774_457239045",
        "photo-194273774_457239046", "photo-194273774_457239054",
        "photo-194273774_457239047", "photo-200012145_457250481",
        "photo-200012145_457250470", "photo-169204537_457293431",
        "photo-168343603_457279642", "photo-169204537_457293435",
        "photo-169204537_457293429", "photo-547924735_457242110",
        "photo-547924735_457240965", "photo-547924735_457240951",
        "photo-194273774_457239061", "photo-190803277_457307249",
        "photo547924735_457242325", "photo547924735_457242328",
        "photo-194273774_457239084", "photo-194273774_457239085",
        "photo-190340814_457281225", "photo-190340814_457281224",
        "photo-169204537_457293896", "photo-171776202_457250411",
        "photo618650795_457240359", "photo618650795_457240358",
        "photo618650795_457240357", "photo618650795_457240356",
        "photo618650795_457240355", "photo618650795_457240353",
        "photo-179997490_457359393", "photo-187177136_457312339",
        "photo-190803277_457308592", "photo-12353330_459056136"
        ]

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_session)
Vk = vk_session.get_api()

def create_keyboard():
    keyboard = VkKeyboard(inline=False)
    keyboard.add_button('Мем', VkKeyboardColor.POSITIVE)
    keyboard.add_button('Видео', VkKeyboardColor.POSITIVE)
    keyboard.add_button('Шутка', VkKeyboardColor.POSITIVE)
    #keyboard.add_button('Музыка', VkKeyboardColor.POSITIVE)  
    return keyboard.get_keyboard()

def sender(id, text):
    global Vk
    Vk.messages.send(
        random_id=get_random_id(),
        user_id=id,
        message=text,
        keyboard=create_keyboard())

def sender_photo(id, text, attachment):
    Vk.messages.send(
        random_id=get_random_id(),
        user_id=id,
        message=text,
        attachment=photo,
        keyboard=create_keyboard())

def sender_photo_1(id, text):
    Vk.messages.send(
        random_id=get_random_id(),
        user_id=id,
        message=text,
        attachment=random.choice(mems),
        keyboard=create_keyboard())

def sender_video(id, text):
    Vk.messages.send(
        random_id=get_random_id(),
        user_id=id,
        message=text,
        attachment=random.choice(video),
        keyboard=create_keyboard())

def sender_joke(id, text):
    Vk.messages.send(
        random_id = get_random_id(),
        user_id = id,
        text = random.choice(joke),
        message =text,
        keyboard = create_keyboard())

#def sender_music(id, text):
#    Vk.messages.send(
#        random_id = get_random_id(),
#         user_id = id,
#        message = text,
#        attachment = music,
#        keyboard = create_keyboard())
    
def work_bot():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                msg = event.text.lower()
                id = event.user_id
                    #Параметры для ответа
                if msg == 'начать':
                    sender(id, 'привет, я Мем Бот) Чтобы получить пикчу напиши \"мем\". Чтобы получить видео напиши \"видео\"') 
                elif msg == 'мем':
                    sender_photo_1(id,'Вот твой мем)')
                elif msg == 'мем':
                    keyboard = VkKeyboard(inline = True)
                    keyboard.add_button("Кнопка") 
                    sender(id, "Привет")
                elif msg == 'видео':
                    sender_video(id, 'video') 
                elif msg == 'шутка':
                    sender_joke(id, random.choice(joke))
                #elif msg == 'музыка':
                #    sender_music(id, ' ')
                else:
                    sender_photo(id, ' Я тебя не понимаю😿' + photo)

if __name__ == '__main__':
    work_bot()  