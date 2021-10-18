const {parse} = require("@babel/parser")
const generator = require("@babel/generator").default()
const traverse = require("@babel/traverse");

const fs = require("fs");

var js_code = fs.readFileSync('AST_1.js', {encoding: 'utf-8'});

const ast_code = parse(js_code);