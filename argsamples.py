import datetime
import random
from typing import Any, Optional

all_holeargs: list["HoleArgs"] = []


class HoleArgs:
    name: str
    allargs: Optional[list[str]]

    def __init_subclass__(cls) -> None:
        globals()["all_holeargs"].append(cls)

    def __call__(self) -> list[str]:
        ...


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class Arrows(HoleArgs):
    name = "arrows"
    allargs = "↙↲⇙←⇐⇦↖↰⇖↓⇓⇩↔↕⇔⇕⥀⥁↑⇑⇧↘↳⇘→⇒⇨↗↱⇗"

    def __call__(self) -> Any:
        return random.choices(self.allargs, k=66)


class CardNumberValidation(HoleArgs):
    name = "card_number_validation"

    def __call__(self) -> list[str]:
        return [
            " ".join(str(random.randint(0, 9999)).zfill(4) for _ in range(4))
            for _ in range(106)
        ]


class CSSColors(HoleArgs):
    name = "css_colors"
    allargs = [
        'IndianRed', 'LightCoral', 'Salmon', 'DarkSalmon', 'LightSalmon',
        'Red', 'Crimson', 'FireBrick', 'DarkRed', 'Pink', 'LightPink',
        'HotPink', 'DeepPink', 'MediumVioletRed', 'PaleVioletRed', 'Coral',
        'Tomato', 'OrangeRed', 'DarkOrange', 'Orange', 'Gold', 'Yellow',
        'LightYellow', 'LemonChiffon', 'LightGoldenRodYellow', 'PapayaWhip',
        'Moccasin', 'PeachPuff', 'PaleGoldenRod', 'Khaki', 'DarkKhaki',
        'Lavender', 'Thistle', 'Plum', 'Violet', 'Orchid', 'Fuchsia',
        'Magenta', 'MediumOrchid', 'MediumPurple', 'BlueViolet', 'DarkViolet',
        'DarkOrchid', 'DarkMagenta', 'Purple', 'Indigo', 'DarkSlateBlue',
        'SlateBlue', 'MediumSlateBlue', 'RebeccaPurple', 'GreenYellow',
        'Chartreuse', 'LawnGreen', 'Lime', 'LimeGreen', 'PaleGreen',
        'LightGreen', 'SpringGreen', 'MediumSpringGreen', 'MediumSeaGreen',
        'SeaGreen', 'ForestGreen', 'Green', 'DarkGreen', 'YellowGreen',
        'OliveDrab', 'Olive', 'DarkOliveGreen', 'MediumAquamarine',
        'DarkSeaGreen', 'LightSeaGreen', 'DarkCyan', 'Teal', 'Aqua', 'Cyan',
        'LightCyan', 'PaleTurquoise', 'Aquamarine', 'Turquoise',
        'MediumTurquoise', 'DarkTurquoise', 'CadetBlue', 'SteelBlue',
        'LightSteelBlue', 'PowderBlue', 'LightBlue', 'SkyBlue', 'LightSkyBlue',
        'DeepSkyBlue', 'DodgerBlue', 'CornflowerBlue', 'RoyalBlue', 'Blue',
        'MediumBlue', 'DarkBlue', 'Navy', 'MidnightBlue', 'Cornsilk',
        'BlanchedAlmond', 'Bisque', 'NavajoWhite', 'Wheat', 'Burlywood', 'Tan',
        'RosyBrown', 'SandyBrown', 'GoldenRod', 'DarkGoldenRod', 'Peru',
        'Chocolate', 'SaddleBrown', 'Sienna', 'Brown', 'Maroon', 'White',
        'Snow', 'Honeydew', 'MintCream', 'Azure', 'AliceBlue', 'GhostWhite',
        'WhiteSmoke', 'SeaShell', 'Beige', 'OldLace', 'FloralWhite', 'Ivory',
        'AntiqueWhite', 'Linen', 'LavenderBlush', 'MistyRose', 'Gainsboro',
        'LightGray', 'LightGrey', 'Silver', 'DarkGray', 'DarkGrey', 'Gray',
        'Grey', 'DimGray', 'DimGrey', 'LightSlateGray', 'LightSlateGrey',
        'SlateGray', 'SlateGrey', 'DarkSlateGray', 'DarkSlateGrey', 'Black'
    ]

    def __call__(self) -> Any:
        random.shuffle(self.allargs)
        return self.allargs


