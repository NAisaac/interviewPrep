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

// contains() - search for value in the tree
Tree.prototype.contains = function (callback, traversal) {
  traversal.call(this, callback);
};


// add() - add a node to a specific node
Tree.prototype.add = function (data, toData, traversal) {
  var errorMessage = 'Failure: no such node to add to';
  var child = new Node(data);
  var parent = null;
  var callback = function (node) {
    if (node.data === toData) {
      parent = node;
    }
  };

  this.contains(callback, traversal);

  if (parent) {
    parent.children.push(child);
    child.parent = parent;
  } else {
    console.error(errorMessage);
    throw new Error(errorMessage);
  }
};

// remove() - remove a node from a speicific node
Tree.prototype.remove = function (data, fromData, traversal) {
  var parent = null,
      childToRemove = null,
      index;
  var callback = function (node) {
    if (node.data === fromData) {
      parent = node;
    }
  };

  function findIndex(arr, data) {
    var index;
    for (var i = 0; i < arr.length; i++) {
      if (arr[i].data === data) {
        index = i;
      }
    }
    return index;
  }

  this.contains(callback, traversal);

  if (parent) {
    index = findIndex(parent.children, data);

    if (!index) {
      console.error('Node to remove DNE');
      throw new Error('Node to remove DNE');
    } else {
      childToRemove = parent.children.splice(index, 1);
    }
  } else {
    console.error('Node to remove from DNE');
    throw new Error('Node to remove from DNE');
  }

  return childToRemove;
};
