export class Matrix {
  constructor(string) {
    this.matrix = string
      .split("\n")
      .map(row => row.split(" ").map(n => parseInt(n)));
  }

  get rows() {
    return this.matrix;
  }

  get columns() {
    if(!this._columns)
      this._columns = this.matrix[0].map((_, i) => this.matrix.map(row => row[i]));

    return this._columns;
  }
}
