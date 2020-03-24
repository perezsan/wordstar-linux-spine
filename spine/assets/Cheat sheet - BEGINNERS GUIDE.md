
## Cheat sheet - BEGINNERS GUIDE
<!-- PRO TIP: Remap Caps Lock to Left Control by INSTALLING
    SharpKeys TO REALLY PLAY WITH POWER.
    https://github.com/randyrants/sharpkeys -->
<!-- LAST PRO TIP: For all you night owls, 
    USE Sublime Text 3 w/ f.lux to make
    writing/editing viewing even more easy one the eyes.
    https://justgetflux.com  -->
<!-- Hold CONTROL TO RIDE THE SNAKE -->
            __LEFT HAND NAVIGATION__
                        ^                       r *[Scroll Up One Page]*
                        |
                        E
(Previous word) a   <--s d-->  f (To Next Word)
                        x
                        |
                        v                       c *[Scroll down one page]*

## Recommended Font install

https://www.dafont.com/perfect-dos-vga-437.font

## Formatting

1. Use double (or single) HASHES for chapter, scene, or notation marking


<!-- 2. Insert greyed out comments like you see on this line with CTRL+SHIFT + / -->
<!-- To change para residing under the cursor into a comment itself, use CTRL + / -->

2. Endnote / Footnotes: __CTRL + .__ Be forewarded, endnote/footnotes may cause problems when converting with pandoc (if your not familiar with using it) so I suggest you use these judicially.

    Lorem ipsum dolor sit[^1] amet consectetur adipiscing elit. Vestibulum vitae bibendum risus. Ut sagittis lacus vitae arcu feugiat, ultrices lacinia odio vestibulum. Nam non hendrerit tucpis. In hac habitasse platea dictumst. Curabitur pulvinar fermentum ex, eu ullamcorper sem dapibus at. Integer ut dui arcu. Maecenas nec purus tincidunt, molestie enim quis, vulputate tortor. Mauris mollis, diam nec vestibulum commodo, mauris nibh dictum ex, vel mattis magna diam sed enim. Suspendisse id augue tortor. Nulla sit amet urna a turpis porttitor tincidunt et vitae enim. Curabitur nec condimentum felis, pulvinar luctus dui. Donec volutpat feugiat nibh, eu tempus nisl molestie at
\#  <!-- Use \# for scene divides -->
    Nunc maximus nisi eget metus malesuada, eu mattis erat sagittis. Praesent pellentesque mi eu congue volutpat. Praesent nec augue sit amet sem pharetra vestibulum id a erat. Vivamus mi arcu, gravida vitae sapien ac, facilisis laoreet turpis. Vestibulum arcu orci, varius nec arcu et, porta rutrum eros. Integer a mi non urna congue bibendum. <!-- Use a single asterik to italicize text --> *Proin et leo lacus. In eget velit aliquet, feugiat turpis a, consequat lorem.* Vivamus egestas velit lorem, sit amet malesuada est tempus a. Integer quam velit, suscipit eget felis pellentesque, venenatis laoreet nunc. Nulla* maximus mattis varius. Pellentesque enim mi, molestie ac interdum in, dictum nec dui.
\#

<!-- Kilroy was here. --> 
    Maecenas rhoncus libero in posuere dignissim. Donec mollis, mauris vitae vehicula lacinia, dolor leo cursus odio, vitae auctor ante orci ut augue. Vestibulum mi felis, facilisis a tortor nec, vestibulum mollis est. Integer quis nibh at ex commodo laoreet quis ac mauris. Aliquam ac mauris eu nulla aliquam auctor. *Duis metus tortor, dapibus sed pulvinar maximus, posuere sodales tellus.* Donec non est vitae lacus tincidunt finibus eget at sem. Duis efficitur vel orci vel iaculis. Pellentesque vitae luctus ante. Sed non nulla feugiat, malesuada augue at, vulputate neque. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam tortor dolor, tincidunt eu ultrices ut, sollicitudin et lorem. In aliquam bibendum interdum. Maecenas vitae euismod leo. In vel ipsum libero. Integer eu mattis lectus, venenatis cursus massa.
\#
    Morbi sit amet diam enim. Nulla eleifend facilisis tellus at ultrices. Ut maximus arcu id magna facilisis, non commodo orci venenatis. Sed dictum finibus dui nec laoreet. Mauris ut metus vel est imperdiet blandit eu vitae magna. Sed eleifend laoreet dignissim. Etiam auctor elit nunc, sed eleifend arcu porta et. Maecenas sed nunc turpis. Cras dignissim, diam sed aliquam sodales, augue metus viverra ex, in consectetur sem ligula quis turpis. Morbi facilisis consequat mi, at rutrum mi.
\#


3. Critical Markup plugin can be accessed with __CTRL + P O__ and exited with __CTRL + P P__

*Accept/reject Critical Markup* __CTRL + O A__

*deletion/subtraction/comment menu* __CTROL + O S__

# Search and Navigation

*Search file* __CTRL + Q F__

