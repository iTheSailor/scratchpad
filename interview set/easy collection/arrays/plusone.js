// var plusOne = function(digits) {
//     let a = '';
//     for(let i = 0; i<digits.length; i++){
//         let num = digits[i];
//         a += num.toString();
//         console.log(a)
//     }
//     let b = Number(a);
//     b += 1
//     let c = b.toString();
//     let d =[];
//     for(let i = 0; i<c.length; i++){
//         d.push(Number(c[i]))
//         console.log(d)
//     }
//     console.log(d)
// };
// above fails because the integer quanity is higher than the max safe integer limit in javascript

var plusOne = function(digits){
    let a = 1;
    let b = digits.length-1
    while(b >= 0){
        digits[b]+= a;
        if(digits[b] <= 9){
            console.log(digits);
            return digits;
        }
        digits[b]=0;
        b--;
    }
    if(carry){
        digits.unshift(carry);
    }
    console.log(digits);
    return digits;
}
digits = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]
plusOne(digits)