from cs1graphics import *
#import random


def convert_idx_rev_to_prop(index, reversal):
    prop = {}
    ########## MODIFY HERE ##########
    prop['arcana'] = 'major'
    prop['num'] = 0
    prop['reversal'] = False
    #################################
    return prop


def spread_cards(canvas, cards, spread_style):
    ########## MODIFY HERE ##########
    card_img = cards[0][0]
    canvas.add(card_img)
    card_img.moveTo(300, 300)
    card_img.rotate(180)
    #################################


def select_cards(spread_style):
    cards = []
    draws = [31, 2, 56, 43, 22] # Fixed selection for your easy verification
    reversals = [True, False, False, True, False] # Fixed selection for your easy verification
    # draws = random.sample(range(78), len(spread_style))
    # reversals = [random.choice((True, False)) for i in range(len(spread_style))]
    for i in range(len(spread_style)):
        prop = convert_idx_rev_to_prop(draws[i], reversals[i])
        img = Image('images/card_' + prop['arcana'] + '_' + str(prop['num']) + '.jpg')
        cards.append((img, prop))
    return cards


def draw_background():
    bg_img = Image('images/background.jpg')
    bg_img.moveTo(288, 375)
    canvas.add(bg_img)


if __name__ == '__main__':
    spread_style = [{'coordinate': (100, 375, 0), 'question': '1. Who am I right now?'},\
    {'coordinate': (200, 375, 0), 'question': '2. Am I on the right path?'},\
    {'coordinate': (300, 375, 0), 'question': '3. What\'s the main obstacle standing in my way?'},\
    {'coordinate': (400, 375, 0), 'question': '4. What circumstances are in my favor and helping me out?'},\
    {'coordinate': (500, 375, 0), 'question': '5. How can I make progress and move forward in my life?'}]
    canvas = Canvas(576, 750, 'black')
    draw_background()
    cards = select_cards(spread_style)
    spread_cards(canvas, cards, spread_style)
