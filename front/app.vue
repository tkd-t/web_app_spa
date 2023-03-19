
<template>
  <div>
    <h1>testest</h1>
    <!-- 全ページで共有されるマークアップ（例: NavBar） -->
    <NuxtPage />
  </div>
</template>

<!-- <template>
  <div>
    <p>{{ host }}</p>
    <button @click="sendRequest">リクエスト</button>
    <p>{{ accept }}</p>
  </div>
</template>

<script>
export default {
  components: {
  },
  data() {
    return {
        host: '',
        accept: ''
    };
  },
  methods: {
    async sendRequest() {
      const response = await this.$axios.$get('https://httpbin.org/get');
      this.accept = response.headers.Accept;
    }
  },
  async asyncData({ app }) {
    const response = await app.$axios.$get('https://httpbin.org/get');
    return { host: response.headers.Host };
  }
}
</script> -->