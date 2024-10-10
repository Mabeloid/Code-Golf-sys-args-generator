# Code Golf sys args generator
 generates args to test your code golf attempts offline

# supported holes:
- Arrows
- Card Number Validation
- CSS Colors
- Day of Week
- Emojify
- Forsyth-Edwards Notation
- Hexdump
- ISBN
- Jacobi Symbol
- Morse Encoder
- Pangram Grep
- Reverse Polish Notation
- Rock-paper-scissors-Spock-lizard
- Seven Segment
- Zodiac Signs

# usage:
```py
args = ArgProvider(seed=0)("Zodiac Signs")
print(args)

>>> ['11-23 22:34', '05-29 15:44', '10-21 09:38', '12-11 17:40', ...]
```
the list of arguments can then be used in subprocess.run()