import { API_URL } from '@/api/config'
import { Slug } from '@/api/schemas/types'
import axios from 'axios'

export class Service {
  protected static BASE_URL = API_URL;

  public static list (params: Object = {}) {
    return axios.get(this.BASE_URL, {
      params: params
    })
  }

  public static detail (slug: Slug) {
    return axios.get(`${this.BASE_URL}${slug}/`)
  }
}
