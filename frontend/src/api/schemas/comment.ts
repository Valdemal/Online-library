import { applyMixins, IdMixin, ScoreMixin } from './mixins'

class _Comment {}

interface _Comment extends ScoreMixin, IdMixin {}

applyMixins(_Comment, [ScoreMixin, IdMixin])

export class Comment extends _Comment {
  constructor (json: {
    id: number,
    book: string,
    user: string,
    score: number,
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

  protected _book: string;
  protected _user: string;
  protected _text: string;
  protected _creationTime: string;
  get book () { return this._book }
  get user () { return this._user }
  get text () { return this._text }
  get creationTime () { return this._creationTime }
}
