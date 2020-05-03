export const rows = (numberOfRows) => {
  let rows = [];

  for (
    let currentRowNumber = 0;
    currentRowNumber < numberOfRows;
    currentRowNumber++
  ) {
    const previousRow = rows[currentRowNumber - 1];
    const currentRow = getCurrentRow(previousRow);
    rows.push(currentRow);
  }

  return rows;
};

function getCurrentRow(row) {
  return row
    ? [
        ...row.map((number, index) => {
          if (index === 0) {
            return 1;
          }
          return number + row[index - 1];
        }),
        1,
      ]
    : [1];
}
