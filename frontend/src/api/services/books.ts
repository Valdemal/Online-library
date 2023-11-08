import { API_URL } from '@/api/config'
import { FullService } from '@/api/services/base'
import { Book } from '@/api/schemas'

export default class BooksService extends FullService {
  protected SchemaClass = Book;
  protected baseUrl: string = API_URL + 'books/';
}
