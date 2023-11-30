import { SchemaService, Service } from '@/api/services/base'
import { User } from '@/api/schemas'
import { API_URL } from '@/api/config'

export default class MeService extends SchemaService {
  protected SchemaClass = User;
  protected baseUrl: string = API_URL + 'users/me/';

  public async get () {
    const response = await Service.API.get(this.baseUrl)
    return new User(response.data)
  }

  public isAuthenticated (): boolean {
    return localStorage.authToken
  }
}
