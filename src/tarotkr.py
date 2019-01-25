import os
import json
import random

file_dir = os.path.dirname(os.path.abspath(__file__))

with open(file_dir+'\\tarotcards.json', encoding='utf8') as f:
    tarotdata = json.load(f)

class TarotDeck:
    cards = [] # { 번호 'number', 이름 'name', 설명 'description, 정위치 'true', 역위치 'reverse' }
    lastdraw = [0, 'T']

    def __init__(self, limit=True):
        if limit == True: # True일 경우 메이저 아르카나 22장, 아닐 경우 마이너 아르카나까지 78장을 사용
            self.cards = [[x, 'T'] for x in range(22)]
        else:
            self.cards = [[x, 'T'] for x in range(78)]
        return

    def _readCard(self, card):
        pos = '정' if card[1] == 'T' else '역'
        name = tarotdata[str(card[0])]['name']
        for idx in range(len(name)):
            if name[idx] == '/':
                name = name[:idx].strip()
                break
        return [name, pos]

    def _readCardDesc(self, card):
        return tarotdata[str(card[0])]['description']

    def _readCardTrue(self, card):
        return tarotdata[str(card[0])]['true']

    def _readCardReverse(self, card):
        return tarotdata[str(card[0])]['reverse']

    def draw(self):
        if self.cards:
            self.lastdraw = self.cards.pop()
            return self.lastdraw
        else:
            return '오류: 남아있는 덱이 없습니다.'

    def shuffle(self):
        random.shuffle(self.cards)
        for idx in range(len(self.cards)):
            rawcard = self.cards[idx][0]
            trueOrReverse = random.choice(['T', 'R'])
            self.cards[idx] = [rawcard, trueOrReverse]

    #nameonly 이름만, simple 간단히, detail 자세히. 옵션에 따라 해당 설명을 반환
    def cardDesc(self, card, option='nameonly'):
        res = ''
        res += self._readCard(card)[0]
        if option == 'nameonly':
            res += ' <정위치>' if card[1] == 'T' else ' <역위치>'
        else:
            res += '\n'
            if option == 'simple':
                { }
            elif option == 'detail':
                res += self._readCardDesc(card) + '\n'
            if card[1] == 'T':
                res += '정위치: ' + self._readCardTrue(card)
            elif card[1] == 'R':
                res += '역위치: ' + self._readCardReverse(card)
        return res

    #size: small 작은 이미지 주소 반환, big 큰 이미지 주소 반환, showback 뒷면 주소 반환
    def cardImg(self, card, size='small', showback=False):
        img_dir = file_dir+'\\tarotimg\\'
        imgIndex = '[{0:02d}]'.format(card[0])
        if size == 'big':
            img_dir += 'big\\'
        if showback:
            for fname in os.listdir(img_dir):
                if 'tarotback' in fname:
                    fpath = img_dir + fname
                    return(fpath)
        else:
            if card[1] == 'R':
                img_dir += 'rv\\'
            for fname in os.listdir(img_dir):
                if imgIndex in fname:
                    fpath = img_dir + fname
                    return(fpath)

#option: desc 상세, tpos 정위치 설명, rpos 역위치 설명
#imgpath: [True, 'small'] 작은 이미지 주소 반환, [True, 'big'] 큰 이미지 주소 반환
def tarotDetail(cardname, option='desc', imgpath=False):
    tarotob = ''
    cardindex = ''
    res = ''
    retlist = []
    for idx in range(0, 78):
        if cardname in tarotdata[str(idx)]['name']:
            tarotob = tarotdata[str(idx)]
            cardindex = idx
            break
    if tarotob:
        if option == 'desc':
            res = '{}\n{}\n정위치: {}\n역위치: {}'.format(tarotob['name'], tarotob['description'], tarotob['true'], tarotob['reverse'])
        elif option == 'tpos':
            res = '{}\n정위치: {}'.format(tarotob['name'], tarotob['true'])
        elif option == 'rpos':
            res = '{}\n역위치: {}'.format(tarotob['name'], tarotob['reverse'])
        else:
            return '오류: 올바른 option 인자값을 넣어주세요.'
        retlist.append(res)
        if imgpath == True:
            ipath = _cardImg([idx, 'T'])
            retlist.append(ipath)
        return retlist
    else:
        return '오류: 카드 이름을 확인해주세요.'
        
def _cardImg(card):
    img_dir = file_dir+'\\tarotimg\\big\\'
    imgIndex = '[{0:02d}]'.format(card[0])
    if card[1] == 'R':
        img_dir += 'rv\\'
    for fname in os.listdir(img_dir):
        if imgIndex in fname:
            fpath = img_dir + fname
            return(fpath)