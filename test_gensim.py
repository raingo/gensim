#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

import sys
sys.path.insert(0, './build/lib.macosx-10.5-x86_64-2.7/')
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = [['first', 'sentence'], ['second', 'sentence']]
model = gensim.models.Word2Vec(sentences, min_count=1)


def main():

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
