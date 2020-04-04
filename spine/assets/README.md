# Part ONE
*DISCLAIMER: Probably little or none of this below applies, as most of what's documented here is not implemented in WORDSTAR Linux just yet (or never will be.)*     

    *howto convert to mobi with proper chapter breaks*

    **

*use double hashes*
*convert to epub using 'wordsmith generate epub'*
*import into calibre and convert to mobi using h2 as chapter breaks*
        
    Section breaks: Heuristic processing and 8========> for line breaks

    'structure detect; in Calibre: h2 = ##, h3 = ### in *.md 
*that's it*

or . . . 

# make a manuscript pdf

1. While in Sublime Text, hit __ALT + P__

 **or run in a terminal 'start-xreader-gen-pdf'**

# (optional) change italics to underline

1. open ODT in Libreoffice
2. ctrl+h, click other options, click Format..., select italics
3. click on replace field
4. click Format..., select "Font Effects", select Underlining; single
5. Replace All
6. run "wordsmith g pdf" again

# How to convert from Wordstar to Markdown

1. open dosbox, press 'c' to load conversion software
2. from the menus, choose 'from wordstar to Wordperfect 5.1'
3. open newly converted Wordperfect 5.1 file in WP51 dos wp.EXE
4. save an 'generic' txt
5. open libreoffice in linux. open txt file, and copy all, then paste into sublime text *.md file

# Convert From Markdown to Wordstar 7

1. open *.md in Sublime Text and save file "ctrl+shift+s" as *.txt 
2. open newly converted TXT file in WP51 Dosbox
3. save file as wordperfect 5.0 file.
4. open (in quikmenu) the conversion software "press c"
5. convert wp 5.0 file to Wordstar 7 file.
