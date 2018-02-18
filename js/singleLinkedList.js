'use strict';

function Node (d) {
  this.data = d;
  this.next = null;
}

function SingleList () {
  // default is an empty list
  this.length = 0;
  this.head = null;
}

// add()
SingleList.prototype.add = function (d) {
  var node = new Node(d),
      currentNode = this.head;

  // empty list
  if (!currentNode) {
    this.head = node;
    this.length++;
    return node;
  }

  // non-empty list
  // go down the link until the last node, which doesn't have a next node
  while (currentNode.next) {
    currentNode = currentNode.next;
  }
  currentNode.next = node;
  this.length++;
  return node;
};

// searchNodeAt()
SingleList.prototype.searchNodeAt = function (position) {
  var currentNode = this.head,
      count = 1,
      errorMessage = 'Failure: no node at that position!';

  // invalid position
  if (this.length === 0 || position < 1 || position > this.length) {
    console.error(errorMessage);
    throw new Error(errorMessage);
  }

  // valid position
  // go down the link until the node at requested position
  while (count < position) {
    currentNode = currentNode.next;
    count++;
  }

  return currentNode;
};

// removeNodeAt()
SingleList.prototype.removeNodeAt = function (position) {
  var currentNode = this.head,
      count = 1,
      errorMessage = 'Failure: no node at that position!',
      beforeNode = null,
      removedNode = null;

      // invalid position
      if (this.length === 0 || position < 0 || position > this.length) {
        console.error(errorMessage);
        throw new Error(errorMessage);
      }

      // remove head node
      if (position === 1){
        removedNode = currentNode;
        this.head = currentNode.next;
        this.length--;
        return removedNode;
      }

      // remove non-head node
      // go down the link until the node at requested position
      // keep track of previous node so that .next can skip over removed node
      while (count < position) {
        beforeNode = currentNode;
        currentNode = currentNode.next;
        count++;
      }
      removedNode = currentNode;
      beforeNode.next = currentNode.next;
      this.length--;
      return removedNode;
};
