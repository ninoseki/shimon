<template>
  <div class="box content is-normal" v-if="queries.length > 0">
    <h4 class="is-size-4">
      <span class="icon">
        <img src="https://www.google.com/s2/favicons?domain=spyonweb.com" alt="spyonweb" />
      </span>
      SpyOnWeb
    </h4>
    <QueryTags :queries="queries"></QueryTags>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, type PropType } from "vue"

import QueryTags from "@/components/services/QueryTags.vue"
import type { Fingerprint, Query } from "@/types"

export default defineComponent({
  name: "SpyOnWebComponent",
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
      return `https://spyonweb.com/${query}`
    }

    const queries = computed<Query[]>(() => {
      if (props.fingerprint.tracker.googleAnalyticsId) {
        return [
          {
            key: "Google Analytics ID",
            query: props.fingerprint.tracker.googleAnalyticsId,
            link: createLink(props.fingerprint.tracker.googleAnalyticsId)
          }
        ]
      }
      return []
    })

    return { queries }
  }
})
</script>
