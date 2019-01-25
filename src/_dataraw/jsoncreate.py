import json
cards = []
with open("tarotpdf.txt", "r") as f:
    card = []
    cardNumber = -1
    lines = f.readlines()
    nextIsCardName = False
    nextIsCardDesc = False
    nextIsCardTPos = False
    nextIsCardRPos = False
    majorAracanaSecondName = False
    res = ''
    for line in lines:
        if line[0] == '-':  # 카드 넘버 체크
            card = []
            cardNumber += 1
            nextIsCardName = True
            card.append(cardNumber)
            continue
        if nextIsCardName:
            res += line
            if cardNumber > 21:
                nextIsCardName = False
                nextIsCardDesc = True
                res = res.replace('\n', '')
                if ')' in res:
                    res = res[3:].strip()
                card.append(res)
                res = ''
                continue
            else:
                if majorAracanaSecondName == False:
                    majorAracanaSecondName = True
                else:
                    majorAracanaSecondName = False
                    nextIsCardName = False
                    nextIsCardDesc = True
                    res = res.replace('\n', '')
                    res = res[3:].strip()
                    card.append(res)
                    res = ''
                    continue
        if nextIsCardDesc:
            if '정위치' in line:
                nextIsCardDesc = False
                nextIsCardTPos = True
                res = res.strip()
                card.append(res)
                res = ''
                continue
            else:
                line = line.replace('\n', '')
                res = res + ' ' + line
        if nextIsCardTPos:
            if '역위치' in line:
                nextIsCardTPos = False
                nextIsCardRPos = True
                res = res.strip()
                card.append(res)
                res = ''
                continue
            else:
                line = line.replace('\n', '')
                res = res + ' ' + line
        if nextIsCardRPos:
            if line == "\n":
                nextIsCardRPos = False
                res = res.strip()
                card.append(res)
                res = ''
                keys = ['number', 'name', 'description', 'true', 'reverse']
                values = card
                dictzip = zip(keys,values)
                card = dict(dictzip)
                cards.append(card)
                card = []
                continue
            else:
                line = line.replace('\n', '')
                res = res + ' ' + line
    with open('tarotcards.json', 'w', encoding='utf8') as fp:
        json.dump(cards, fp, ensure_ascii=False)
print(cards)
with open('tarotcards.json', 'r', encoding='utf8') as f:
    lines = f.readlines()
    datanumber = 0
    for line in lines:
        aline = line
        bline = ''
        formeridx = 0
        for idx in range(len(aline)):
            if '{' == aline[idx]:
                bline += aline[formeridx:idx]
                bline = bline + '{0} : {{'.format(datanumber)
                datanumber += 1
                formeridx = idx+1
        bline += aline[formeridx:]
        if '[' in bline:
            bline = bline.replace('[', '{')
        if ']' in bline:
            bline = bline.replace(']', '}')
        res += bline
cards = eval(res)
print(cards)
with open('tarotcards.json', 'w', encoding='utf8') as fp:
    json.dump(cards, fp, ensure_ascii=False)