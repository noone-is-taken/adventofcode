Start with the input in your vim script.

Remove Everything except regex. mul([0-9]*,[0-9]*) is the regex to preseve
https://stackoverflow.com/questions/4503748/remove-everything-except-regex-match-in-vim
::let @a=""|%s/mul([0-9]*,[0-9]*)/\=setreg('A', submatch(0), 'l')/g|%d _|pu a|0d _

Substitutes to clean data
Eliminates mul(1,1) and transform to 1 * 1
:%s/mul(//g 
:%s/,/*/g

eliminates breakline to sum operations
:%s/)\n/+/g

Calculate opretions:
http://vimcasts.org/episodes/simple-calculations-with-vims-expression-register/
yy operation and in a new line calculate result
note: the copy command puts a extra character that you need to remove
yy O <C-r>= <C-r>" <CR> <Esc>


