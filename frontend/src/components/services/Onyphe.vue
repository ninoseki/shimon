<template>
  <div class="box content is-normal">
    <h4 class="is-size-4">
      <span class="icon">
        <img src="https://www.google.com/s2/favicons?domain=onyphe.io" alt="shodan" />
      </span>
      Onyphe
    </h4>
    <QueryTags :queries="queries"></QueryTags>
  </div>
</template>

<script lang="ts">
import * as qs from "qs"
import { computed, defineComponent, type PropType } from "vue"

import QueryTags from "@/components/services/QueryTags.vue"
import type { Fingerprint, Query } from "@/types"

export default defineComponent({
  name: "OnypheComponent",
  props: {
    fingerprint: {
      type: Object as PropType<Fingerprint>,
      required: true
    }
  },
  components: {
    QueryTags
  },
  setup(props) {
    const createLink = (query: string): string => {
      const baseUrl = "https://onyphe.io/search/?"
      const params = {
        query
      }
      return baseUrl + qs.stringify(params)
    }

    const queries = computed<Query[]>(() => {
      const q: Query[] = [
        {
          key: "HTML",
          query: `category:datascan app.http.bodymd5:"${props.fingerprint.html.md5}"`,
          link: createLink(`category:datascan app.http.bodymd5:"${props.fingerprint.html.md5}"`)
        }
      ]

      if (props.fingerprint.favicon) {
        const query = `category:datascan app.favicon.imagemmh3:"${props.fingerprint.favicon?.mmh3}"`
        q.push({ key: "Favicon", query: query, link: createLink(query) })
      }

      return q
    })

    return { queries }
  }
})
</script>
