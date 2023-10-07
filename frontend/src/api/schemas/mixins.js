export const ScoreMixin = {
  get score () { return this._score },

  set score (value) { this._score = value },

  roundedScore () {
    return this.score.toFixed(2)
  }
}

export const SlugMixin = {
  get slug () { return this._slug },
  set slug (value) { this._slug = value }
}

export const DescriptionMixin = {
  get description () { return this._description },
  set description (value) { this._description = value }
}

export const PopularityMixin = {
  get popularity () { return this._popularity },
  set popularity (value) { this._popularity = value }
}

export const IdMixin = {
  get id () { return this._id },
  set id (value) { this._id = value }
}

export const NameMixin = {
  get name () { return this._id },
  set name (value) { this._id = value }
}
