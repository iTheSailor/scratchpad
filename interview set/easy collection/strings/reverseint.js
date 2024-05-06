var reverse = function(x) {
    y=x
    let s ='',h;
    if(x<0){y=x*-1; h=1}
    z=String(y)
    for(i=z.length-1;i>-1;i--){
        s+=z[i]
        console.log(s)
        console.log(z)
    }
    r=Number(s)
    console.log(r)
    if(h==1){return r*-1}
    console.log(r)
    if(-2^31 <= r){return 0}
    return r
};

x=321
console.log(reverse(x))