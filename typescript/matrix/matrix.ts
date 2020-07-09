const transpose = (matrix: number[][]): number[][] => {
  return matrix[0].map((_, i) => matrix.map((row) => row[i]));
};

class Matrix {
  private readonly _rows: number[][];
  private _columns?: number[][];

  constructor(matrix: string) {
    this._rows = matrix
      .split("\n")
      .map((row) => row.split(" ").map((n) => parseInt(n)));
  }

  get rows(): number[][] {
    return this._rows;
  }

  get columns(): number[][] {
    if (!this._columns) {
      this._columns = transpose(this._rows);
    }

    return this._columns;
  }
}

export default Matrix;
