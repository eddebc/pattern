# Pattern - a reimplementation of pattern\_create/pattern\_offset in Python3
Metasploit comes with multiple very convenient scripts and utilities. Among
the most valuable are pattern_create and pattern_offset. 
They have both have a relatively long startup time.

So after I found a Python2 rewrite of this, I decided to write it in Python3
and to bring it closer to the original Metasploit's ruby list of options.
## Usage
```
$ ./pattern_create.py -h
usage: pattern_create.py [-h] -l LENGTH [-s SETS]

Tool to create a unique pattern. Example:
$ ./pattern_create.py -l 50 -s ABC,def,123
Ad1Ad2Ad3Ae1Ae2Ae3Af1Af2Af3Bd1Bd2Bd3Be1Be2Be3Bf1Bf

optional arguments:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        Length of the pattern
  -s SETS, --sets SETS  Custom pattern sets such as <ABC,def,123>

```
So, to create a 2048 byte pattern you run
```
$ ./pattern_create.py -l 2048
Aa0Aa1Aa2[...snip...]p7Cp8Cp9Cq0Cq1Cq
```
