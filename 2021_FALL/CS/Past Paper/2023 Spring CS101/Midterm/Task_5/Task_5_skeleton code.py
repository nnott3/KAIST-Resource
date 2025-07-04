from cs1media import *
from problem3_support import get_example


def inpaint(img_org, img_r, img_g, img_b):
    w, h = img_org.size()
    img_i = create_picture(w, h)
    for y in range(h):
        for x in range(w):
            img_i.set(x, y, img_org.get(x, y))

    #############################
    # Implement your logic here #
    #############################

    return img_i

def main():
    #######################################
    # Uncomment the case you want to test #
    #######################################

    # filename, mode, num = 'images/ironman.jpg',   'r',    1
    # filename, mode, num = 'images/minion.jpg',    'r',    2
    # filename, mode, num = 'images/neobjuggi.png', 'r',    3
    # filename, mode, num = 'images/pikachu.jpg',   'r',    4
    # filename, mode, num = 'images/sherlock.jpg',  'r',    5
    # filename, mode, num = 'images/ironman.jpg',   'g',    6
    # filename, mode, num = 'images/minion.jpg',    'g',    7
    # filename, mode, num = 'images/neobjuggi.png', 'g',    8
    # filename, mode, num = 'images/pikachu.jpg',   'g',    9
    # filename, mode, num = 'images/sherlock.jpg',  'g',   10
    # filename, mode, num = 'images/ironman.jpg',   'b',   11
    # filename, mode, num = 'images/minion.jpg',    'b',   12
    # filename, mode, num = 'images/neobjuggi.png', 'b',   13
    # filename, mode, num = 'images/pikachu.jpg',   'b',   14
    # filename, mode, num = 'images/sherlock.jpg',  'b',   15
    # filename, mode, num = 'images/ironman.jpg',   'rgb', 16
    # filename, mode, num = 'images/minion.jpg',    'rgb', 17
    # filename, mode, num = 'images/neobjuggi.png', 'rgb', 18
    filename, mode, num = 'images/pikachu.jpg',   'rgb', 19
    # filename, mode, num = 'images/sherlock.jpg',  'rgb', 20

    img_org, img_r, img_g, img_b = get_example(filename, mode, num)
    img_r.show()
    img_g.show()
    img_b.show()
    img_org.show()
    img_i = inpaint(img_org, img_r, img_g, img_b)
    img_i.show()

if __name__ == '__main__':
    main()