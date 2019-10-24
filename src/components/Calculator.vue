<template>
  <div>
    <b-field>
      <b-input v-model="url"></b-input>
    </b-field>
    <div class="has-text-centered">
      <b-button type="is-light" @click="calculate">Calculate</b-button>
      <div v-if="link">
        <span class="icon">
          <img src="https://www.google.com/s2/favicons?domain=shodan.io" alt="shodan" />
        </span>
        <a :href="link" target="_blank">{{ type }}:{{ hash }}</a>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import axios, { AxiosError } from "axios";
import * as qs from "qs";

@Component
export default class Calculator extends Vue {
  hash: number | undefined;
  link: string | undefined;
  type: string | undefined;
  url: string | undefined;

  data() {
    return {
      hash: undefined,
      link: undefined,
      type: undefined,
      url: "https://www.google.com/favicon.ico"
    };
  }

  buildLink(type: string, hash: number) {
    const baseUrl = "https://shodan.io/search?";
    const params = {
      query: `${type}:${hash}`
    };
    return baseUrl + qs.stringify(params);
  }

  async calculate() {
    try {
      const response = await axios.get("/hash", { params: { url: this.url } });
      const data = response.data;
      if ("hash" in data && "type" in data) {
        this.hash = data.hash;
        this.type = data.type;
        this.link = this.buildLink(data.type, data.hash);
      }
    } catch (error) {
      const data = error.response.data;
      console.error(data);
      if ("error" in data) {
        alert(data.error);
      } else {
        alert(error);
      }
    }
  }
}
</script>
