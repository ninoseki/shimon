<template>
  <div class="box content is-normal">
    <h4 class="is-size-4">
      <span class="icon">
        <img src="https://www.google.com/s2/favicons?domain=urlscan.io" alt="shodan" />
      </span>
      urlscan.io
    </h4>
    <QueryTags :queries="queries"></QueryTags>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, type PropType } from "vue"

import QueryTags from "@/components/services/QueryTags.vue"
import type { Fingerprint, Query } from "@/types"

export default defineComponent({
  name: "URLScanComponent",
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
      const baseUrl = "https://urlscan.io/search/#"
      return baseUrl + encodeURI(query)
    }

    const queries = computed<Query[]>(() => {
      const q: Query[] = [
        {
          key: "HTML",
          query: props.fingerprint.html.sha256,
          link: createLink(props.fingerprint.html.sha256)
        }
      ]

      if (props.fingerprint.favicon) {
        q.push({
          key: "Favicon",
          query: props.fingerprint.favicon.sha256,
          link: createLink(props.fingerprint.favicon.sha256)
        })
      }

      ;(props.fingerprint.dns.a || []).forEach((record) => {
        const query = `page.ip:${record.host}`
        q.push({ key: "A", query: record.host, link: createLink(query) })
      })

      return q
    })

    return { queries }
  }
})
</script>
