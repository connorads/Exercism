export class List {
  constructor(values) {
    this.values = values || [];
  }

  append(list) {
    return new List([...this.values, ...list.values]);
  }

  concat(list) {
    let newList = new List(this.values);
    for (let i = 0; i < list.values.length; i++) {
      newList = newList.append(list.values[i]);
    }
    return newList;
  }

  filter(predicate) {
    let newList = [];
    for (let i = 0; i < this.values.length; i++) {
      const value = this.values[i];
      if (predicate(value)) newList = [...newList, value];
    }
    return new List(newList);
  }

  map(func) {
    let newList = [];
    for (let i = 0; i < this.values.length; i++) {
      newList = [...newList, func(this.values[i])];
    }
    return new List(newList);
  }

  length() {
    return this.values.length;
  }

  foldl(func, initialValue) {
    let acc = initialValue;
    for (let i = 0; i < this.values.length; i++) {
      acc = func(acc, this.values[i]);
    }
    return acc;
  }

  foldr(func, initialValue) {
    let acc = initialValue;
    for (let i = this.values.length - 1; i >= 0; --i) {
      acc = func(acc, this.values[i]);
    }
    return acc;
  }

  reverse() {
    let newList = [];
    for (let i = this.values.length - 1; i >= 0; --i) {
      newList = [...newList, this.values[i]];
    }
    return new List(newList);
  }
}
