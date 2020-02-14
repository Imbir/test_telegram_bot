import unittest
import telegram
from telegram_bot.constants import ACCESS_TOKEN


class BotTestCase(unittest.TestCase):

    def test_bot_info(self):
        bot_info = telegram.Bot(ACCESS_TOKEN).get_me()
        self.assertEqual(bot_info.first_name, 'TensorTest')
        self.assertEqual(bot_info.is_bot, True)
        self.assertEqual(bot_info.username, 'tensor_test_task_bot')


if __name__ == '__main__':
    unittest.main()
