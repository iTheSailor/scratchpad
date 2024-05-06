var isValidSudoku = function(board) {
    for(let a=0; a<board.length; a++){
        let x = new Set();
        let y = new Set();
        let z = new Set();
        for(let b=0; b<board[a].length; b++){
            let c = board[a][b];
            let d = board[b][a];
            let zx = 3*Math.floor(a/3);
            let zy = 3*Math.floor(b/3);
            let e = board[zx + a%3][zy + b%3];
            if(c !=='.'){
                if(x.has(c))
                    return false;
                
                x.add(c);
            }
            if(d !=='.'){
                if(y.has(d))
                    return false;
                
                y.add(d);
            }
            if(e !=='.'){
                if(z.has(e))
                    return false;
                
                z.add(e);
            }
        }
    }
    return true
};

// console.log(3*(1%3)+(4%3))

board=[

[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","3"],
[".",".","4",".",".",".",".","3","."]]
console.log(isValidSudoku(board))



// console.log(parseInt(board[0][0]))
// let y=0;
//     while(y<board.length){
//         let i =[];
//         for(let x =0; x<board[y].length; x++){
//             let num=parseInt(board[y][x]);
//             if(!isNaN(num)){
//                 i.push(num)
//             }
//             i.sort((a,b) => a-b)
//             if(i.length>1){
//                 for(let j = 0; j<i.length-1;j++){
//                     if(i[j] == i[j+1]){
//                         return false
//                     }
//                 }
//             }
//         }
//         y++
//     }
//     let x=0;
//     while(x<board.length){
//         let i = []
//         for(let y=0; y<board.length; y++){
//             let num=parseInt(board[y][x])
//             if(!isNaN(num)){
//                 i.push(num)
//             }
//             i.sort((a,b) => a-b)
//             if(i.length>1){
//                 for(let j = 0; j<i.length-1;j++){
//                     if(i[j] == i[j+1]){
//                         return false
//                     }
//                 }
//             }
//         }
//         x++
//     }
//     let z = 0;
//     while(z<board.length){
//         let i = []
//         for(let j = 0;j<board.length; j++){
//             i.
//         }
//     }
//     return true