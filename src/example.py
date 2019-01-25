import tarotkr
from PIL import Image
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def showCardDeck():
    carddeck = [
        '┌─┌─────────┐',
        '│|│┏━━━^━━━┓│',
        '│|│┃░░░░░░░┃│',
        '│|│┃░░░░░░░┃│',
        '│|│<░░░░░░░>│',
        '│|│┃░░░░░░░┃│',
        '│|│┃░░░░░░░┃│',
        '│|│┗━━━v━━━┛│',
        '└─└─────────┘'
    ]
    for line in carddeck:
        print(line)

def showCardback(num=1):
    cardback = [
        '┌─────────┐',
        '│┏━━━^━━━┓│',
        '│┃░░░░░░░┃│',
        '│┃░░░░░░░┃│',
        '│<░░░░░░░>│',
        '│┃░░░░░░░┃│',
        '│┃░░░░░░░┃│',
        '│┗━━━v━━━┛│',
        '└─────────┘'
    ]
    line = []
    for cb in cardback:
        subline = ''
        for _ in range(num):
            subline += cb + ' '
        line.append(subline)
    for sl in line:
        print(sl)

def talk(string):
    print(string)
    while True:
        chk = input()
        if chk == '':
            return

def enterwait():
    while True:
        chk = input()
        if chk == '':
            return
class Spread:

    def threeCard(self):
        drawedlist = []
        tdeck = tarotkr.TarotDeck()
        tdeck.shuffle()

        showCardDeck()
        talk_src = '<점집 할머니>\n 점을 보러온 겐가? 카드를 세 장 뽑아보시게.'
        talk(talk_src)
        cls()

        showCardback(1)
        drawedlist.append(tdeck.draw())
        talk_src = '<점집 할머니>\n 첫 장은 과거'
        talk(talk_src)
        cls()

        showCardback(2)
        drawedlist.append(tdeck.draw())
        talk_src = '<점집 할머니>\n 다음은 현재'
        talk(talk_src)
        cls()

        showCardback(3)
        drawedlist.append(tdeck.draw())
        talk_src = '<점집 할머니>\n 마지막은 미래를 말해주지 흐흐...'
        talk(talk_src)
        cls()

        showCardback(2)
        cardname = tdeck.cardDesc(drawedlist[0])
        talk_src = '<점집 할머니>\n 첫 장은 ' + cardname + '를 뽑았군. 자네의 과거를 말해주지\n'
        talk(talk_src)
        cls()

        showCardback(1)
        cardname = tdeck.cardDesc(drawedlist[1])
        talk_src = '<점집 할머니>\n 그 다음 장은 ' + cardname + '를 뽑았군. 현재의 자네를 보여준다네.\n'
        talk(talk_src)
        cls()

        showCardDeck()
        cardname = tdeck.cardDesc(drawedlist[2])
        talk_src = '<점집 할머니>\n 마지막은 ' + cardname + '를 뽑았군. 미래엔 이런 일이 있을 걸세.\n'
        talk(talk_src)
        cls()

        while True:
            showCardDeck()
            talk_src = '<점집 할머니>\n 카드에 대한 설명이 궁금한가?\n(예, 아니오로 대답)'
            print(talk_src)
            answer = input()
            cls()
            if answer == '예':
                break
            elif answer == '아니오':
                exit()

        showCardDeck()
        talk_src = '<점집 할머니>\n 과거는 카드가 이렇게 말해주는군. \n' + tdeck.cardDesc(drawedlist[0], 'detail')
        print(talk_src)
        img = Image.open(tdeck.cardImg(drawedlist[0], 'big'))
        img.show()
        enterwait()
        cls()

        showCardDeck()
        talk_src = '<점집 할머니>\n 현재는 카드가 이렇게 말해주는군. \n' + tdeck.cardDesc(drawedlist[1], 'detail')
        print(talk_src)
        img = Image.open(tdeck.cardImg(drawedlist[1], 'big'))
        img.show()
        enterwait()
        cls()


        showCardDeck()
        talk_src = '<점집 할머니>\n 미래는 카드가 이렇게 말해주는군. \n' + tdeck.cardDesc(drawedlist[2], 'detail')
        print(talk_src)
        img = Image.open(tdeck.cardImg(drawedlist[2], 'big'))
        img.show()
        enterwait()
        cls()

        showCardDeck()
        talk_src = '<점집 할머니>\n 즐거웠는가? 크크크...잘 있게나'
        print(talk_src)
        enterwait()

sp = Spread()
sp.threeCard()


