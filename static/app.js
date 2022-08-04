new Vue({
    el: "#app",

    data: {
        books: [],
        message: 'Привет, Vue!'
    },

    created: function () {
        let vm = this;
        axios.get('/api/books/').then(function (response) {
            vm.books = response.data;
        })
    }

});
