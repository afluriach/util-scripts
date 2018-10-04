#!/usr/bin/env python

import sys

in_path = sys.argv[1]
out_path = sys.argv[2]

in_fp = open(in_path, 'r')
out_fp = open(out_path, 'w')

out_fp.write("[table]")

for line in in_fp:
	tokens = line.split(",")
	
	out_fp.write("[tr]")
	
	for token in tokens:
		out_fp.write("[td]")
		out_fp.write(token)
		out_fp.write("[/td]")
	#end
	
	out_fp.write("[/tr]\n")
#end

out_fp.write("[/table]")

in_fp.close()
out_fp.close()