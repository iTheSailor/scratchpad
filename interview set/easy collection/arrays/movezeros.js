// var moveZeroes = function(nums) {
//     let a = nums.length-1;
//     var b = 0;
//     while(a >=0){
//         if(nums[a] === 0){
//             b+=1
//         };
//         a--;

//     }
//     if(b>0){
//         nums = nums.filter((n) => n!== 0);
//         while(b>0){
//             nums.push(0)
//             b--
//             console.log(nums)
//         }

//     }
//     console.log(b)
//     console.log(nums)
//     return nums

// };
//the above doesnt work i guess because im not altering nums in place

var moveZeroes = function(nums) {
    let a = nums.length-1;
    if(a===0){return nums};
    var b=0;
    while(a>=0){
        if(nums[a]===0){
            nums.splice(a,1)
            nums.push(0)
        }
        a--;
    }
}
nums = [0,1,0,3,12]
moveZeroes(nums)