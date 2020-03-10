<template>
  <div>
    <b-field>
      <b-input v-model="url"></b-input>
    </b-field>
    <div class="has-text-centered">
      <b-button type="is-light" @click="calculate">Calculate</b-button>
      <div v-if="link">
        <span class="icon">
          <img
            src="https://www.google.com/s2/favicons?domain=shodan.io"
            alt="shodan"
          />
        </span>
        <a :href="link" target="_blank"
          >{{ response.type }}:{{ response.hash }}</a
        >
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import axios, { AxiosError } from "axios";
import * as qs from "qs";

import { Response } from "@/types";

@Component
export default class Calculator extends Vue {
  link: string | undefined = undefined;
  url: string | undefined = "https://www.google.com/favicon.ico";
  response: Response | undefined = undefined;

  buildLink(type: string, hash: number) {
    const baseUrl = "https://shodan.io/search?";
    const params = {
      query: `${type}:${hash}`
    };
    return baseUrl + qs.stringify(params);
  }

  async calculate() {
    try {
      const response = await axios.get<Response>("/hash", {
        params: { url: this.url }
      });
      this.response = response.data;
      this.link = this.buildLink(this.response.type, this.response.hash);

      this.$forceUpdate();
    } catch (error) {
      const data = error.response.data;
      if ("error" in data) {
        alert(data.error);
      } else {
        alert(error);
      }
    }
  }
}
</script>
