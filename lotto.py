#!/usr/bin/python
#
# Check der Lottozahlen fuer die Tippgemeinschaft
#

import sys

players=[ \
('Axel', [4,7,17,26,34,45]), \
('Lonnny', [6,15,23,27,38,42]), \
('Sascha', [4,11,18,25,36,37]), \
('Melanie', [7,11,13,17,28,43]), \
('Sabine', [6,7,12,22,42,47]), \
('Franja', [3,14,21,39,43,49])
]

if len (sys.argv) != 8:
	raise Exception ("7 Argumente sollt Ihr sein !")

current = set (sys.argv[1:7])
bonus = sys.argv[7]

print (current, bonus)

for player in players:
	name=player[0]
	numbers=player[1]

	hits = 0
	for i in numbers:
		if str (i) in current:
			hits += 1

	if int (bonus) in numbers:
		print (name, hits, "+Zusatzzahl")
	else:
		print (name, hits)


