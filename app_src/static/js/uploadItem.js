

const Upload = {
    delimiters: ['[[', ']]'],
    data() {
        return {
            counter:0,
            categories:[]
        }
    },
    methods: {
        async getCats(){
            const requestOptions = {
                method: "POST",
                credentials: "include",
                body: JSON.stringify(''),
                cache: "no-cache",
                headers: new Headers({
                    "content-type": "application/json"
                })
            }
            const response = await fetch(`${window.origin}/api/category_list`, requestOptions);
            const data = await response.json();
            this.categories=data.list_cat;


        }
    }
}

Vue.createApp(Upload).mount('#upload')

