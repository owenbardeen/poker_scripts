# poker_scripts
Welcome to my poker scripts! These are here to help me and whoever finds it useful gain familiarity with pre-flop
ranges/strategy.
What's next: I want to finish a function that tells the user whether or not to continuation bet a flop. This
is pretty complicated as it has to assess ranges.
Then, I plan on adding a GUI that will make practicing using this program a lot more conducive towards learning.

Turn and river strategy are yet to be added. I am not very familiar with optimal turn/river strategy, as they are
more complicated. This makes them difficult to code in and they tend to be more computation heavy due to many
combinations of hands as opposed to the 2 cards you have pre-flop and 5 cards (1 exact hand) you have on the flop.

File guide:
initiation - creates the "deck" and adds useful functions for sorting and extracting information from cards
hand_values - determines the value of a given hand, as well as whether or not a hand has some kind of draw
raise_pf - puts user in a seat before the BB and a hand and asks whether or not to raise
calling_pf_raise - puts user in a seat after UTG and a hand and asks wther or not to call a raise from
a given poisition
