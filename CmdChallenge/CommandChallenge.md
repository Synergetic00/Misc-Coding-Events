# cmdchallenge.com

## :snail: hello world

### Prompt

```
Your first challenge is to print "hello world" on the terminal in a single command.

Hint: There are many ways to print text on the command line, one way is with the 'echo' command. Try it below and good luck!
```

### Solution

```
echo "hello world"
```

### Output

```
hello world
```

## :butterfly: cwd

### Prompt

```
Print the current working directory.
```

### Solution

```
pwd
```

### Output

```
/var/challenges/current_working_directory
```

## :bug: list files

### Prompt

```
List names of all the files in the current directory, one file per line.
```

### Solution

```
ls
```

### Output

```
01-take.txt
02-the.txt
03-command.txt
04-challenge.txt
```

## :ant: file contents

### Prompt

```
There is a file named access.log in the current directory. Print the contents.
```

### Solution

```
cat access.log
```

### Output

```
163.56.115.58 - - [09/Jan/2017:22:29:57 +0100] "GET /posts/2/display HTTP/1.0" 200 3240
75.113.188.234 - - [09/Jan/2017:22:30:43 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 1116
69.16.40.148 - - [09/Jan/2017:22:34:33 +0100] "GET /pages/create HTTP/1.0" 500 3471
225.219.54.140 - - [09/Jan/2017:22:35:30 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 500 2477
207.243.19.2 - - [09/Jan/2017:22:38:03 +0100] "GET /bar/create HTTP/1.0" 200 1116
199.37.62.156 - - [09/Jan/2017:22:42:18 +0100] "GET /posts/1/display HTTP/1.0" 200 2477
55.74.240.123 - - [09/Jan/2017:22:44:25 +0100] "POST /posts/1/display HTTP/1.0" 200 3471
251.111.109.143 - - [09/Jan/2017:22:49:02 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 2477
101.163.230.250 - - [09/Jan/2017:22:52:31 +0100] "DELETE /posts/2/display HTTP/1.0" 404 2477
200.19.168.148 - - [09/Jan/2017:22:57:11 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 3471
```

## :spider_web: last lines

### Prompt

```
Print the last 5 lines of "access.log".
```

### Solution

```
tail -5 access.log
```

### Output

```
199.37.62.156 - - [09/Jan/2017:22:42:18 +0100] "GET /posts/1/display HTTP/1.0" 200 2477
55.74.240.123 - - [09/Jan/2017:22:44:25 +0100] "POST /posts/1/display HTTP/1.0" 200 3471
251.111.109.143 - - [09/Jan/2017:22:49:02 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 2477
101.163.230.250 - - [09/Jan/2017:22:52:31 +0100] "DELETE /posts/2/display HTTP/1.0" 404 2477
200.19.168.148 - - [09/Jan/2017:22:57:11 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 3471
```

## :whale2: Create a file

### Prompt

```
Create an empty file named take-the-command-challenge in the current working directory.
```

### Solution

```
touch take-the-command-challeng
```

## :whale: Create a directory

### Prompt

```
Create a directory named tmp/files in the current working directory
```

### Solution

```
mkdir -p tmp/files
```

## :dolphin: copy file

### Prompt

```
Copy the file named take-the-command-challenge to the directory tmp/files
```

### Solution

```
cp take-the-command-challenge tmp/files
```

## :fish: move file

### Prompt

```
Move the file named take-the-command-challenge to the directory tmp/files
```

### Solution

```
mv take-the-command-challenge tmp/files
```

## :tropical_fish: create symlink

### Prompt

```
A symbolic link is a type of file that is a reference to another file.

Create a symbolic link named take-the-command-challenge that points to the file tmp/files/take-the-command-challenge.
```

### Solution

```
ln -s tmp/files/take-the-command-challenge take-the-command-challenge
```

## :blowfish: delete files

### Prompt

```
Delete all of the files in this challenge directory including all subdirectories and their contents.
```

### Solution

```
rm -r * .*
```

### Output

```
rm: refusing to remove '.' or '..' directory: skipping '.'
rm: refusing to remove '.' or '..' directory: skipping '..'
```

## :wolf: remove files with extension

### Prompt

```
There are files in this challenge with different file extensions. Remove all files with the .doc extension recursively in the current working directory.
```

### Solution

```
rm **/*.doc
```

## :bee: find string

### Prompt

```
There is a file named access.log in the current working directory. Print all lines in this file that contains the string "GET".
```

### Solution

```
grep GET access.log
```

### Output

