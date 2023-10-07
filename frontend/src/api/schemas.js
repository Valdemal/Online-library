export const Slug = String
export const Comment = {
  id: Number,
  book: Slug,
  user: String,
  score: Number,
  text: String,
  creation_time: String
}

export const Book = {
  author: Slug,
  genres: Array,
  score: Number,
  popularity: Number,
  slug: Slug,
  title: String,
  description: String,
  file: String,
  year_of_writing: String,
  cover: String
}

export const Author = {
  score: Number,
  popularity: Number,
  slug: Slug,
  name: String,
  surname: String,
  image: String,
  description: String
}
