import { API_URL } from '@/api/config'
import { FullService } from '@/api/services/base'
import { Author } from '@/api/schemas'

export default class AuthorsService extends FullService {
  protected SchemaClass = Author;
  protected baseUrl: string = API_URL + 'authors/';
}
