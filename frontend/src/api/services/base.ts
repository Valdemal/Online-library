import { Slug } from '@/api/schemas/types'
import axios from 'axios'
import { applyMixins } from '@/api/schemas/mixins'

function getCookie (name: string) {
  const matches = document.cookie.match(new RegExp(
    '(?:^|; )' + name.replace(/([.$?*|{}()[\]\\/+^])/g, '\\$1') + '=([^;]*)'
  ))
  return matches ? decodeURIComponent(matches[1]) : undefined
}

function putAuthTokenIntoHeaders (config: any) {
  if (localStorage.authToken) {
    config.headers.Authorization = `Token ${localStorage.authToken}`
  }

  return config
}

function putCSRFTokenIntoHeaders (config: any) {
  const csrfToken = getCookie('csrftoken')
  if (csrfToken) {
    config.headers['X-CSRFToken'] = csrfToken
  }

  return config
}

export abstract class Service {
  protected abstract baseUrl: string;

  protected static API = (() => {
    const instance = axios.create()

    instance.interceptors.request.use(putAuthTokenIntoHeaders)
    instance.interceptors.request.use(putCSRFTokenIntoHeaders)
    instance.interceptors.response.use(putAuthTokenIntoHeaders)
    instance.interceptors.response.use(putCSRFTokenIntoHeaders)

    return instance
  })()
}

export abstract class SchemaService extends Service {
  // @ts-ignore
  protected abstract SchemaClass: Constructor;
}

export abstract class ListServiceMixin extends SchemaService {
  public async list (params: Object = {}) {
    const response = await Service.API.get(this.baseUrl, {
      params: params
    })

    return response.data.results.map((json: any) => {
      return new this.SchemaClass(json)
    })
  }
}

export abstract class DetailServiceMixin extends SchemaService {
  public async detail (slug: Slug) {
    const response = await Service.API.get(`${this.baseUrl}${slug}/`)
    return new this.SchemaClass(response.data)
  }
}

abstract class _FullService {
}

interface _FullService extends SchemaService, ListServiceMixin, DetailServiceMixin {
}

applyMixins(_FullService, [SchemaService, ListServiceMixin, DetailServiceMixin])

export abstract class FullService extends _FullService {
}
