import { Service } from '@/api/services/base'
import { API_URL } from '@/api/config'

export default class CommentsService extends Service {
  protected static BASE_URL = API_URL + 'comments/';
}
