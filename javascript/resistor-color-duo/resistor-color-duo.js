export const decodedValue = ([color1, color2]) => {
    let first = COLORS.indexOf(color1).toString();
    let second = COLORS.indexOf(color2).toString();
    return parseInt(first + second);
};

const COLORS = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"];