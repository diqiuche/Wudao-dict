import JsonReader


class CommandDraw:
    RED_PATTERN = '\033[31m%s\033[0m'
    GREEN_PATTERN = '\033[32m%s\033[0m'
    BLUE_PATTERN = '\033[34m%s\033[0m'
    PEP_PATTERN = '\033[36m%s\033[0m'
    BROWN_PATTERN = '\033[33m%s\033[0m'

    def __init__(self):
        self.reader = JsonReader.JsonReader()

    def draw_text(self, word):
        # Word
        print(word['word'])
        # pronunciation
        try:
            print(u'英 ' + self.PEP_PATTERN % word['pronunciation']['英'], end='  ')
            print(u'美 ' + self.PEP_PATTERN % word['pronunciation']['美'])
        except KeyError:
            print(u'英 ' + self.PEP_PATTERN % word['pronunciation'][''])
        # paraphrase
        for v in word['paraphrase']:
            print(self.BLUE_PATTERN % v)
        # short desc
        print(self.RED_PATTERN % word['rank'], end='  ')
        print(self.RED_PATTERN % word['pattern'])
        # sentence
        count = 1
        for v in word['sentence']:
            if v[1].startswith('['):
                print(str(count) + '. ' + self.GREEN_PATTERN % (v[1]), end=' ')
            else:
                print(str(count) + '. ' + self.GREEN_PATTERN % ('[' + v[1] + ']'), end=' ')
            print(v[0])
            for sv in v[2]:
                print(self.GREEN_PATTERN % u'例: ' + self.BROWN_PATTERN % (sv[0] + sv[1]))
            count += 1