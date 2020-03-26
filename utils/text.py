from collections import defaultdict
from hgtk.text import compose, decompose
from string import ascii_lowercase, ascii_uppercase
import numpy as np



jaem = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㄲ', 'ㄸ', 'ㅃ', 'ㅆ', 'ㅉ', 'ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅄ']
moem = ['ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅐ', 'ㅒ', 'ㅔ', 'ㅖ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ']
english = list(ascii_lowercase) + list(ascii_uppercase)
sign = [s for s in ''' `~!@#$%^&*()+-/=_,.?;:'"[]{}<>\|''']

link_list = sign + jaem + moem + english + [str(i) for i in range(10)]
encoding_dict = defaultdict(lambda : 0, {k:code+1 for code, k in enumerate(link_list)}) # 0은 OOV


def encode(text):
    text = decompose(text).replace('ᴥ', '')
    code = [encoding_dict[t] for t in text]
    return code


def len_encode(text, maxlen):
    if isinstance(text, str):
        text = [encode(text)]
    elif isinstance(text, list):
        text = [encode(t) for t in text]
    
    data_list = []
    for t in text:
        if len(t) > maxlen:
            # nplist = np.array(t[:maxlen])
            data_list.append(np.array(t[:maxlen]))
        else:
            t = [0] * (maxlen - len(t)) + t
            # nplist = np.array(t)
            data_list.append(np.array(t))
    
    return np.array(data_list)


if __name__ == "__main__":
    while True:
        s = input()
        enc = len_encode(s, 100)
        print(enc)