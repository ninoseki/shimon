<template>
  <div class="block content is-normal" v-if="queries.length > 0">
    <h4 class="is-size-4">
      <span class="icon">
        <img src="https://www.google.com/s2/favicons?domain=spyonweb.com" alt="spyonweb" />
      </span>
      SpyOnWeb
      <span class="icon" @click="toggleIsHidden()">
        <font-awesome-icon icon="caret-down" v-if="isHidden" />
        <font-awesome-icon icon="caret-up" v-else />
      </span>
    </h4>
    <QueryTags :queries="queries" v-if="!isHidden" />
  </div>
</template>

<script setup lang="ts">
import { useToggle } from "@vueuse/core"
import { computed, type PropType, ref } from "vue"

import QueryTags from "@/components/services/QueryTags.vue"
import type { Fingerprint, Query } from "@/types"

const props = defineProps({
  fingerprint: {
    type: Object as PropType<Fingerprint>,
    required: true
  }
})

const isHidden = ref(true)

const toggleIsHidden = useToggle(isHidden)

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
</script>
