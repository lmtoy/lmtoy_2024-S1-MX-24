#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-24"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['Per-emb-2'] = [113271, 113408, 113410, 113412,
                   123258, 123260, 123262, 123319, 123321, 123323, 123327,     # nov 25/26
                   123493, 123495, 123497, 123503, 123505, 123507,]            # nov 27


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['Per-emb-2']   = "dv=5 dw=20 b_order=1"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['Per-emb-2']   = "srdp=1 admit=0 pix_list=-3,14"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, None, sys.argv)
