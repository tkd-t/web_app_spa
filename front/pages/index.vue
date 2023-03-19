<template>
    <div>
        <p>{{ host }}</p>
        <button @click="sendRequest">リクエスト</button>
        <p>{{ accept }}</p>
        Page visits: {{ count["data"] }}
    </div>
</template>
  
<script>

export default {
    components: {
    },
    data() {
        return {
            host: '',
            accept: '',
            count: ''
        };
    },
    methods: {
        async sendRequest() {
            // console.log({ axios: this.axios });
            // const response = await this.$axios.get('https://httpbin.org/get');
            // this.accept = response.headers.Accept;
            this.count = await useFetch('http://localhost:5001/', {
                method: 'POST',
                body: {text : "text"}
            });
        }
    }
}
</script>