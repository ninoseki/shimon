<template>
  <div class="box content is-normal">
    <h4 class="is-size-4">
      <span class="icon">
        <img src="https://www.google.com/s2/favicons?domain=binaryedge.io" alt="binaryedge" />
      </span>
      BinaryEdge
    </h4>
    <QueryTags :queries="queries"></QueryTags>
  </div>
</template>

<script lang="ts">
import * as qs from "qs"
import { computed, defineComponent, type PropType } from "vue"

import QueryTags from "@/components/services/QueryTags.vue"
import type { Fingerprint, Query } from "@/types"
import { convertToColonSeparatedText } from "@/utils"

export default defineComponent({
  name: "BinaryEdgeComponent",
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
      const baseUrl = "https://app.binaryedge.io/services/query?"
      const params = {
        query
      }
      return baseUrl + qs.stringify(params)
    }

    const queries = computed<Query[]>(() => {
      const q: Query[] = [
        {
          key: "HTML",
          query: `web.body.sha256:${props.fingerprint.html.sha256}`,
          link: createLink(`web.body.sha256:${props.fingerprint.html.sha256}`)
        }
      ]

      if (props.fingerprint.favicon) {
        const query = `http.favicon.md5:${props.fingerprint.favicon.md5}`
        q.push({ key: "Favicon", query: query, link: createLink(query) })
      }

      if (props.fingerprint.certificate) {
        const sha1 = convertToColonSeparatedText(props.fingerprint.certificate.sha1)
        const query = `ssl.cert.sha1_fingerprint:"${sha1}"`
        q.push({ key: "Certificate", query: query, link: createLink(query) })
      }

      return q
    })

    return { queries }
  }
})
</script>
