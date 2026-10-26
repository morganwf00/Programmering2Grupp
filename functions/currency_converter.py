# Konvertera priset från EUR to SEK
def convert_to_sek(price_eur, exchange_rate):
    return round(price_eur * exchange_rate, 2)

