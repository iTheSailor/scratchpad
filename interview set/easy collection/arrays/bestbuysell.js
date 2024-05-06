var maxProfit = function(prices) {
    var i , j = 1, k, total=0;
    for (i = 0; i < prices.length; i++){
        if (prices[j]-prices[i] > 0){
            k = prices[j]-prices[i]
            total += k
        }
        j++
    }
    return total
};

// prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]

maxProfit(prices)