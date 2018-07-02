from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *

#janome初期化
#フィルタの初期化
tokenizer = Tokenizer()
char_filters=[UnicodeNormalizeCharFilter()]
token_filters=[CompoundNounFilter(),POSStopFilter("助詞"),LowerCaseFilter()]
a = Analyzer(char_filters,tokenizer,token_filters)

#ツイッターデータ処理

for token in a.analyze("今日はとても暑いけれども虹がとても綺麗である．"):
    print(token)
    if token.surface == "虹":
        print("虹をはっけん")
