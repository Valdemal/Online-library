import { Score, Slug } from '@/api/schemas/types'

export function applyMixins (derivedCtor: any, constructors: any[]) {
  constructors.forEach((baseCtor) => {
    Object.getOwnPropertyNames(baseCtor.prototype).forEach((name) => {
      Object.defineProperty(
        derivedCtor.prototype,
        name,
        Object.getOwnPropertyDescriptor(baseCtor.prototype, name) ||
        Object.create(null)
      )
    })
  })
}

export class ScoreMixin {
  protected _score: Score = 0;

  get score (): Score {
    return this._score
  }

  set score (value: Score) {
    this._score = value
  }

  roundedScore (): string | null {
    if (this._score === null) {
      return null
    }

    return Number(this.score).toFixed(2)
  }
}

export class SlugMixin {
  protected _slug: Slug = '';

  get slug (): string {
    return this._slug
  }

  set slug (value: string) {
    this._slug = value
  }
}

export class DescriptionMixin {
  protected _description: string = '';

  get description (): string {
    return this._description
  }

  set description (value: string) {
    this._description = value
  }
}

export class PopularityMixin {
  protected _popularity: number = 0;
  get popularity () {
    return this._popularity
  }

  set popularity (value) {
    this._popularity = value
  }
}

export class IdMixin {
  protected _id: number = 0;
  get id (): number {
    return this._id
  }

  set id (value: number) {
    this._id = value
  }
}

export class NameMixin {
  protected _name: string = '';
  get name (): string {
    return this._name
  }

  set name (value: string) {
    this._name = value
  }
}
