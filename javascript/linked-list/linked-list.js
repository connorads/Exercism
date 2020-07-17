export class LinkedList {
  constructor() {
    this.head = undefined;
    this.tail = undefined;
    this._count = 0;
  }

  push(value) {
    const node = { value };
    if (!this.head) {
      this.head = node;
    }
    if (this.tail) {
      this.tail.next = node;
      node.prev = this.tail;
    }
    this.tail = node;
    this._count++;
  }

  pop() {
    if (this.tail) {
      const value = this.tail.value;
      this.tail = this.tail.prev;
      this._count--;
      return value;
    }
  }

  shift() {
    if (this.head) {
      const value = this.head.value;
      this.head = this.head.next;
      this._count--;
      return value;
    }
  }

  unshift(value) {
    const node = { value };
    if (!this.tail) {
      this.tail = node;
    }
    if (this.head) {
      this.head.prev = node;
      node.next = this.head;
    }
    this.head = node;
    this._count++;
  }

  delete(value) {
    let currentNode = this.head;
    let valueFound = false;
    do {
      if (currentNode.value === value) {
        valueFound = true;
        if (currentNode === this.head) {
          this.head = this.head.next;
        } else if (currentNode === this.tail) {
          this.tail = this.tail.prev;
        } else {
          currentNode.prev.next = currentNode.next;
          currentNode.next.prev = currentNode.prev;
        }
        this._count--;
      }
      currentNode = currentNode.next;
    } while (!valueFound && currentNode);
  }

  count() {
    return this._count;
  }
}
