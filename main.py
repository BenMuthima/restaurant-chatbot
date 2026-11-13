import string

intents = {
    "restaurant_greetings": {
        "patterns": ["hey", "hello", "hi", "good morning", "good afternoon", "good evening"],
        "responses": "Hello! Welcome to our restaurant. How can I help you today?"
    },

    "restaurant_salamu": {
        "patterns": ["niaje", "habari", "uko aje", "mambo", "vipi", "hujambo"],
        "responses": "Karibu! Naweza kukusaidia aje leo?"
    },

    "restaurant_services": {
        "patterns": ["services", "offer", "what do you have", "menu", "food", "meals", "order", "delivery"],
        "responses": "We offer dine-in, takeaway and delivery. Our menu includes breakfast, lunch, dinner, snacks and drinks."
    },

    "restaurant_huduma": {
        "patterns": ["mko na nini", "mko n nini", "huduma", "chakula", "menyu", "mnauza nini"],
        "responses": "Tuna huduma za kula hapa, kuchukua chakula, na kupelekewa. Tuna kiamsha kinywa, chakula cha mchana, cha jioni, vitafunio na vinywaji."
    },

    "restaurant_location": {
        "patterns": ["location", "located", "where are you", "address", "premises"],
        "responses": "We are located at Kenyatta Avenue, Nakuru, Kenya."
    },

    "restaurant_mahali": {
        "patterns": ["mko wapi", "wapi", "mahali", "anwani"],
        "responses": "Tuko Kenyatta Avenue, Nakuru, Kenya."
    },

    "restaurant_goodbye": {
        "patterns": ["bye", "goodbye", "see you", "thanks", "thank you"],
        "responses": "Goodbye! Thank you for visiting. Have a great day!"
    },

    "restaurant_kuaga": {
        "patterns": ["kwa heri", "tutaonana", "asante", "shukran"],
        "responses": "Kwa heri! Asante kwa kutembelea. Uwe na siku njema!"
    }
}


FALLBACK="Sorry , i didn't undertand that!!"


def get_reply(text):
    text=text.lower().strip()
    user_words=text.translate(str.maketrans("","",string.punctuation))
    for intent in intents.values():
        for w in intent["patterns"]:
            if (" " in w and w in text) or w in user_words.split():
                return intent["responses"]
    return FALLBACK

while True:
    user_input=input("BOT: ")
    if user_input=="q":
        print("BOT:GOODBYE!!")
        break
    print(get_reply(user_input))