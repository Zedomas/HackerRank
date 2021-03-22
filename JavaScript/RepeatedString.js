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