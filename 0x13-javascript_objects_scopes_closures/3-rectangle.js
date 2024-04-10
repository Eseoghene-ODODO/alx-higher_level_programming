#!/usr/bin/node
/*
 * A class Rectangle that defines a rectangle
 */


class Rectangle {
	constructor(w, h) {
		if (w < 1 && h < 1 || !Number.isInteger(w) && !Number.isInteger(h)) {

		}
		this.width = w;
		this.height = h;
	}
	print() {
		return this.width * this.height;
	}
}
module.exports = Rectangle;
