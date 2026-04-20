# Ett synsätt:
# Modulo är resten vid division

# Ett annat synsätt:
# Se 2 som att den ska ta de sista 2 - 1 sifforrna binärt... Kanske inte pedagosikt?

mod_10_2 = 10 % 2
mod_11_2 = 11 % 2
mod_12_2 = 12 % 2
mod_13_2 = 13 % 2
mod_14_2 = 14 % 2

# Håll talet mellan 0..99
import random

rnd_big = int(random.random() * 10000)
rnd_0_99 = rnd_big % 100
