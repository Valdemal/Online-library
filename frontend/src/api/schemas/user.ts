export class User {
  protected _username: string;
  protected _email: string;
  protected _photo: string;
  protected _isStaff: boolean;

  get username () {
    return this._username
  }

  get email () {
    return this._email
  }

  get photo () {
    return this._photo
  }

  get isStaff () {
    return this._isStaff
  }

  constructor (json: {
    // eslint-disable-next-line camelcase
    email: string, username: string, photo: string, is_staff: boolean
  }) {
    this._email = json.email
    this._username = json.username
    this._photo = json.photo
    this._isStaff = json.is_staff
  }
}
