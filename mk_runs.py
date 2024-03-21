#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-24"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['Per-emb-2'] = [113271, 113408, 113410, 113412,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['Per-emb-2']   = "dv=20 dw=20 b_order=5"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['Per-emb-2']   = "srdp=1 admit=0"

pars3 = {}
pars3['Per-emb-2']   = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
