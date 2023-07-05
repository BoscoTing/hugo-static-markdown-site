function max(numbers) {
    let maxNumber = numbers[0];
    for (let i = 0; i < numbers.length ; i ++) {
        if (numbers[i] > maxNumber) {
            maxNumber = numbers[i];
        }
    }
    return maxNumber
}
function findPosition(numbers, target) {
    let result = -1
    for (let position = 0; position < numbers.length; position ++) {
        if (numbers[position] == target) {
            return position;
        } 
    }
    return result
}