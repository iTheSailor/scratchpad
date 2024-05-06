var rotate = function(nums, k) {
    if(k > nums.length){k = k % nums.length}
    let j = nums.splice(-k, k)
    j.reverse()
    for(i = 0; i<j.length; i++){
        nums.unshift(j[i])
    }
};

nums = [1,2], k = 3
console.log(nums)
rotate(nums, k)