<template>
  <div class="box content is-normal" v-if="queries.length > 0">
    <h4 class="is-size-4">
      <span class="icon">
        <img src="https://www.google.com/s2/favicons?domain=securitytrails.com" alt="st" />
      </span>
      SecurityTrails
    </h4>
    <QueryTags :queries="queries"></QueryTags>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, type PropType } from "vue"

import QueryTags from "@/components/services/QueryTags.vue"
import type { Fingerprint, Query } from "@/types"

export default defineComponent({
  name: "SecurityTrailsComponent",
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
      return `https://securitytrails.com/list/ip/${query}`
    }

    const queries = computed<Query[]>(() => {
      return (props.fingerprint.dns.a || []).map((record) => {
        return { key: "A", query: record.host, link: createLink(record.host) }
      })
    })

    return { queries }
  }
})
</script>
