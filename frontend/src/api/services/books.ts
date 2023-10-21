import { API_URL } from '@/api/config'
import { Service } from '@/api/services/base'

export default class BooksService extends Service {
  protected static BASE_URL = API_URL + 'books/';
}
