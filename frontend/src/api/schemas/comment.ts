import { applyMixins, IdMixin, ScoreMixin } from './mixins'
import { Score, Schema, Slug, Username } from '@/api/schemas/types'

class _Comment implements Schema {}

interface _Comment extends ScoreMixin, IdMixin {}

applyMixins(_Comment, [ScoreMixin, IdMixin])

export class Comment extends _Comment {
  constructor (json: {
    id: number,
    book: Slug,
    user: Username,
    score: Score,
    text: string,
    // eslint-disable-next-line camelcase
    creation_time: string
  }) {
    super()
    this._book = json.book
    this._user = json.user

    this._text = json.text
    this._creationTime = json.creation_time

    this.score = json.score
    this.id = json.id
  }

  protected _book: Slug;
  protected _user: Username;
  protected _text: string;
  protected _creationTime: string;
  get book () { return this._book }
  get user () { return this._user }
  get text () { return this._text }
  get creationTime () { return this._creationTime }
}
