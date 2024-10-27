import telebot
from telebot import types
import pytest
from unittest.mock import patch, MagicMock
import json
from bot import weather, answer, f
API = 'abcb934124c8947e0111042c44372700'
bot = telebot.TeleBot('7587930044:AAEbrcOhPdJaleOkoQTSH5D_Uf238Bbd7bY')
@pytest.fixture
def mock_bot():
#Создаем мок для бота
    return MagicMock()
@pytest.fixture
def request_weather():
    with patch('requests.get') as mock:
        #преобразуем в строку
        mock.return_value.text = json.dumps({'main': {'temp': 20}})
        yield mock
def test_weather(mock_bot, request_weather):
    message = types.Message()
    message.text = '/weather'
    with patch('telebot.TeleBot.reply_to', new = mock_bot.reply_to):
        weather(message)
        mock_bot.reply_to.assert_called_once_with(message, 'сейчас погода в городе Паттайя: 25')
def test_answer(mock_bot):
    message = types.Message()
    message.text = 'Привет'
    with patch('telebot.TeleBot.reply_to', new = mock_bot.reply_to):
        answer(message)
        mock_bot.reply_to.assert_called_once()