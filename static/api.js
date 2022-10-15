
function getData(url) {
    let data = []
    axios.get('http://127.0.0.1:8000/' + url).then(function (response) {
        data = response.data;
    })
    return data;
}

Api = {
    getAuthors: function () {
        return getData('api/authors/');
    },

    getBooks: function () {
        return getData('api/books/');
    },

    getBookById: function (id) {
      return getData(`api/books/${id}/`);
    },

    getAuthorById: function (id) {
        return getData(`api/authors/${id}/`);
    },

    getAuthorBooks: function (author_id) {
      return getData(`api/authors/${author_id}/books/`)
    }
}
