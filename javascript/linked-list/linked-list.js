class Node {
  constructor(value) {
    this.value = value;
    this.prev = undefined;
    this.next = undefined;
  }
}

export class LinkedList {
  constructor() {
    this.head = undefined;
    this.tail = undefined;
  }

  push(value) {
    const node = new Node(value);
    if (!this.head) {
      this.head = node;
    }
    if (this.tail) {
      this.tail.next = node;
      node.prev = this.tail;
    }
    this.tail = node;
  }

  pop() {
    if (this.tail) {
      const value = this.tail.value;
      this.tail = this.tail.prev;
      return value;
    }
  }

  shift() {
    if (this.head) {
      const value = this.head.value;
      this.head = this.head.next;
      return value;
    }
  }

  unshift(value) {
    const node = new Node(value);
    if (!this.tail) {
      this.tail = node;
    }
    if (this.head) {
      this.head.prev = node;
      node.next = this.head;
    }
    this.head = node;
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
      }
      currentNode = currentNode.next;
    } while (!valueFound && currentNode);
  }

  count() {
    if (!this.head || !this.tail) {
      return 0;
    }
    let count = 1;
    let currentNode = this.head;
    while (currentNode !== this.tail) {
      count++;
      currentNode = currentNode.next;
    }
    return count;
  }
}
