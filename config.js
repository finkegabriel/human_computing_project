const baseConfig = {
  hsyncServer: 'ws://localhost:3101',
  hsyncSecret: process.env.HSYNC_SECRET, // keep it secret, keep it safe!
  localHost: process.env.LOCAL_HOST || 'localhost', // host of local server
  port: process.env.PORT || 3000, // port of local server
  hsyncBase: process.env.HSYNC_BASE || '_hs',
  keepalive: parseInt(process.env.HSYNC_KEEP_ALIVE) || 60,
};


const connections = [baseConfig];
const keys = Object.keys(process.env);
keys.forEach((k) => {
  if(k.startsWith('HUMAN_SERVER_')) {
    const name = k.substring(12);
    const value = process.env[k];
    if (name && value) {
      connections.push({
        name,
        hsyncServer: value,
        hsyncSecret: process.env['HSYNC_SECRET_' + name] || baseConfig.hsyncSecret,
        localHost: process.env['LOCAL_HOST_' + name] || baseConfig.localHost,
        port: process.env['PORT' + name] || baseConfig.port,
        hsyncBase: process.env['HSYNC_BASE_' + name] || baseConfig.hsyncBase,
        keepalive: parseInt(process.env['HSYNC_KEEP_ALIVE_' + name]) || baseConfig.keepalive,
      })
    }
  }
})
console.log("connetions ",connections);
const config = Object.assign({}, baseConfig, {connections});

module.exports = config;