*Global file/folder search (configurible* __CTRL + L F__

# *Cycle previous or next HASH* __CTRL+SHIFT + PgUp/PgDn__ 

*Next tab navigation* __CTRL + L D__

*Previous tab nav* __CTRL + L S__

# Enter / Exit Fullcreen and Distraction-free Mode

*Enter/Exit Fullscreen Mode* __Down Arrow__

*Enter/Exit Distraction-free Mode* __Up Arrow__

*Show/Hide File Navigator* __Left Arrow__

# Highlighting (i.e. selecting chars words with caret)

1. Highlight word, line, or paragraph with __CTRL + j j__ or __CTRL + j k__ or __CTRL + j l__ respectively.

\#

# Personally, I use single hashes for HIGH PRIORITY SECTIONS THAT NEED ATTENTION SOMEDAY; you can use them however the fuck you want.
<!-- A comment must follow HASHES to break back into green text for your paragraph below. -->
    Praesent venenatis varius eleifend. Sed a eleifend tellus. Integer commodo nisi in erat convallis volutpat. Nulla 
\#

    Also:

*select char forward* __CTRL + 3__

*Select char backward* __CTRL + 2__

*Select line forward*  __CTRL + 4__

*Select line backward* __CTRL + 1__

\#

# Cut and paste

*cut* __CTRL + K X__

*paste* __CTRL + K V__

*Paste selection from buffer (from clipboard plugin)*  __CTRL + J V__

*Undo* __CTRL + Z__
# Save (or be sorry!)

NOTE ON SAVING: Default configure omes with Autobackup installed (please configure plugin target directory yourself ... defaults to ~/Sync/manuscripts/WIPs/sublime_backups last I checked)

*Save* __CTRL + K S__

*Save as...* __CTRL + K A__

*New file (allows path selection)*  __CTRL + K N__

# Last But Not Least, functions / config options via Command Pallete menu

*Sublime's Command Pallete* __CTRL + K K__

# Scripts for PDF, epub generation with pandoc

If you downloaded these from healingrant.com, put these in a path that's in your $PATH, usually set in ~/.bashrc, but your milage may vary with linux distros other than Manjaro. NO WARRANTY!
\#

    Prereqs + INSTALLATION INSTRUCTION (read if you want in-house pdf preview and epub gen)

1. Open guake terminal by hitting ~ (or any terminal you have installed) and edit script in ~/.scripts called **gen_wordsmith_profile** to your liking, mainly change target directories, manuscript name, author name, etc.
5. Bootstrap wordsmith project by running __start-gen-wordsmith-project__ in quake terminal.
6. Now switch to Sublime Text, and add your project dir folder from the drop-down menu __Project/Add Folder to Project__ ... (in the included template--assuming you didn't change shit which you should!--will be __$HOME/Sync/manuscripts/Novels/your_manuscript__ 
7. Add new file to __content__ folder. name each chapter/break file leading with 00_ i.e. 00_this_is_my_first_chapter.md. 01_2nd_chapter.md 02_3rd.md 03_4th_etc.md 
8. Remember to use markdown in file! You can search the internet on HOWTO markdown if you're not familiar with its capabilities. Use # for title, otherwise, pdf/epub mobi generation may be horrid!
9. After writing a bit, generate a pdf! Note: These script should work under i3, gnome, trinity, or plasma. Under i3, it should automatically open your pdf on the 2nd workspace (also should work if using trinity desktop.)


*Generate PDF* __ALT + P__

\#

     Outline generation

1. cp reference-outline.odt to $HOME/.pandoc-outline/reference.odt
2. make sure you copied over ever gen_ and start- script fro mthe zip file, and that they are executable and in your $PATH
3. create a new file in root dir of your project, i.e. /home/lain/Syncthing/manuscripts/Novels/your_manuscript/$DOS_DIR-outline.md

so give it the same name as you designated your DOS_DIR in gen_wordsmith_profile. (The default the DOS_DIR is called YOURMANU

*Generate Outline* __ALT+SHIFT + P__

# TODO / FURTHER NOTES

1. mobi / epub gen


*generate_ebook*  __ALT + I__

As of writing this, I'm not sure if I'll include mobi/epub gen, and auto import into CAlibre for the first release. If it's there, it'll probably be epub only at first, then you can pretty up the epub to mobi through Calibre.

You can also manually generate ebooks yourself from the terminal under the project root dir by envoking __wordsmith g epub__ or wordsmith g mobi or wordsmith g odt. Your MILEAGE MAY VARY when manually doing this.

3. WORDSTAR file conversion (i.e. ws7 to md, or MD to txt to import to Wordstar under DOSBOX). There's a nice script out in the wild somewhere called wschange.py -- forget the project name, but easily discoverable with a google search.

On my personal Linux setups, I have Wordstar 7 emulated nicely under Dosbox which I can share project chapters nicely. I have scripts that work, maybe I'll include those in the next release.

5. kindelgen previewer w/ wine

bundling old skool windows kindlegen previewer 2.97 would not be kosher ... perhaps a script you can run will suffice (assuming there's actually an online mirror somewhere.)

# Wordstar LinuxDistro TODOS

1. Custom graphics!

The placeholders (or lack thereof) may become a final release (for now.)

2. df
3. 
                        
                        
                        
                    
                    
                    

# A bunch of other shit that's undocumented, but feel free to modify and enchance!


# Hi mom! Doo da doo da doo da doo do doo.

[^1]: Really
