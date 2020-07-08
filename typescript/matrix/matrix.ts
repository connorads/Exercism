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
    if (!this._columns)
      this._columns = this._rows[0].map((_, i) =>
        this._rows.map((row) => row[i])
      );

    return this._columns;
  }
}

export default Matrix;
