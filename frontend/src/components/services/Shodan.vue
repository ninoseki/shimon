<template>
  <div class="box content is-normal">
    <h4 class="is-size-4">
      <span class="icon">
        <img src="https://www.google.com/s2/favicons?domain=shodan.io" alt="shodan" />
      </span>
      Shodan
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
  name: "ShodanComponent",
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
      const baseUrl = "https://shodan.io/search?"
      const params = {
        query
      }
      return baseUrl + qs.stringify(params)
    }

    const queries = computed<Query[]>(() => {
      const q: Query[] = [
        {
          key: "HTML",
          query: `http.html_hash:${props.fingerprint.html.mmh3}`,
          link: createLink(`http.html_hash:${props.fingerprint.html.mmh3}`)
        }
      ]

      if (props.fingerprint.html.title) {
        const query = `http.title:'${props.fingerprint.html.title}'`
        q.push({ key: "Title", query: query, link: createLink(query) })
      }

      if (props.fingerprint.favicon) {
        const query = `http.favicon.hash:${props.fingerprint.favicon.mmh3}`
        q.push({ key: "Favicon", query: query, link: createLink(query) })
      }

      if (props.fingerprint.certificate) {
        const query = `ssl.cert.serial:${props.fingerprint.certificate.serial}`
        q.push({ key: "Certificate", query: query, link: createLink(query) })
      }

      ;(props.fingerprint.dns.a || []).forEach((record) => {
        const query = `ip:${record.host}`
        q.push({ key: "A", query: query, link: createLink(query) })
      })

      return q
    })

    return { queries }
  }
})
</script>
