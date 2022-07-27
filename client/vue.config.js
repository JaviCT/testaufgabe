const { defineConfig } = require('@vue/cli-service')

if (process.env.NODE_ENV === 'development') {
  module.exports = defineConfig({
    transpileDependencies: true,
  })
} else {
  module.exports = defineConfig({
    transpileDependencies: true,
    productionSourceMap: false,  
    outputDir: '../dist',
    assetsDir: 'static',
    indexPath: 'templates/index.html'
  })
}