# 2024-S1-MX-24


This is a SEQ 200MHz (8k channels) project.

Only one IF.  

One source, Per-emb-2, observed in 17 obsnums.

Oddly enough , beam13 looks ok, at 90GHz.

Restfreq = 90.978989 = HC3N

vlsr=7 was used.

Narrow window, dv=5 dw=20 look ok, with low order b_order=1.  For some obsnums beam 3 seems still
somewhat varying and may need to be masked out, but overall the signal is fairly strong. beam 14 is
also suspect in some of the obsnums.

PV-slices show strong stripes, which is no good, so may need extra work depending on what PI wants.


## Experiments

A few special experiments were done 

* 113271_123327__all : subset combo
* 113271__wide:  example how the full bandwidth looks (arguing only dv=5 dw=20 has some degree of success)
