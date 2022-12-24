# poker_scripts

Welcome to my poker scripts! These are here to help me and whoever finds it useful gain familiarity with pre-flop
ranges/strategy.

I have a relatively basic GUI that I update whenever I make a new function or feel some inspiration to improve its 
appearance. I'm not much of a graphic designer but I'm pretty satisfied with how it looks.

What's next: I want to finish a function that tells the user whether or not to continuation bet a flop. This
is pretty complicated as it has to assess ranges. After that, general flop strategy is next.

Turn and river strategy are yet to be added. I am not very familiar with optimal turn/river strategy, as they are more 
complicated. This makes them difficult to code in and they tend to be more computation heavy due to many combinations 
of hands as opposed to the 2 cards you have pre-flop and 5 cards (1 exact hand) you have on the flop. Comprehensively 
covering flop strategy will take awhile so I'll cross the bridge of further streets when I get to it.

File guide:

TRAINING

initiation - creates the "deck" and adds useful functions for sorting and extracting information from cards

hand_values - determines the value of a given hand, as well as whether or not a hand has some kind of draw

raise_pf - puts user in a seat before the BB and a hand and asks whether or not to raise

calling_pf_raise - puts user in a seat after UTG and a hand and asks wther or not to call a raise from
a given poisition

flop_wetness - helper function for c_bet_flop, determines how "wet" a board is.

c_bet_flop - (in progress) puts user in a seat having raised PF, their hand, a flop, and asks them whether
or not to continuation bet. It currently has basic functionality, but I'd like to consider ranges, and add
a feature that asks for sizing if one does continuation-bet.

SIMULATIONS

aces_vs_wrld - simulation I ran to see how often aces has the best hand six-handed post-flop. Thinking about
expanding this to to add equities and calculate it for different ranges/kinds of flops.

pf_stats - simulation I ran to see how often one flops hands such as a pair, a flush draw, etc.

GUI UPDATES

12/23/22
Having finally finished finals, I've had some time to work on the GUI consistently. Updates include:
-improved "look" of screen after making decision
-updated ranges according to Johnathan Little's pre-flop charts, which are more accurate in terms of GTO optimal strategy
-BTS: working on function that allows user to manually update opening pre-flop ranges. This will be included in a new settings bar.
-BTS: wrote more appropriate function for assessing state of flop. I think I will end up with multiple functions that assess 
different qualities of the flop and use them in tandem to determine what to do. Coding in even simple flop strategy is turning out to be 
difficult, but I'm welcome for the challenge.

