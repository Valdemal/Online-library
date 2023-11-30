import { Service } from '@/api/services/base'
import { API_URL } from '@/api/config'
import { AuthToken, LoginCredentials } from '@/api/schemas/types'

export default class AuthService extends Service {
  protected baseUrl = API_URL + 'auth/token/';

  async login (credentials: LoginCredentials): Promise<AuthToken> {
    const response = await Service.API.post(this.baseUrl + 'login/', credentials)
    return response.data.auth_token
  }

  async logout () {
    await Service.API.post(this.baseUrl + 'logout/')
  }
}
