var containsDuplicate = function(nums) {
    nums.sort((a, b) => a - b);  
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === nums[i - 1]) {
            return true;
        }
    }  
    return false;
};
nums = [1,1,1,3,3,4,3,2,4,2]
// nums = [0]
// nums = [1,2,3,4]
// nums = [2,14,18,22,22]
// nums = [1,5,-2,-4,0]
console.log(containsDuplicate(nums))
// console.log(nums.slice())
// console.log(nums.indexOf(22))
