# BookBot 📖

A simple command-line tool that analyzes a text file and reports word count and letter frequency. My first [Boot.dev](https://www.boot.dev) project.

## What it does

Point it at a `.txt` file and it will:
- Count the total number of words
- Count how many times each letter appears
- Print the letters sorted from most to least frequent

## Usage

```bash
python3 main.py books/frankenstein.txt
```

Sample output:

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt.
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
...
============= END ===============
```

A few sample books (*Frankenstein*, *Moby Dick*, *Pride and Prejudice*) are included in `books/` to try it out on.

## How it works

- `stats.get_book_text` reads the file into a string.
- `stats.get_num_words` splits on whitespace and counts the words.
- `stats.get_char_count` builds a dictionary of character → count (case-insensitive).
- `stats.sort_char_count` converts that into a list of `{char, num}` entries sorted by frequency.
- `stats.analyze` ties it all together and prints the report, filtering the output down to alphabetic characters only.

## Running it

No dependencies beyond the Python standard library.

```bash
python3 main.py <path_to_book>
```
