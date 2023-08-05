#!/usr/bin/env python


prefix = {}
root = {}
suffix = {}
word = {}
correlatives = {}
pos_marker = {}

def load_txt_file(file_txt,d):

	with open(file_txt) as f:
		for line in f:
			(key, val) = line.split(",")
			d[key] = val.strip()
	f.close()

def replace_by_dict(word,dictionary):
	for key in dictionary.keys():
		word = word.lower().replace(key, dictionary[key])
	return word

load_txt_file("nra_correlatives.txt",word)
load_txt_file("nra_full_words.txt",word)
load_txt_file("nra_ends.txt",pos_marker)
load_txt_file("nra_roots.txt",root)
load_txt_file("nra_prefixes.txt",prefix)
load_txt_file("nra_suffixes.txt",suffix)

def replaceWord(wordre,typeParticle):
	if typeParticle == 'word':
		return(replace_by_dict(wordre,word))
	elif typeParticle == 'pos_marker':
		return(replace_by_dict(wordre,pos_marker))
	elif typeParticle == 'root':
		return(replace_by_dict(wordre,root))
	elif typeParticle == 'prefix':
		return(replace_by_dict(wordre,prefix))
	elif typeParticle == 'suffix':
		return(replace_by_dict(wordre,suffix))


print(replace_by_dict("aŭ",word))

#print(word)

