# wordstats

A tiny command-line program. It reads a text file and prints the five
most common words, each with its count. `sample.txt` holds the opening
paragraph of Moby-Dick (public domain).

Run it from this folder:

    python3 wordstats.py sample.txt

Expected output when the program works:

       8  i
       8  the
       6  and
       5  of
       4  me

(`i` and `the` tie at 8, so your output may show those two lines in
either order.)

Right now the program crashes. Fixing that crash is the first exercise
in lesson A4. Needs Python 3.8 or later; no packages to install.
