var twoSum = function(nums, target) {
    let a;
    let i,j;
    let res =[];
    for(i=0;i<nums.length; i++){
        for(j=i+1;j<nums.length;j++){
            a = target-nums[i]
            if(nums[j] == a){
                res.push(i)
                res.push(j)
            }
        }

    }
    return res
};

nums = [2,7,11,15], target = 9
twoSum(nums, target)