'use strict';

function Node (d) {
  this.data = d;
  this.parent = null;
  this.children = [];
}

function Tree (d) {
  this.root = new Node(d);
}

function Queue() {
  // queue.js
}


/*
Example Tree:
one
├── two
│   ├── five
│   └── six
├── three
└── four
    └── seven

DFS Order: five, six, two, thre, seven, four, one
BFS Order: one, two, three, four, five, six, seven
*/

// DFS
Tree.prototype.traverseDF = function (callback) {
  // recursively traverse down depth of current node
  (function recurse(currentNode) {
    for (var i = 0; i < currentNode.children.length; i++) {
      recurse(currentNode.children[i]);
    }
    // apply callback on the current node
    callback(currentNode);
  // immediately invoke recurse on the root node
  })(this.root);
};

// BFS
Tree.prototype.traverseBF = function (callback) {
  var bfsQueue = new Queue();
  var currentNode;

  bfsQueue.enqueue(this.root);
  currentNode = bfsQueue.dequeue();

  while (currentNode) {
    for (var i = 0; i < currentNode.children.length; i++) {
      bfsQueue.enqueue(currentNode.children[i]);
    }
    callback(currentNode);
    currentNode = bfsQueue.dequeue();
  }
};
