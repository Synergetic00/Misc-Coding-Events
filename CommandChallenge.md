# cmdchallenge.com

## :snail:

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

## :butterfly:

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

## :bug:

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

## :ant:

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

## :spider_web:

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

## :whale2:

### Prompt

```
Create an empty file named take-the-command-challenge in the current working directory.
```

### Solution

```
touch take-the-command-challeng
```

### Output

```
```

## :whale:

### Prompt

```
Create a directory named tmp/files in the current working directory
```

### Solution

```
mkdir -p tmp/files
```

### Output

```
```

## :dolphin:

### Prompt

```
Copy the file named take-the-command-challenge to the directory tmp/files
```

### Solution

```
cp take-the-command-challenge tmp/files
```

### Output

```
```

## :fish:

### Prompt

```
Move the file named take-the-command-challenge to the directory tmp/files
```

### Solution

```
mv take-the-command-challenge tmp/files
```

### Output

```
```

## :tropical_fish:

### Prompt

```
A symbolic link is a type of file that is a reference to another file.

Create a symbolic link named take-the-command-challenge that points to the file tmp/files/take-the-command-challenge.
```

### Solution

```
ln -s tmp/files/take-the-command-challenge take-the-command-challenge
```

### Output

```
```

## :blowfish:

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

## :wolf:

### Prompt

```
There are files in this challenge with different file extensions. Remove all files with the .doc extension recursively in the current working directory.
```

### Solution

```
rm **/*.doc
```

## :bee:

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