```
163.56.115.58 - - [09/Jan/2017:22:29:57 +0100] "GET /posts/2/display HTTP/1.0" 200 3240
75.113.188.234 - - [09/Jan/2017:22:30:43 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 1116
69.16.40.148 - - [09/Jan/2017:22:34:33 +0100] "GET /pages/create HTTP/1.0" 500 3471
225.219.54.140 - - [09/Jan/2017:22:35:30 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 500 2477
207.243.19.2 - - [09/Jan/2017:22:38:03 +0100] "GET /bar/create HTTP/1.0" 200 1116
199.37.62.156 - - [09/Jan/2017:22:42:18 +0100] "GET /posts/1/display HTTP/1.0" 200 2477
251.111.109.143 - - [09/Jan/2017:22:49:02 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 2477
200.19.168.148 - - [09/Jan/2017:22:57:11 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 3471
```

## :beetle: search for string

### Prompt

```
Print all files in the current directory, one per line (not the path, just the filename) that contain the string "500".
```

### Solution

```
grep -lr 500
```

### Output

```
access.log.1
access.log
```

## :cricket: search for extension

### Prompt

```
Print the relative file paths, one path per line for all filenames that start with "access.log" in the current directory.
```

### Solution

```
find . -name "access.log*"
```

### Output

```
./access.log.1
./access.log
./access.log.2
```

## :spider: search recursive

### Prompt

```
Print all matching lines (without the filename or the file path) in all files under the current directory that start with "access.log" that contain the string "500".

Note that there are no files named access.log in the current directory, you will need to search recursively.
```

### Solution

```
ls **/access.log* | grep -hr 500
```

### Output

```
2.71.250.27 - - [09/Jan/2017:22:41:26 +0100] "GET /pages/create HTTP/1.0" 500 2477
69.16.40.148 - - [09/Jan/2017:22:34:33 +0100] "GET /pages/create HTTP/1.0" 500 3471
225.219.54.140 - - [09/Jan/2017:22:35:30 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 500 2477
```

## :scorpion: find ip address

### Prompt

```
Extract all IP addresses from files that start with "access.log" printing one IP address per line.
```

### Solution

```
ls **/access.log* | grep -Pro '^([0-9.]){3,}[0-9]'
```

### Output

```
var/log/httpd/access.log.1:108.68.174.15
var/log/httpd/access.log.1:17.2.20.139
var/log/httpd/access.log.1:28.151.137.59
var/log/httpd/access.log.1:199.150.241.179
var/log/httpd/access.log.1:2.71.250.27
var/log/httpd/access.log.1:17.137.186.194
var/log/httpd/access.log.1:151.84.119.34
var/log/httpd/access.log.1:4.180.204.195
var/log/httpd/access.log.1:9.230.96.54
var/log/httpd/access.log.1:157.143.233.21
var/log/httpd/access.log:163.56.115.58
var/log/httpd/access.log:75.113.188.234
var/log/httpd/access.log:69.16.40.148
var/log/httpd/access.log:225.219.54.140
var/log/httpd/access.log:207.243.19.2
var/log/httpd/access.log:199.37.62.156
var/log/httpd/access.log:55.74.240.123
var/log/httpd/access.log:251.111.109.143
var/log/httpd/access.log:101.163.230.250
var/log/httpd/access.log:200.19.168.148
```

## :fly: count files

### Prompt

```
Count the number of files in the current working directory. Print the number of files as a single integer.
```

### Solution

```
ls -l | wc -l
```

### Output

```
2
```

## :worm: simple sort

### Prompt

```
Print the contents of access.log sorted.
```

### Solution

```
sort access.log
```

### Output

```
101.163.230.250 - - [09/Jan/2017:22:52:31 +0100] "DELETE /posts/2/display HTTP/1.0" 404 2477
163.56.115.58 - - [09/Jan/2017:22:29:57 +0100] "GET /posts/2/display HTTP/1.0" 200 3240
199.37.62.156 - - [09/Jan/2017:22:42:18 +0100] "GET /posts/1/display HTTP/1.0" 200 2477
200.19.168.148 - - [09/Jan/2017:22:57:11 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 3471
207.243.19.2 - - [09/Jan/2017:22:38:03 +0100] "GET /bar/create HTTP/1.0" 200 1116
225.219.54.140 - - [09/Jan/2017:22:35:30 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 500 2477
251.111.109.143 - - [09/Jan/2017:22:49:02 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 2477
55.74.240.123 - - [09/Jan/2017:22:44:25 +0100] "POST /posts/1/display HTTP/1.0" 200 3471
69.16.40.148 - - [09/Jan/2017:22:34:33 +0100] "GET /pages/create HTTP/1.0" 500 3471
75.113.188.234 - - [09/Jan/2017:22:30:43 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 1116
```

