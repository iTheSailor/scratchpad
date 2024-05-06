var intersect = function(nums1, nums2) {
    let i=0,j=0;
    let res = [];
    nums1.sort((a,b) => a-b);
    nums2.sort((a,b) => a-b);
    while(i<nums1.length && j<nums2.length){
        if(nums1[i] === nums2[j]){
            res.push(nums1[i]);
            i++;
            j++;
        } else if(nums1[i]>nums2[j]){
            j++;
        } else{
            i++;
        }
    }
    return res;
};

nums1 = [4,9,5], nums2 = [9,4,9,8,4]
console.log(intersect(nums1, nums2))