class DayOfWeek(HoleArgs):
    name = "day_of_week"
    _range = (
        datetime.date(1583, 1, 1).toordinal(),
        datetime.date(9999, 12, 31).toordinal(),
    )

    def __call__(self) -> list[str]:
        ordinals = [random.randint(*self._range) for _ in range(687)]
        return [datetime.date.fromordinal(s).isoformat() for s in ordinals]


class Emojify(HoleArgs):
    name = "emojify"
    allargs = [
        ";-)", ";-P", ":-", ":-(", ":-)", ":-@", ":-*", ":-\\", ":-#", ":-|",
        ":-$", ":-D", ":-J", ":-O", ":-P", ":'-(", ":'-)", "':-(", "':-D",
        "}:-(", "}:-)", "B-)", "O:-)", "X-)", "X-P"
    ]

    def __call__(self) -> list[str]:
        random.shuffle(self.allargs)
        return self.allargs


class ForsythEdwardsNotation(HoleArgs):
    name = "forsyth_edwards_notation"
    allargs = [
        "1n1Rkb1r/p4ppp/4q3/4p1B1/4P3/8/PPP2PPP/2K5 b k - 1 17",
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
        "K7/2bb4/1bbb4/3k4/8/8/8/8 w - - 69 272",
        "1R6/2k1N3/7r/8/2B5/4K3/3rb3/4n3 w - - 0 50",
        "4K3/2k1N3/1R6/7r/4n3/8/3rb3/2B5 w - - 0 50",
        "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1",
    ]

    def __call__(self) -> Any:
        random.shuffle(self.allargs)
        return self.allargs


class Hexdump(HoleArgs):
    name = "hexdump"
    allargs = [
        "Code Golf", "0123456789abcdef",
        """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~""",
        "Code Golf is a game designed to let you show off your code-fu by solving problems in the least number of characters.",
        """Lorem ipsum dolor sit amet,

 consectetur adipiscing elit""", """multi-
line
string""",
        """In mathematics and computing, the hexadecimal (also base 16 or simply hex)
numeral system is a positional numeral system that represents numbers using a
radix (base) of 16. Unlike the decimal system representing numbers using 10
symbols, hexadecimal uses 16 distinct symbols, most often the symbols "0"-"9"
to represent values 0 to 9, and "A"-"F" (or alternatively "a"-"f") to represent
values from 10 to 15.

Software developers and system designers widely use hexadecimal numbers because
they provide a human-friendly representation of binary-coded values. Each
hexadecimal digit represents four bits (binary digits), also known as a nibble
(or nybble). For example, an 8-bit byte can have values ranging from 00000000 to
11111111 in binary form, which can be conveniently represented as 00 to FF in
hexadecimal."""
    ]

    def __call__(self) -> Any:
        random.shuffle(self.allargs)
        return self.allargs


