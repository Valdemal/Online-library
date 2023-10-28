import { API_URL } from '@/api/config'
import { Schema, Slug } from '@/api/schemas/types'
import axios from 'axios'
import { applyMixins } from '@/api/schemas/mixins'

abstract class Service {
  protected abstract baseUrl: string;
  // @ts-ignore
  protected abstract SchemaClass: Constructor;
}

export abstract class ListServiceMixin extends Service {
  public async list (params: Object = {}) {
    const response = await axios.get(this.baseUrl, {
      params: params
    })

    return response.data.results.map((json: any) => {
      return new this.SchemaClass(json)
    })
  }
}

export abstract class DetailServiceMixin extends Service {
  public async detail (slug: Slug) {
    const response = await axios.get(`${this.baseUrl}${slug}/`)
    return new this.SchemaClass(response.data)
  }
}

abstract class _FullService {}
interface _FullService extends Service, ListServiceMixin, DetailServiceMixin {}

applyMixins(_FullService, [Service, ListServiceMixin, DetailServiceMixin])

export abstract class FullService extends _FullService {}
