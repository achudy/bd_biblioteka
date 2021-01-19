module.exports = {
    publicPath: '/static/',
    configureWebpack: {
        devServer: {
        }
      },


      chainWebpack: config => {
        config.performance
          .maxEntrypointSize(12800000)
          .maxAssetSize(12800000)
      }
}