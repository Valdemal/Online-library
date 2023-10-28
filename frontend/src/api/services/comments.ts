import { FullService } from '@/api/services/base'
import { API_URL } from '@/api/config'
import { Comment } from '@/api/schemas'

export default class CommentsService extends FullService {
  protected SchemaClass = Comment;
  protected baseUrl: string = API_URL + 'comments/';
}
