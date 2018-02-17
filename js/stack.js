'use strict';
// Stack: if you need data to be organized in sequential order (i.e. linear data structure), but LIFO
// https://code.tutsplus.com/articles/data-structures-with-javascript-stack-and-queue--cms-23348

// LIFO
function Stack () {
  this.size = 0;
  this.storage = {};
}

// push()
// increment the size of the stack, add new data to storage object in order (i.e. key:value is size:data)
Stack.prototype.push = function (d) {
  // ++i increments the variable, AND returns the new value
  // i++ increments the variable, BUT returns the old value
  this.storage[++this.size] = d;
};

// pop()
// if there is data in the stack, get the most recently added data, update the stack
Stack.prototype.pop = function () {
  let popData;
  if(this.size) {
    popData = this.storage[this.size];
    delete this.storage[this.size];
    this.size--;
    return popData;
  }
};