class MorseEncoder(HoleArgs):
    name = "morse_encoder"
    nums_alphs = ["0123456789", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    words = "VEX QUICK WALTZ BUD FOR JIGS NYMPH FOR".split(" ")

    def __call__(self) -> list[str]:
        remaining = self.words.copy()
        words = [""] * 6
        for _ in range(random.randint(0, 5)):
            i = random.choice([i for i in range(6) if not words[i]])
            words[i] = remaining.pop(random.randint(0, len(remaining) - 1))

        empty_i = [i for i in range(6) if not words[i]]
        num_or_alph = [random.choice([0, 1]) for _ in range(6)]
        while len(" ".join(words)) < 36:
            i = random.choice(empty_i)
            charspool = self.nums_alphs[num_or_alph[i]]
            words[i] += random.choice(charspool)
        return [" ".join(words)]


class PangramGrep(HoleArgs):
    name = "pangram_grep"
    allargs = [
        "MY faXED f|OKe| dOn a PAGEx iN THe CaBL{E{ {Tv qUIz SHOD.",
        "6>~_4\"gV9lb?2!Ic7}=-m'Kd30ph].o%@W+[{8UNk&U1HS<Xz(x;${^Y#)Q,rJ\\{5/*:",
        "ubc|j{eGmAViSkzHrt~ylWQd}of~xn",
        "juSt POETs wAX BolDlY As KI~ngS ANd qUE|ENs maRzh OOEr fUZZ.",
        "gR~~JEqsoHMNyKcIfzt}d~lAUxpBW",
        "GRu~Mpy wIzARDs Make TOXIC BreW foR THe evIL qUeEn{ And jAcK.",
        "all QuEstiOns ASked| by FIve WaTc}Hed Ex{pErTS AMaZe thE jUdgE.",
        "Back iN JUne wE delIveRED OXYGeN eQUIp}mENT Of thE sAME S~IzE.",
        "N~QBklfrpwdMHT{ygzcJueoxVai",
        "Z}sAFXMkevlWUrjPbOYCDqNI{gh",
        "Hey zacH, sHoULd I ~pRogRAM A heX eDItoR IN JAv{A? wHy nOT }SQL Or BrAinf--K!",
        "jaVjiM WiLl bUDgmT|{ F~Or tXm mOST MXpmNsIVm zOOLOgY mQUIpmMn|t.",
        "oIHbkwY{|EFGPdJr~XnmSaTVulCz",
        "QuiRky SPUd bOYS ca|n JAM aFTER ZAppinG fiVE Worthy pOLYSi~xeS.",
        "baTtlE Of THEr{M~oPYLaE|: qUick JaZELIN grazed Wry zERZEs}.",
        "cuCe, kxnd, jOVxsL, foxY pHysX~quE, sMSzxNG beSU{CY? GoGSEr!",
        "A QUICk ~MoveMect OF tHE ECEmY WIl|~l {jeopArDIZe SIv g~uCBOatS.",
        "gR|uMzy W{iZards make tOXiC brEw {fOr THE evIL QUEEH aHd j|ac~K.",
        "}IADgwCmYNh{rTPFvBO~}ZjSlEuXq",
        "YrZPwAUhlT~~CVMSD}}JGOfkX~beQI",
        "{GPa~~jl{FRWeZTo}SbVcNxuKqhiyd",
        "Dim |QuIcKly REvLizED TdvT tDE bevUTifuL gzwns VrE e}XP{EN}sIV~e.",
        "BaTtL|E OF The|rMO|PYlAE: qUicK jAveLIN GRazeD wRy X|eRxEs.",
        "yml~Vhx|zsFErOQbg{NdP}ikCuTaJ",
        "How raZ|orbacK-Jump}INg FrogS CaN lEVEL siX pIqUED gYmNAsTS!",
        "WQlE|vTbrzyhG|XJdF~kN}aciMosp",
        "haIXbS}ZTrwEoFcQJg|~UPd{VN|kml",
        "jUsT po~etS wAx~ }BolDLY AS }KINgs anD }qUEEnS marCh oVER Fuzz.",
        "|FOXY }PArSo}NS qUIz AND CajoLE tHE lOvABly dim WIkI-gIrL.",
        "vUiRkG SpuL bOgS can jAm aFT|eR zAPpin}g fivE wOrTHG pOL~GSIXes.",
        "ZSy{{XFjuqIDvgKRWeNC{lBphMOt",
        "cuTE, KInD, jovIAl, FOxy phYSiqu{E|, AmaZ|inG beAUTY? WO~WsER!",
        "w~hen ZO~MbIEs arrive, quicklY faX JUDGe p|At.",
        "boREd? CravinG A puB QUIz FiX{? Why, JuSt come to~ the |{RoyaL OaK!",
        "WHen ZoMW{ieS aRrIYe, qUIc~KLy ~{faX BuDGe dA|t.",
        "uES~ohZDaLjiTBKv}NfGm}ry}QWpx",
        "fowY |ParSoN{S qUWZ and c|AJOLe tke lOvABlY d~Wm RWKw{-GwrL.",
        "RSy{JVmpEtaFH}dCWngqK|zXUIb|l",
        "a| lARGe fawn JumPEd Q}uicKLY OvER WH{iTE z|~inC boXeS.",
        "Sb|XrHWVp|zgQl}IFcaO}jteU|nmKy",
        "ghX~|ldb{MkpqvCOwErzYN}sIAFtU",
        "JiM QuICKly rEALIzed |~That Th}e bEAutifuL gOWNs Are exPENSIvE.",
        "SZdT|qoM~pIYlCvwkxFreujHNag",
    ]

    def __call__(self) -> list[str]:
        random.shuffle(self.allargs)
        return self.allargs


class ReversePolishNotation(HoleArgs):
    name = "reverse_polish_notation"
    allargs = [
        "30931 29731 24650 - - 3 20161 12756 - * -",
        "11793 21262 21131 189 2 3 * * 73 1 0 + * + - - 16434 498 / 183 * + + 1 1 26031 26030 - * * /",
        "32409 1645 - 27245 - 17161 1 / 1 1 1 * * 23032 1 * 654 22377 + - * * + 77 238 * 3 1 + 7497 * 1 / 18 / 4 3844 * 17695 1187 1133 + - - 21142 22 / 1 * 5657 5657 / 5759 4812 - * - * / / +",
        "6519 19511 30 441 * + 279 21 8 + * 6787 + 14877 - 1 * / 31828 13567 13566 - / 1 / 218 / - 15171 0 * 1 + 0 + 1171 7116 6 / + * 2352 - / -",
        "67 12 + 352 + 26811 22389 - +",
        "1472 24042 + 0 1 + / 25071 - 28521 10449 - 36 / 17426 2850 4140 + - 2 / 1 28962 28962 - 0 + + / + +",
        "20856 1 / 6 / 2060 + 70 + 19250 + 24811 - 474 * 10665 / 15817 * 31632 - 0 + 1 * 899 * 14030 + 6 / 16185 + 11469 + 2 /",
        "30912 8 / 483 2856 + 3283 - / 18699 18637 - + 25654 25654 - 1 17659 * 17659 / + * 17589 194 1159 + / *",
        "2 0 + 11812 * 1 1115 31921 137 1 * / + 22276 + * / 21745 21745 - 13422 13421 - 1 * + 24974 1 2 * / 1376 11008 8 / / * * *",
        "26196 3090 23201 2603 17511 1 1 13599 13598 1 1 1 21408 0 12787 0 12870 25740 2 1 0 29913 29913 - + + * / - + * + * + * * * - * * / + - - /",
        "2956",
        "2032 223 25565 20329 1 1 * / - + +",
        "2884 188 3 30500 30481 1 / - + * + 1 1 * 0 + *",
        "28813 24615 - 13349 13932 15996 + 17392 - - 3890 + 27281 1 / 1 / + 32222 16307 - 5 1 * / 30391 25578 - + / *",
        "18599 1 / 5349 - 19505 + 27546 25479 1 / 22509 14274 13 / - 2379 / / - 24557 - 40 * 618 + -",
        "11 22 21653 10627 - 11026 / * 973 * 25540 2554 / 12 + / *",
        "31690 2432 - 15468 - 19518 15045 - 4472 - *",
        "4197 6737 + 10932 - 4707 * 67 233 * 67 / 1 13 * 32376 32369 - * 141 * + 2 2771 * + 1 28277 * 27181 - 614 1215 7392 42 / + + + 2 0 1 + 2 8496 * 16992 - + * * / /",
        "31220 2746 3 * - 171 809 + 448 12 + + 2 488 * - - 18130 24447 1 / 2143 - 21267 1442 + 415 - - / - 28360 1 / 20130 18073 12335 - + - 2291 + 14632 + -",
        "267 5 *",
        "0 -1 + 1 -",
    ]

    def __call__(self) -> list[str]:
        random.shuffle(self.allargs)
        return self.allargs


class RockPaperScissorsSpockLizard(HoleArgs):
    name = "rock_paper_scissors_spock_lizard"
    allargs = ["💎📄✂🖖🦎"[x] + "💎📄✂🖖🦎"[y] for x in range(5) for y in range(5)]

    def __call__(self) -> list[str]:
        random.shuffle(self.allargs)
        return self.allargs


class SevenSegment(HoleArgs):
    name = "seven_segment"

    def __call__(self) -> list[str]:
        return [str(random.randint(0, 10**20 - 1)).zfill(20)]


class ZodiacSigns(HoleArgs):
    name = "zodiac_signs"

    def __call__(self) -> list[str]:
        return [
            str(
                datetime.datetime.fromtimestamp(
                    random.randint(63068400, 94690800 - 1)))[5:-3]
            for _ in range(620)
        ]


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class ArgProvider:
    classdict = {C.name: C for C in all_holeargs}

    def __init__(self, seed: Optional[int] = None) -> None:
        random.seed(seed)

    def __call__(self, hole: str) -> list[str]:
        name = hole.lower()
        for a, b in {
                " ": "_",
                "-": "_",
                "–": "_",
                "’": "",
                "(": "",
                ")": "",
                "ń": "n",
                "á": "a",
        }.items():
            name = name.replace(a, b)
        _class = self.classdict.get(name)
        if _class is None: return []
        return _class()()


if __name__ == "__main__":
    args = ArgProvider(seed=None)("Zodiac Signs")
    print(args)