## :microbe: count the strings

### Prompt

```
Print the number of lines in access.log that contain the string "GET".
```

### Solution

```
grep GET access.log | wc -l
```

### Output

```
8
```

## :monkey_face: split on a char

### Prompt

```
The file split-me.txt contains a list of numbers separated by a ; character.

Split the numbers on the ; character, one number per line.
```

### Solution

```
cat split-me.txt | tr ';' '\n'
```

### Output

```
1
2
3
4
5
6
7
8
9
10
```

## :dog: generate a number sequence

### Prompt

```
Print the numbers 1 to 100 separated by spaces.
```

### Solution

```
echo {1..100}
```

### Output

```
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100
```

## :fox_face: replace text in files

### Prompt

```
This challenge has text files (with a .txt extension) that contain the phrase "challenges are difficult". Delete this phrase from all text files recursively.

Note that some files are in subdirectories so you will need to search for them.
```

### Solution

```
sed -i 'challenges are difficult' **/*.txt
```

## :cat: sum the numbers

### Prompt

```
The file sum-me.txt has a list of numbers, one per line. Print the sum of these numbers.
```

### Solution

```
cat sum-me.txt | echo $((`tr '\n' '+'`0))
```

### Output

```
42
```

## :lion: only the file names

### Prompt

```
Print all files in the current directory recursively without the leading directory path.
```

### Solution

```
ls -R | grep [A-z]
```

### Output

```
beatae.flac
error.doc
libero.xls
necessitatibus.doc
totam
animi.doc
corporis.xls
odit.doc
```

## :tiger: remove extensions

### Prompt

```
Rename all files removing the extension from them in the current directory recursively.
```

### Solution

```
rename 's/\.\w+$//g' **/*
```

## :horse: replace spaces

### Prompt

```
The files in this challenge contain spaces. List all of the files (filenames only) in the current directory but replace all spaces with a '.' character.
```

### Solution

```
ls | tr ' ' '.'
```

### Output

```
Adam.Simpson
Alexis.Stein
Allison.Brown
Amy.Anderson
Angel.Saunders
Brad.Michael
Briana.Wilson
Carrie.Alexander
Christine.Valdez
Christopher.Miller
Claudia.Mccormick
Corey.Bird
Courtney.Miller
Crystal.Dunn
Crystal.Valdez
Erica.Richardson
James.Harper
James.Roberts
Jared.Hill.DVM
John.Nguyen
Jorge.Ross
Joseph.Hurst
Karen.Ramirez
Kevin.Price
Kimberly.Parker
Lori.Macias
Luke.Mason
Lynn.Robinson
Mallory.Peterson
Marie.Gutierrez
Matthew.Romero
Michaela.Hobbs
Molly.Stevens
Mr..James.Lopez
Mr..Shawn.Martin
Mrs..Jade.Clark
Olivia.Irwin
Parker.Gilbert
Robert.Gregory
Robert.Hill
Sarah.Hill
Scott.Rice
Sheri.Bishop
Tamara.Anderson
Tammy.Galloway
Terri.Young
Thomas.Parks
Thomas.Washington
Tiffany.Clark
Yvonne.Myers
```

## :unicorn: directories containing files

### Prompt

```
In this challenge there are some directories containing files with different extensions. Print all directories, one per line without duplicates that contain one or more files with a ".tf" extension.
```

### Solution

```
dirname **/*.tf | uniq
```

### Output

```
terraform
terraform/modules/load_balancer
terraform/modules/virtual_machine
terraform/modules/vpn
```

## :cow: files starting with a number

### Prompt

```
There are a mix of files in this directory that start with letters and numbers. Print the filenames (just the filenames) of all files that start with a number recursively in the current directory.
```

### Solution

```
ls -Rp | grep ^[0-9] | grep -v /
```

- `ls -Rp` list directory contents (recursively and put '/' for a directory)
- `grep ^[0-9]` find lines where the first character is a number
- `grep -v /` inverted search, find all lines without  '/'

### Output

