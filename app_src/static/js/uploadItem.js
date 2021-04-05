

const Upload = {
    delimiters: ['[[', ']]'],
    data() {
        return {
            display_form: false,
            categories: [],
            errors: [],

            Name: null,
            Category: null,
            Price: null,
            Company: null,
            City: null,
            Info: null,
            Age: null,
            Weight: null,
            Image: null,
            display_success: false
            // add image support
        }
    },
    methods: {
        async getCats() {
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
            this.categories = data.list_cat;
            this.display_form = true
        },
        checkForm: async function (e) {
            // console.log(this.Image);
            console.log("entered")
            this.errors = [];
            if (this.Name && this.Age && this.Price&& this.Category && this.Company && this.Weight && this.City && this.Info && this.Image) {
                entry = {
                    name: this.Name,
                    age: this.Age,
                    price: this.Price,
                    company: this.Company,
                    weight: this.Weight,
                    city: this.City,
                    info: this.Info,
                    photo: this.Image,
                    category: this.Category
                };
                const requestOptions = {
                    method: "POST",
                    credentials: "include",
                    body: JSON.stringify(entry),
                    cache: "no-cache",
                    headers: new Headers({
                        "content-type": "application/json"
                    })
                };
                // console.log(`${window.origin}/api/upload_item`);
                const response = await fetch(`${window.origin}/api/upload_item`, requestOptions);
                const data = await response.json();
                console.log(data)
                this.display_success = true
                console.log("hi");
                if(data.message==="ok")
                {
                    window.location.href=`${window.origin}/post_upload/success`
                }
                else{
                    window.location.href=`${window.origin}/post_upload/${start_msg} ${data.exception}`
                }
            }
            console.log('81');
            if (!this.Name) {
                this.errors.push('Name is required.');
            }
            if (!this.Age) {
                this.errors.push('Age is required.');
            }
            if (!this.Price) {
                this.errors.push('Price is required.');
            }
            if (!this.Company) {
                this.errors.push('Company is required.');
            }
            if (!this.City) {
                this.errors.push('City is required.');
            }
            if (!this.Weight) {
                this.errors.push('Weight is required.');
            }
            if (!this.Info) {
                this.errors.push('Info is required.');
            }
            if (!this.Image) {
                this.errors.push('Image is required.');
            }
            e.preventDefault();
        },
        onFileChange(e) {
            var files = e.target.files || e.dataTransfer.files;
            if (!files.length)
                return;
            console.log()
            this.createImage(files[0]);
        },
        createImage(file) {
            var image = new Image();
            var reader = new FileReader();
            var vm = this;
            reader.onload = (e) => {
                vm.Image = e.target.result;
            };
            reader.readAsDataURL(file);
        },
        removeImage: function (e) {
            this.Image = '';
        }
    }
}

Vue.createApp(Upload).mount('#upload')

