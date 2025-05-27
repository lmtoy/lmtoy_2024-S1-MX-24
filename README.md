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

## Observations

See lmtinfo.txt for a full record. There were 17 obsnums observed, a few of them actually
has all beams good (somewhat unusual) - see comments.txt - None of the obsnums were
discarded.

# DATE-OBS          OBSNUM
2024-03-17T03:37:05 113271
2024-03-18T03:09:46 113408
2024-03-18T03:28:02 113410
2024-03-18T03:43:58 113412
2024-11-25T08:40:36 123258
2024-11-25T08:56:37 123260
2024-11-25T09:12:50 123262
2024-11-26T07:24:06 123319
2024-11-26T07:40:23 123321
2024-11-26T07:56:39 123323
2024-11-26T08:20:19 123327
2024-11-27T07:35:57 123493
2024-11-27T07:53:52 123495
2024-11-27T08:09:42 123497
2024-11-27T08:44:59 123503
2024-11-27T09:02:15 123505
2024-11-27T09:19:41 123507


## Experiments

A few special experiments were done 

* 113271_123327__all : subset combo
* 113271__wide:  example how the full bandwidth looks (arguing only dv=5 dw=20 has some degree of success)

## QA branches

- main (6-mar-2024)
- alaina (9-dec-2024)
- alaina_2 (18-dec-2024)
- main (9-apr-2025)
