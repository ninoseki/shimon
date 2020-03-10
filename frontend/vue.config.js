module.exports = {
  outputDir: "dist",
  assetsDir: "static",
  devServer: {
    proxy: {
      "/hash": {
        target: "http://localhost:5000/"
      }
    }
  }
};
