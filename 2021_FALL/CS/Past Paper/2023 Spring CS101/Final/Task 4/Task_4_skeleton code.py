from cs1graphics import *
import random

img_path = './images/'

arcana_names = ['major', 'cups', 'pentacles', 'swords', 'wands']
face_names_major = ['The Fool', 'The Magician', 'The High Priestess', 'The Empress', 'The Emperor', 'The Hierophant', 'The Lovers', 'The Chariot', 'Strength', 'The Hermit', 'The Wheel of Fortune', 'Justice', 'The Hanged Man', 'Death', 'Temperance', 'The Devil', 'The Tower', 'The Star', 'The Moon', 'The Sun', 'Judgement', 'The World']
face_names_minor = ['', 'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Page', 'Knight', 'Queen', 'King']

current_text_written = 0

def read_cheat_table(cheat_table):
    # args cheat_table (dict of lists of tuples)
    """
    Read the .csv files and fill the cheat_table,
    following the structural diagram in HW3 Description, strictly.
    No typo in dict keys will be accepted.
    We recommend you to take a look at the formats of the .csv files,
    before you getting into implementation.
    If you want, you may use the Python csv module.
    """
    ######## IMPLEMENT HERE ########
    f = open('major.csv')
    print(f.readlines())
    f.close()
    ################################


class Card:
    """
    Initialize the Card class
    following the parameters into correspondent attributes.
    Attribute 'reversal' should be initialized as False.
    """
    def __init__(self, arcana, face, interpret, image):
        # args arcana (string)
        # args face (string)
        # args interpret (tuple of string)
        # args image (cs1graphics image object)
        ######## IMPLEMENT HERE ########
        pass
        ################################


def create_deck(cheat_table):
    # arg cheat_table (dict of lists of tuples)
    # Return deck (list of Cards) : property + interpret text
    """
    Create a list("deck") of all 78 cards and return the list.
    The list 'deck' have to include Card objects.
    A Card is represented by an object with five attributes:
    the arcana, the face, the interpret,
    the reversal, and the image object.
    """
    deck = []
    ######## IMPLEMENT HERE ########
    image = Image(img_path + 'major_The World.jpg')
    for i in range(20):
        deck.append(Card('major', 'The World', 'sample text', image))
    ################################
    return deck



def generate_fortune_text(card):
    # args card (Card object) : card to be interpreted
    # Return fortune_text (string) : interpretation text
    """
    Return a nice string to interpret card
    (such as "Minor Arcana - Ten of cups: waste, broken relationships,
    quarrel" or "Major Arcana - The High Priestess: knowledge, wisdom,
    learning, intuition, impatience, virtue, purity")
    """
    ######## IMPLEMENT HERE ########
    fortune_text = 'sample text'
    ################################
    return fortune_text


def draw_text(canvas, question, interpret):
    global current_text_written
    if len(interpret) > 60:
        interpret = interpret[:60] + "\n  " + interpret[60:]
        if len(interpret) > 125:
            interpret = interpret[:125] + "\n  " + interpret[125:]
    text = question + '\n' + interpret
    text_obj = Text(text, 10)
    text_obj.adjustReference(-text_obj.getDimensions()[0]//2, 0)
    canvas.add(text_obj)
    text_obj.setFontColor((255, 255, 0))
    text_obj.moveTo(600, (current_text_written + 1) * 65)
    current_text_written += 1


def spread_cards(canvas, cards, spread_style):
    for i in range(len(spread_style)):
        coordinate = spread_style[i]['coordinate']
        try: card_img = cards[i].image
        except: card_img = Image(img_path + 'major_The World.jpg')
        canvas.add(card_img)
        card_img.moveTo(coordinate[0], coordinate[1])
        try:
            if cards[i].reversal:
                card_img.rotate(180)
        except Exception as ex:
            print(ex)
        card_img.rotate(coordinate[2])


def select_cards(deck, spread_style):
    cards = random.sample(deck, len(spread_style))
    for card in cards:
        if random.choice((True, False)):
            card.reversal = True
    return cards


def draw_background():
    bg_img = Image('images/background.jpg')
    bg_img.moveTo(288, 375)
    canvas.add(bg_img)


if __name__ == '__main__':
    cheat_table = {}
    read_cheat_table(cheat_table)
    deck = create_deck(cheat_table)
    canvas = Canvas(1020, 750, 'black')
    draw_background()
    spread_style = [{'coordinate': (220, 350, 0), 'question': '1. Where am I now?'},\
    {'coordinate': (220, 350, -90), 'question': '2. What are Potential or Challenges?'},\
    {'coordinate': (220, 525, 0), 'question': '3. Where should I directly focus?'},\
    {'coordinate': (80, 350, 0), 'question': '4. Looking at my past...'},\
    {'coordinate': (220, 175, 0), 'question': '5. What is my unique strength?'},\
    {'coordinate': (360, 350, 0), 'question': '6. Glancing at the near future...'},\
    {'coordinate': (500, 590, 0), 'question': '7. How should I approach?'},\
    {'coordinate': (500, 430, 0), 'question': '8. What do I need to know?'},\
    {'coordinate': (500, 270, 0), 'question': '9. What are my hopes or fears?'},\
    {'coordinate': (500, 110, 0), 'question': '10. What will be the potential outcome?'}]
    cards = select_cards(deck, spread_style)
    spread_cards(canvas, cards, spread_style)
    for i in range(len(spread_style)):
        draw_text(canvas, spread_style[i]['question'], generate_fortune_text(cards[i]))