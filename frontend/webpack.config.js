const path = require("path");

// Конфиг клиента.
clientConfig = {
  mode: "development",
  entry: {
    client: ["./src/client.js", "@babel/polyfill"]
  },
  output: {
    path: path.resolve(__dirname, "../dist"),
    filename: "[name].js"
  },
  module: {
    rules: [
        { test: /\.js$/, exclude: /node_modules/, loader: "babel-loader" }
    ]
 }
};

// Конфиг сервера. Обратите внимание на две вещи:
// 1. target: "node" - без этого упадёт уже на import path.
// 2. складываем в .., а не в ../dist -- нечего пользователям
//    видеть код нашего сервера, пусть и скомпилированный!
serverConfig = {
  mode: "development",
  target: "node",
  entry: {
    server: ["./index.js", "@babel/polyfill"]
  },
  output: {
    path: path.resolve(__dirname, ".."),
    filename: "[name].js"
  },
  module: {
    rules: [
        { test: /\.js$/, exclude: /node_modules/, loader: "babel-loader" }
    ]
 }
};

module.exports = [clientConfig, serverConfig];
