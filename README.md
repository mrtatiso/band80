# band80

80 uniform digits from the system's random source, grouped as you ask.

```
$ band80 4:20
39563319081286831671.85130815965080617505.81064959590150397768.12816156932300764448
```

## Install

```
pip install git+https://github.com/mrtatiso/band80
```

## Use

### Terminal

```
band80 <groups>:<size>
```

`groups × size` must be 80:

```
1:80  2:40  4:20  5:16  8:10  10:8  16:5  20:4  40:2  80:1
```

```
$ band80 8:10
7129437635.8889845141.8581453939.1188794158.0568444238.0653891926.0800174989.9121717592
$ band80 1:80
24345766710253999834910350509153163034183455493828081152357950821834097525890124
```

Anything else prints the usage and exits with code 2.

### Python

```python
from band80 import gen

gen(4, 20)   # same as band80 4:20
gen(8, 10)   # same as band80 8:10
```

`gen` raises `ValueError` if `groups × size` is not 80.

## What it is

- **80 digits, uniform.** Every value from `000…0` to `999…9` is equally likely, leading zeros included: 10⁸⁰ possibilities, about 265.75 bits of entropy.
- **From the system's random source.** `secrets.randbelow`, which reads from the operating system's cryptographic generator.
- **The grouping is only format.** `4:20` and `8:10` are equally random; only the dots move.
- **Raw material.** A band80 carries no type, tag or checksum. What it means (a salt, a key, a coordinate) and how secure the result is depend on whatever reads it, not on band80.

## Test

```
python -m unittest discover test
```