```
04Carrie Alexander
132Rebecca Rubio
25Brandon Mcdonald
293Linda Bennett
335John Joseph
388Andrew Carter
402Nancy Henson
42Robert Hill
436Teresa Owens
477Thomas Pierce MD
48Thomas Allen
511Tammy Welch
540Katherine Jones
593Brett Martin
639Charles Ferguson
670James Jacobs
682Terri Jones
737Jeffrey Davis
757Robert Marquez
778Holly Archer
78Michelle Spencer
974Michael Bowman
3maxime.mp3
99blanditiis.avi
```

## :pig: nth line

### Prompt

```
Print the 25th line of the file faces.txt
```

### Solution

```
head -n 25 faces.txt | tail -1
```

### Output

```
¯\_(ツ)_/¯
```

## :mouse: reverse

### Prompt

```
Print the lines of the file reverse-me.txt in this directory in reverse line order so that the last line is printed first and the first line is printed last.

~~~~~~~~~~~~~~~~~~~~~
In the future
Environmental destruction will be the norm
No longer can it be said that
My peers and I care about this earth
It will be evident that
My generation is apathetic and lethargic
It is foolish to presume that
There is hope
~~~~~~~~~~~~~~~~~~~~~
-Jonathan Reed "The Lost Generation"
```

### Solution

```
tac reverse-me.txt
```

### Output

```
-Jonathan Reed "The Lost Generation"
~~~~~~~~~~~~~~~~~~~~~
There is hope
It is foolish to presume that
My generation is apathetic and lethargic
It will be evident that
My peers and I care about this earth
No longer can it be said that
Environmental destruction will be the norm
In the future
~~~~~~~~~~~~~~~~~~~~~
```

## :hamster:

### Prompt

```
Print the file faces.txt, but only print the first instance of each duplicate line, even if the duplicates don't appear next to each other.

Note that order matters so don't sort the lines before removing duplicates.
```

### Solution

```
awk '!seen[$0]++' faces.txt
```

- `awk <command> <file>` pattern scanning and processing language
- `$0` the whole line input of awk, the arguments are `$1, $2, ...`
- `seen[$0]` arbritrary array of all of the faces with values initally of 0
- `seen[$0]++` increment the value at the entry for the given key of the face
- `!seen[$0]++` since they are either 0 or not, it's a boolean, so `!arr[key]` will only be true if it's the first because `0` is false and `!` inverts it to true, since otherwise it will increment and thus it will be false and not be output to the console

### Output

```
(◕‿◕)
(^̮^)
ʘ‿ʘ
ಠ_ಠ
ಠ⌣ಠ
ಠ‿ಠ
(ʘ‿ʘ)
(ಠ_ಠ)
¯\_(ツ)_/¯
(ಠ⌣ಠ
ಠಠ⌣ಠ)
(ಠ‿ಠ)
٩◔̯◔۶
ヽ༼ຈل͜ຈ༽ﾉ
♥‿♥
◔̯◔
⊙﹏⊙
(¬_¬)
(；一_一)
(͡° ͜ʖ ͡°)
(° ͜ʖ °)
¯\(°_o)/¯
( ﾟヮﾟ)
(︺︹︺)
```

## :bear: finding prime numbers

### Prompt

```
The file random-numbers.txt contains a list of 100 random integers. Print the number of unique prime numbers contained in the file.
```

### Solution

```
sort -u random-numbers.txt | factor | awk 'NF<3' | wc -l
```

### Output

```
12
```

## :panda_face: printing common lines

### Prompt

```
access.log.1 and access.log.2 are http server logs.

Print the IP addresses common to both files, one per line.
```

### Solution

```
awk '++seen[$1]==2{print $1}' access.log*
```

### Output

```
17.137.186.194
2.71.250.27
28.151.137.59
108.68.174.15
```

## :hatching_chick: printing lines before match

### Prompt

```
Print all matching lines (without the filename or the file path) in all files under the current directory that start with "access.log", where the next line contains the string "404".

Note that you will need to search recursively.
```

### Solution

```
awk '/404/{print prev}{prev=$0}' **/access.log*
```

If the line matches exactly 404, then print the value, after assign it, so that next time this command is run, prev holds the previous value.

### Output

```
251.111.109.143 - - [09/Jan/2017:22:49:02 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 2477
17.137.186.194 - - [09/Jan/2017:22:43:17 +0100] "GET /pages/create HTTP/1.0" 200 1116
89.148.148.238 - - [09/Jan/2017:22:33:09 +0100] "GET /posts/1/display HTTP/1.0" 502 2477
138.212.253.84 - - [09/Jan/2017:22:53:54 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 3471
```

## :peacock: files that are different

### Prompt

```
Print all files with a .bin extension in the current directory that are different than the file named base.bin.
```

