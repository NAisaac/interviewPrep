'use strict';
// unlike Singly-Linked List, which is uni-directional (i.e. head to tail)
// Doubly-Linked List is bi-directional (i.e. head to tail, tail to head)

function Node (d) {
  this.data = d;
  this.previous = null;
  this.next = null;
}

function DoubleList () {
  // default is an empty list
  this.length = 0;
  this.head = null;
  this.tail = null;
}

// add()
DoubleList.prototype.add = function (d) {
  var node = new Node(d);

  // empty list
  if (!this.length) {
    this.head = node;
    this.tail = node;
  }

  // non-empty list
  this.tail.next = node;
  node.previous = this.tail;
  this.tail = node;

  this.length++;
  return node;
};

// go down from head
DoubleList.prototype.traverseDown = function (position) {
  var count = 1,
      previousNode = null,
      currentNode = this.head,
      nextNode = this.head.next;

  while (count < position) {
    previousNode = currentNode;
    currentNode = currentNode.next;
    nextNode = currentNode.next;
    count++;
  }

  return {
    previous: previousNode,
    current: currentNode,
    next: nextNode
  };
};

// go up from tail
DoubleList.prototype.traverseUp = function (position) {
  var count = this.length,
      previousNode = this.tail.previous,
      currentNode = this.tail,
      nextNode = null;

  while (count > position) {
    nextNode = currentNode;
    currentNode = currentNode.previous;
    previousNode = currentNode.previous;
    count--;
  }

  return {
    previous: previousNode,
    current: currentNode,
    next: nextNode
  };
};

// searchNodeAt()
DoubleList.prototype.searchNodeAt = function (position) {
  var errorMessage = 'Failure: no node at that position!',
      traverse,
      nodes;

  // invalid position
  if (position < 1 || this.length < 1 || this.length < position) {
    console.error(errorMessage);
    throw new Error(errorMessage);
  }

  // valid position
  // depending on position from mid length, go down or go up
  traverse = position <= this.length / 2 ? this.traverseDown : this.traverseUp;
  nodes = traverse(position);

  return nodes.current;
};

// removeNodeAt()
DoubleList.prototype.removeNodeAt = function (position) {
  var errorMessage = 'Failure: no node at that position!',
      traverse,
      nodes;

  // invalid position
  if (position < 1 || this.length < 1 || this.length < position) {
    console.error(errorMessage);
    throw new Error(errorMessage);
  }

  traverse = position <= this.length / 2 ? this.traverseDown : this.traverseUp;
  nodes = traverse(position);

  // if there is only 1 node then reset to default
  if (this.length === 1) {
    this.head = null;
    this.tail = null;
  } else if (position === 1) {
    // remove head
    nodes.next.previous = null;
    this.head = nodes.next;
  } else if (position === this.length) {
    // remove tail
    nodes.previous.next = null;
    this.tail = nodes.previous;
  } else {
    // remove middle
    nodes.previous.next = nodes.next;
    nodes.next.previous = nodes.previous;
  }

  length--;
  return nodes.current;
};
