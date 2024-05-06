var singleNumber = function(nums) {
    if(nums.length == 1){return nums[0]};
    nums.sort((a,b) => a-b);
    for(let i = 0; i<nums.length; i++){
        if(nums[i] !== nums[i+1] & nums[i] !== nums[i-1]){
            return nums[i]
        }
    }
    
};

nums = [4,1,2,1,2]
console.log(singleNumber(nums))