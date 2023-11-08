export const API_URL = process.env.VUE_APP_BACKEND_PROTOCOL + '://' + process.env.VUE_APP_BACKEND_HOST + (process.env.VUE_APP_BACKEND_PORT ? ':' + process.env.VUE_APP_BACKEND_PORT : '') + '/api/'
