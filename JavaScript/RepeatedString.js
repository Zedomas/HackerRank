/*

There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first  letters of the infinite string.

Example
s = "abcac"
n = 10

The substring we consider is abcacabcac, the first 10 characters of the infinite string. There are 4 occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Returns

int: the frequency of a in the substring
Input Format

The first line contains a single string, s.
The second line contains an integer, n.



*/

function repeatedString(s, n) {
    let acount = 0
    
    if(n >= s.length) {
        let timesOfA = [...s].filter(e => e === "a").length
        
        acount = Math.floor(n/s.length) * timesOfA
    }
    
    let tail = n % s.length;
    
    for(let i = 0; i< tail; i++) {
        if(s[i] === "a") acount++;
    }
    
    return acount
}