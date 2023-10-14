import { applyMixins, DescriptionMixin, PopularityMixin, ScoreMixin, SlugMixin } from './mixins'

class _Book {}

interface _Book extends ScoreMixin, SlugMixin, PopularityMixin, DescriptionMixin {}

applyMixins(_Book, [ScoreMixin, SlugMixin, PopularityMixin, DescriptionMixin])
export class Book extends _Book {
  constructor (json: {
    slug:string,
    author: string,
    genres: string[],
    title: string,
    description: string,
    file: string,
    // eslint-disable-next-line camelcase
    year_of_writing: number,
    cover: string,
    score: number | null,
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
  protected _genres: string[];
  protected _title: string;
  protected _file: string;
  protected _yearOfWriting: number;

  protected _cover: string;
  get author () { return this._author }
  get genres () { return this._genres }
  get title () { return this._title }
  get file () { return this._file }
  get yearOfWriting () { return this._yearOfWriting }
  get cover () { return this._cover }
}
