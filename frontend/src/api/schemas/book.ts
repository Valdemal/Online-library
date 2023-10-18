import { applyMixins, DescriptionMixin, PopularityMixin, ScoreMixin, SlugMixin } from './mixins'
import { Slug, FileUrl, Score } from '@/api/schemas/types'

class _Book {}

interface _Book extends ScoreMixin, SlugMixin, PopularityMixin, DescriptionMixin {}

applyMixins(_Book, [ScoreMixin, SlugMixin, PopularityMixin, DescriptionMixin])

export class Book extends _Book {
  constructor (json: {
    slug:Slug,
    author: Slug,
    genres: Slug[],
    title: string,
    description: string,
    file: FileUrl,
    // eslint-disable-next-line camelcase
    year_of_writing: number,
    cover: FileUrl,
    score: Score,
    popularity: number,
  }) {
    super()
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

  protected _author: string;
  protected _genres: Slug[];
  protected _title: string;
  protected _file: FileUrl;
  protected _yearOfWriting: number;

  protected _cover: FileUrl;
  get author () { return this._author }
  get genres () { return this._genres }
  get title () { return this._title }
  get file () { return this._file }
  get yearOfWriting () { return this._yearOfWriting }
  get cover () { return this._cover }
}
