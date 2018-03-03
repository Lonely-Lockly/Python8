from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
# Импортируем нужные компоненты

def calculator(bot, update):
    case = update.message.text     
    case = case.replace('/calc ', '')
    case = case.replace('=', '')
    print(case)

    nums = ['+', '-', '/', '*']

    for n in nums:
    
        if n in case: 
            case = case.split()
            num_1 = int(case)
            num_2 = int(case)
            print(num_1)
            print(num_2)

            answer = ('{} + {} = '.format(num_1, num_2))
            answer = num_1 + num_2
            print(answer)
        
            answer = ('{} - {} = '.format(num_1, num_2))
            answer = num_1 - num_2

            answer = ('{} * {} = '.format(num_1, num_2))
            answer = num_1 * num_2

            try:
                answer = ('{} / {} = '.format(num_1, num_2))
                answer = float(num_1 / num_2)
            except ZeroDivisionError:
                update.message.reply_text('Division by zero has no meaning! Try another number!')

        else:
            update.message.reply_text('Make sure you enter a case with one of the operations: "+", "-", "*", "/"')

    update.message.reply_text(answer)

# Функция, которая соединяется с платформой Telegram, "тело" бота

def main():
    updater = Updater("498747935:AAHANRICU65KYR1E-tcXjpMUMqrj47whGR8")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('calc', calculator))
    updater.start_polling()
    updater.idle()

# Вызываем функцию - эта строчка запускает бота
main()