### Solution

```
diff *.bin --to-file base.bin | cut -d ' ' -f 3
```

- `diff *.bin --to-file base.bin` compare files with .bin extension to base.bin
- `cut -d ' ' -f 3` get the third argument which is the file name

### Output

```
test2.bin
test4.bin
test5.bin
test7.bin
```

## :frog: tricky file

### Prompt

```
There is a file: ./.../ /. .the flag.txt

Show its contents on the screen.
```

### Solution

```
cat "$(find |grep flag)"
```

### Output

```
you got it!
```

## :dragon_face: find tabs in file

### Prompt

```
How many lines contain tab characters in the file named file-with-tabs.txt in the current directory.
```

### Solution

```
grep -c $'\t' file-with-tabs.txt
```

### Output

```
3
```

## :hibiscus: Remove files without extension.

### Prompt

```
There are files in this challenge with different file extensions.

Remove all files without the .txt and .exe extensions recursively in the current working directory.
```

### Solution

```
find ! -regex '.*\(txt\|exe\)$' -delete
```

### Output

```
find: cannot delete './b': Directory not empty
find: cannot delete './c/m': Directory not empty
find: cannot delete './c': Directory not empty
```

## :: Remove files that start with a dash

### Prompt

```
There are some files in this directory that start with a dash in the filename. Remove those files.
```

### Solution

```
rm ./-*
```

## :tulip: Print the contents sorted by PID

### Prompt

```
There are two files in this directory, ps-ef1 and ps-ef2. Print the contents of both files sorted by PID and delete repeated lines.
```

### Solution

```
sort -unk2 ps-ef*
```

- `-u` only output the unique values
- `-n` sort based on the numerical value of the key
- `-k 2` set the sorting key to be the value in the second column

### Output

```
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 mar04 ?        00:00:13 /sbin/init
root         2     0  0 mar04 ?        00:00:00 [kthreadd]
root         3     2  0 mar04 ?        00:01:07 [ksoftirqd/0]
user         5     2  0 mar04 ?        00:00:00 [kworker/0:0H]
user         7     2  0 mar04 ?        00:07:06 [rcu_sched]
user         8     2  0 mar04 ?        00:00:00 [rcu_bh]
root         9     2  0 mar04 ?        00:00:00 [migration/0]
root        10     2  0 mar04 ?        00:00:04 [watchdog/0]
user        11     2  0 mar04 ?        00:00:04 [watchdog/1]
root        12     2  0 mar04 ?        00:00:00 [migration/1]
root        13     2  0 mar04 ?        00:00:59 [ksoftirqd/1]
user        15     2  0 mar04 ?        00:00:00 [kworker/1:0H]
user        16     2  0 mar04 ?        00:00:04 [watchdog/2]
root        17     2  0 mar04 ?        00:00:00 [migration/2]
root        18     2  0 mar04 ?        00:00:59 [ksoftirqd/2]
root        20     2  0 mar04 ?        00:00:00 [kworker/2:0H]
user        21     2  0 mar04 ?        00:00:04 [watchdog/3]
root        22     2  0 mar04 ?        00:00:00 [migration/3]
root        23     2  0 mar04 ?        00:01:29 [ksoftirqd/3]
```

## :sunflower: print the ports

### Prompt

```
In the current directory there is a file called netstat.out.

Print all the IPv4 listening ports sorted from the higher to lower.
```

### Solution

```
```

### Output

```
```

## ::

### Prompt

```
```

### Solution

```
```

### Output

```
```

## ::

### Prompt

```
```

### Solution

```
```

### Output

```
```

## ::

### Prompt

```
```

### Solution

```
```

### Output

```
```

## ::

### Prompt

```
```

### Solution

```
```

### Output

```
```

## ::

### Prompt

```
```

### Solution

```
```

### Output

```
```

## ::

### Prompt

```
```

### Solution

```
```

### Output

```
```

## ::

### Prompt

```
```

### Solution

```
```

### Output

```
```

## ::

### Prompt

```
```

### Solution

```
```

### Output

```
```

## ::

### Prompt

```
```

### Solution

```
```

### Output

```
```

## ::

### Prompt

```
```

### Solution

```
```

### Output

```
```

## ::

### Prompt

```
```

### Solution

```
```

### Output

```
```

## ::

### Prompt

```
```

### Solution

```
```

### Output

```
```

## ::

### Prompt

```
```

### Solution

```
```

### Output

```
```

## ::

### Prompt

```
```

### Solution

```
```

### Output

```
```