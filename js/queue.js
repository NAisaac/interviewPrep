'use strict';
// Queue: if you need data to be organized in sequential order (i.e. linear data structure), but FIFO
// https://code.tutsplus.com/articles/data-structures-with-javascript-stack-and-queue--cms-23348

// FIFO
function Queue () {
  this.oldestIndex = 1;
  this.newestIndex = 1;
  this.storage = {};
}

// add new data to the bottom
Queue.prototype.enqueue = function (d) {
  // ++i increments the variable, AND returns the new value
  // i++ increments the variable, BUT returns the old value
  this.storage[++this.newestIndex] = d;
};

// get/remove from the bottom
Queue.prototype.dequeue = function () {
  let dequeueData = this.storage[this.oldestIndex];
  if(this.oldestIndex !== this.newIndex) {
    delete this.storage[this.oldestIndex];
    this.oldestIndex++;
    return dequeueData;
  }
};

// get queue size
Queue.prototype.size = function () {
  return this.newestIndex - this.oldestIndex;
};
