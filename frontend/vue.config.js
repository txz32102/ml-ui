const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,
  chainWebpack: config => {
    // Add a rule for .md files
    config.module
      .rule('markdown')
      .test(/\.md$/)
      .use('raw-loader')
        .loader('raw-loader')
        .end();
  },
  configureWebpack: {
    module: {
      rules: [
        {
          test: /\.html$/,
          loader: 'html-loader'
        }
      ]
    }
  }
});
