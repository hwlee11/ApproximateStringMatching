# Approximate string matching

This code is word level string aligner base on levenshtein distance.  
Support langauge: english, korean

## Author
hwlee
hwl@ai.korea.ac.kr

## Date

2022-09-20

## Requirements

python-levenshtein  
jamo  
g2pk  

## Usage

```
$ python3 WordsAlignment.py --strA 'hello i am bob' --strB 'hello i'm alice'
$ [('hello', 'hello'), ('-', 'i'), ('-', 'am'), ('bob', 'bob')]
```

```
$ python3 WordsAlignment.py --strA '나는 저녁으로 라면을 먹었다' --strB '나는 점심을 먹었다' --korean 1
$ [('나는', '나는'), ('-', '저녁으로'), ('점심을', '라면을'), ('먹었다', '먹었다')]
```

## Reference

[1] https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm  
[2] CSE 589 Applied algorithms-https://courses.cs.washington.edu/courses/csep521/99sp/lectures/lecture18/sld001.htm
