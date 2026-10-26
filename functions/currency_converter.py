# Konvertera priset från EUR to SEK

# 1 EURO = 11,14 SEK idag
exchange_rate = 11.14

def convert_to_sek(price_eur, exchange_rate):
    return round(price_eur * exchange_rate, 2)

