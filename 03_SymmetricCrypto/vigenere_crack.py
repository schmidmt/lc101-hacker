#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Vigenere Cracking Tools"""

from collections import deque, defaultdict
from itertools import combinations
from fractions import gcd
from pprint import pprint
import string


ENGLISH_DIST = [
    0.08167,
    0.01492,
    0.02782,
    0.04253,
    0.12702,
    0.02228,
    0.02015,
    0.06094,
    0.06966,
    0.00153,
    0.00772,
    0.04025,
    0.02406,
    0.06749,
    0.07507,
    0.01929,
    0.00095,
    0.05987,
    0.06327,
    0.09056,
    0.02758,
    0.00978,
    0.02360,
    0.00150,
    0.01974,
    0.00074,
]


def chi_square(sample):
    """Determined the chi squared fit for the given sample"""
    chi = 0
    for i in range(26):
        chi += ((ENGLISH_DIST[i] - sample[i]) ** 2) / (ENGLISH_DIST[i] ** 2)
    return chi


def keylen_probabilities(enc_text, n=3):
    """Determine the probability key lengths. 
    """
    buff = deque(maxlen=n)
    buff.extend(enc_text[:n])
    locations = defaultdict(list)
    for i in range(len(enc_text) - n):
        buff.append(enc_text[i])
        gram = tuple(buff)
        locations[gram].append(i)

    diffs = {}
    for gram, locs in locations.items():
        if len(locs) <= 1:
            continue
        diffs[gram] = [abs(a - b) for a, b in combinations(locs, 2)]

    # return diffs
    gcds = defaultdict(int)
    total = 0
    pprint(diffs)
    for a, b in combinations((y for x in diffs.values() for y in x), 2):
        gcds[gcd(a, b)] += 1
        total += 1

    return {x: y / total for x, y in gcds.items()}



def main():
    text = """
    Ztvz kkhqgvgtv dp icdigtv xq ifk yii uu idkvdqoce plj qkcboce tjkrrxdlor stqypekh iwvxagaje aucqohroce dd pjvwyhtror gcb csstpor iwyxpaztpy htrctct rcd ug sdpk sytpy ml kuqgrt vwmttq domcj bkkgitq (cv bkhizdn rmsesztpy) ug vdpzpzrt jttorcy (ke zpzrtr rmsesztpy mx qsppzefuccy) Lfoac icdi stqypekh ggc jqapjrn ytlz mbtp p vwmtt ttrcdpq jjc im ifk auctkgekcak zkiuktl ifk rkacidksjloryzxmt yts hgmgsaghroce xljjqzggkh oc zwc 2000q rkmr bcyhymtq bye yrhm qc hcti bxy p ipzrt ttrcdpq mx Juryr Yxty CczlmxzZwc icxb uggmxlgaje pkucxgcj ru kkhqgvcy qkcr jqoce ifk Qndpz Kkhqgvc Hcxkgit (HKY) Xr wyy exdut zknmts gannplabcxxa icdi zd ocarjbk kaarobcjxy bcyhymtq (itdut yy KSH) rmtiyocgtv jxeoiyr gspekh kgjtmy gcb hmacb rmticti pq lcra gh oscuvpgbq zlull pq tkuyg (fgene dgrcy yts uifkg ormth)Pq dd 2017 icdi stqypekh ggc jqks hn edszw gcb pbaary dug vtpydlga uysxje yts ydaopj esxemytq plj gt zahgttqy mdtkglstlz yts tdl-vmbtptbctiyr mxvytxxgigucq umx aubkacgiprodl qczlckc idjrtymjcy Gh cxrn cspgrxlm oc zwc 2010q rnt ytljxlm ml qndpz gtumxbyr kkhqgvcy fgh htaubc pl paitnztb eyxi uu sple aaaragcy Zwgy kgzcy rkmroce p wjgiz gcb tyyn cpw im rmsbstxagic lgzw lggkcby yts idjrtymjcy ocarjboce xl rmticdiq lfkgc p vwmtt ipjr uujjj zk gsemrxrk mx gtpnvgmvgggic (cv agajoce kcxn rprk yz lovfz mx untl dlk itduy rnt uifkg vtpydl xq qsyn cxrn dgbgrn ug cdpq yiigbxrotq) Rxik c-byoa gcb kmorc byoa plj stagqt rpljagtt ug sdzoac efucc ryraq (gt unxan rnt ipjrtp wmvtq im hnkpi sgxtazaw lgzw zwc gcixnotlz) icdigtv jdcy lui xtoaxpk rnt ipjrtp plj pkrgvxcti zd hdrn zk dxtc pr ifk qgbc bmstlz; zwgy nkgkoiq rmsbstxagiguc kkct zkiuktl qsyn ocbokgjjyrh Icdi stqypekh ipl pjyd ht ahcj ru gticxpaz uoif pszdkgicj qehrkbq dug kmysejk zd ugbkg vgmjjazh ug ytpbxakh lgms c-rmsbcxrc lchhgztq mx ru nggrorgvprk gt mtagtt idlztqzh Pbbtpzxqkgq plj qkgtorc epukgjtpy syt jxpkrr icdi sppqtroce im hcts stqypekh zd sdzoac efucc jqkgq pzujr epubmzxmth eyebcti jjc syztq yts uifkg tdrougiprodly gthrkpb dd jqoce emyiyr kgxj cspgr ug bdgitkgxj
    """.replace(' ', '').replace('\n', '').upper()

    keyprobs = keylen_probabilities(text)
    print('Key Probabilities:')
    for leng, prob in sorted(keyprobs.items(), key=lambda x: -x[1])[:5]:
        print(leng, prob)
    print('----------')

    most_likely_length = max(keyprobs.items(), key=lambda x: x[1])[0]
    print('Most Likey Key Length =', most_likely_length)
    print('----------')

    # Compute character bins
    ch_bins = [defaultdict(int) for _ in range(most_likely_length)]
    for i in range(len(text)):
        ch_bins[i % most_likely_length][text[i]] += 1

    print('Character Frequencies')
    for ch in string.ascii_uppercase:
        print(ch, ' '.join("{:3d}".format(ch_bins[i][ch]) for i in range(most_likely_length)))


if __name__ == "__main__":
    main()
