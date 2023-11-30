import { Email, FileUrl, Schema, Username } from '@/api/schemas/types'

export class User implements Schema {
  protected _username: Username;
  protected _email: Email;
  protected _photo: FileUrl;
  protected _isStaff: boolean;

  private static USER_PHOTO_PLACEHOLDER_SRC = new URL('@/assets/user_photo_placeholder.png', import.meta.url).href

  get username () {
    return this._username
  }

  get email () {
    return this._email
  }

  get photo () {
    if (this._photo) {
      return this._photo
    } else {
      return User.USER_PHOTO_PLACEHOLDER_SRC
    }
  }

  get isStaff () {
    return this._isStaff
  }

  constructor (json: {
    // eslint-disable-next-line camelcase
    email: Email, username: Username, photo: FileUrl, is_staff: boolean
  }) {
    this._email = json.email
    this._username = json.username
    this._photo = json.photo
    this._isStaff = json.is_staff
  }
}
