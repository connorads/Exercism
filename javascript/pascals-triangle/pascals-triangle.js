export const rows = (numberOfRows) => {
  if (numberOfRows === 0) {
    return [];
  }

  const rows = [[1]];

  for (
    let currentRowNumber = 1;
    currentRowNumber < numberOfRows;
    currentRowNumber++
  ) {
    const previousRow = rows[currentRowNumber - 1];
    const currentRow = getCurrentRow(previousRow);
    rows.push(currentRow);
  }

  return rows;
};

const getCurrentRow = (previousRow) => [
  ...previousRow.map((number, index) => {
    if (index === 0) {
      return 1;
    }
    return number + previousRow[index - 1];
  }),
  1,
];
