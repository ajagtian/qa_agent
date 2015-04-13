#!/usr/bin/python3 -tt

import percepclassify

question = input()
coarse_class = percepclassify.classify(question, percepclassify.get_g_hash_from_file('../data/models/coarse.model'))
fine_class = percepclassify.classify(question, percepclassify.get_g_hash_from_file('../data/models/fine.'+coarse_class+'.model'))
print(coarse_class+':'+fine_class)



		
