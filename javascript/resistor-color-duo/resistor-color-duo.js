export const decodedValue = (array) => {
    let first = COLORS.indexOf(array[0]).toString();
    let second = COLORS.indexOf(array[1]).toString();
    return parseInt(first + second);
};

const COLORS = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"];