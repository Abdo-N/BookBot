from stats import get_num_words
from stats import get_book_text
from stats import get_char_count
from stats import sort_char_count
from stats import analyze
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        analyze(sys.argv[1]) 
       
main()