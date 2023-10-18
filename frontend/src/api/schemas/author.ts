import { applyMixins, DescriptionMixin, NameMixin, PopularityMixin, ScoreMixin, SlugMixin } from './mixins'
import { Slug, FileUrl, Score } from '@/api/schemas/types'

class _Author {}

interface _Author extends ScoreMixin, SlugMixin, PopularityMixin, DescriptionMixin, NameMixin {}

applyMixins(_Author, [ScoreMixin, SlugMixin, PopularityMixin, DescriptionMixin, NameMixin])

export class Author extends _Author {
  constructor (json: {
    slug: Slug,
    name: string,
    surname: string,
    score: Score,
    popularity: number,
    image: FileUrl,
    description: string
  }) {
    super()
    this.slug = json.slug
    this.name = json.name
    this._surname = json.surname
    this.score = json.score
    this.popularity = json.popularity
    this._image = json.image
    this.description = json.description
  }

  protected _image: FileUrl;
  protected _surname: string;
  get image () { return this._image }
  get surname () { return this._surname }
  public get fullName () { return this.name + ' ' + this._surname }
}
