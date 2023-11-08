import { Schema, Slug } from '@/api/schemas/types'
import axios from 'axios'
import { applyMixins } from '@/api/schemas/mixins'

function putAuthTokenIntoHeaders (config: any) {
  if (localStorage.authToken) {
    config.headers = {
      Authorization: `Token ${localStorage.authToken}`
    }
  }

  return config
}

export abstract class Service {
  protected abstract baseUrl: string;

  protected static API = (() => {
    const instance = axios.create()

    instance.interceptors.request.use(putAuthTokenIntoHeaders)
    instance.interceptors.response.use(putAuthTokenIntoHeaders)

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
