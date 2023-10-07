import { DescriptionMixin, IdMixin, NameMixin, PopularityMixin, ScoreMixin, SlugMixin } from '@/api/schemas/mixins'

export class User {
  get username () { return this._username }
  get email () { return this._email }
  get photo () { return this._photo }
  get isStaff () { return this._isStaff }

  constructor (json) {
    this._email = json.email
    this._username = json.username
    this._photo = json.photo
    this._isStaff = json.is_staff
  }
}

export class Comment {
  get book () { return this._book }
  get user () { return this._user }
  get text () { return this._text }
  get creationTime () { return this._creationTime }
  constructor (json) {
    this.id = json.id
    this._book = json.book
    this._user = json.user
    this.score = json.score
    this._text = json.text
    this._creationTime = json.creation_time
  }
}
Object.assign(Comment.prototype, ScoreMixin, IdMixin)

export class Book {
  get author () { return this._author }
  get genres () { return this._genres }
  get title () { return this._title }
  get file () { return this._file }
  get yearOfWriting () { return this._yearOfWriting }
  get cover () { return this._cover }
  constructor (json) {
    this._author = json.author
    this._genres = json.genres
    this._title = json.title
    this._file = json.file
    this._yearOfWriting = json.year_of_writing
    this._cover = json.cover

    this.slug = json.slug
    this.score = json.score
    this.popularity = json.popularity
    this.description = json.description
  }
}
Object.assign(Book.prototype, ScoreMixin, SlugMixin, PopularityMixin, DescriptionMixin)

export class Author {
  get image () { return this._image }
  get surname () { return this._surname }
  get fullName () { return this.name + ' ' + this._surname }
  constructor (json) {
    this.slug = json.slug
    this.name = json.name
    this._surname = json.surname
    this.score = json.score
    this.popularity = json.popularity
    this._image = json.image
    this.description = json.description
  }
}
Object.assign(Author.prototype, ScoreMixin, SlugMixin, PopularityMixin, DescriptionMixin, NameMixin)
