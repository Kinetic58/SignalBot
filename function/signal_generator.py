import random

CURRENCY_PAIRS = [
    "AED/CNY", "EUR/HUF", "GBP/AUD",
    "AUD/CHF", "USD/JPY", "EUR/USD"
]

OUTCOMES = ["ПОКУПКА", "ПРОДАЖА"]

def generate_signal():
    pair = random.choice(CURRENCY_PAIRS)
    outcome = random.choice(OUTCOMES)
    return f"""
📊 ВАЛЮТНАЯ ПАРА - {pair}
⏰ Время : 5 минут
🔍 Исход : {outcome}
"""
