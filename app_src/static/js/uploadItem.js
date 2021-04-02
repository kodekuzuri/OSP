

const Upload = {
    delimiters: ['[[', ']]'],
    data() {
        return {
            counter: 0,
            categories: []
        }
    },
    created(){
        const requestOptions = {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(''),
            cache: "no-cache",
            headers: new Headers({
                "content-type": "application/json"
            })
        }
        // const response = await fetch(`${window.origin}/api/category_list`, requestOptions);
        // const data = await response.json();
        // this.categories=data.list_cat;
        fetch(`${window.origin}/api/category_list`, requestOptions)
            .then(function (response) {
                response.json()
                    .then(function (data) {
                        this.categories = data.list_cat;
                    })
            })
            .catch(function (error) { console.log(error) });
        console.log("hi");
    },
    methods: {

    }
}

Vue.createApp(Upload).mount('#upload')

