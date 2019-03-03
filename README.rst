=========================
BanglaKit Bengali Stemmer
=========================

.. image:: https://travis-ci.org/banglakit/bengali-stemmer.svg?branch=dev
    :target: https://travis-ci.org/banglakit/bengali-stemmer

A stemmer is a light-weight approach to find root words, avoiding expensive morphological analysis. The *BanglaKit Stemmer* implements a stepwise approach to removing inflections from Bengali Words [1].

Work is in progress with the algorithm of the stemmer, the implementations may vary significantly from version to version.


----------
Algorithms
----------

Rafi Kamal's Stemmer
~~~~~~~~~~~~~~~~~~~~

Originally Developed by `Rafi Kamal`_. Ported to Python.::

  from bengali_stemmer.rafikamal2014 import RafiStemmer
  stemmer = RafiStemmer()
  stemmer.stem_word('বাংলায়')

.. _`Rafi Kamal`: https://github.com/rafi-kamal/Bangla-Stemmer


----------
References
----------

[1] M. R. Mahmud, M. Afrin, M. A. Razzaque, E. Miller and J. Iwashige, "A rule based bengali stemmer," 2014 International Conference on Advances in Computing, Communications and Informatics (ICACCI), New Delhi, 2014, pp. 2750-2756.
doi: 10.1109/ICACCI.2014.6968484
